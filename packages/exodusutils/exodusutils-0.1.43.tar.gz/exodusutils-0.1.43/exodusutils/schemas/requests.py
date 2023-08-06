from __future__ import annotations
from exodusutils.schemas.input_file import InputFile

import json
import traceback
from enum import Enum
from logging import Logger
from typing import Awaitable, Callable, Dict, List, Optional

import pandas as pd
import requests
from minio import Minio
from pydantic import BaseModel
from pydantic.class_validators import validator
from pydantic.fields import Field

from exodusutils import internal
from exodusutils.enums import DataType
from exodusutils.exceptions.exceptions import ExodusBadRequest
from exodusutils.schemas import Column
from exodusutils.schemas.responses import FailedResp, ModelRespBase
from exodusutils.schemas.uri import MinioURI


class AwaitableReq(BaseModel):
    url: Optional[str] = Field(
        description="The url for the Exodus pod to report to. Default is None",
        default=None,
    )

    def callback(self, stuff: Dict) -> None:
        if self.url is not None:
            requests.post(self.url, data=json.dumps(stuff, allow_nan=True))

    async def run(
        self, func: Callable[[AwaitableReq], Awaitable[ModelRespBase]], logger: Logger
    ) -> None:
        try:
            resp = await func(self)
            logger.info(f"Response = {json.dumps(resp.dict(), indent=4)}")
            self.callback(resp.dict())
        except Exception:
            reason = traceback.format_exc()
            logger.warn(f"Failed to finish request, reason = {reason}")
            self.callback(FailedResp(reason=reason).dict())


class TrainReqBodyBase(AwaitableReq):
    """
    The base schema for training requests.

    Attributes
    ----------
    training_data : str
        The URI for the training data.
    feature_types : List[Column]
        The features present in training data.
    target : Column
        The target column. Must be present in `feature_types`.
    folds : int
        Number of folds for this experiment.
    """

    training_data: str = Field(description="The training data uri")
    feature_types: List[Column] = Field(
        default=[Column(name="foo", data_type="double")],
        description="The features present in training data"
    )
    target: Column = Field(
        default=Column(name="foo", data_type="string"),
        description="The target column. Must be present in feature_types"
    )
    folds: int = Field(
        default=5, ge=2, le=10, description="Number of folds for this experiment"
    )

    @validator("target")
    def check_column(cls, v, values):
        if v not in values.get("feature_types", []):
            raise ExodusBadRequest(
                f"target {v} not found in feature_types {values.get('feature_types', [])}"
            )
        return v

    def get_feature_names(self) -> List[str]:
        """
        Returns the names of the features.
        """
        return [f.name for f in self.feature_types]

    def get_training_df(self, client: Minio) -> pd.DataFrame:
        """
        Returns the Pandas DataFrame from the bytes in training_data field.
        """
        return internal.get_df(
            MinioURI.parse(self.training_data), client, self.feature_types
        )

    def get_features(self, data_type: DataType) -> List[Column]:
        """
        Returns the features with the specified data type.

        Parameters
        ----------
        data_type : DataType
            The specified data type.

        Returns
        -------
        List[Column]
            The features.

        """
        return [f for f in self.feature_types if f.data_type == data_type]

    def get_feature_names_by_data_type(self, data_type: DataType) -> List[str]:
        """
        Helper function for extracting names for features with a specified type.

        Parameters
        ----------
        data_type : DataType
            The specified data type.

        Returns
        -------
        List[str]
            Names of the features.
        """
        return [f.name for f in self.get_features(data_type)]


class TrainIIDReqBody(TrainReqBodyBase):
    """
    The schema for IID training request body.

    Has the following fields:
    - `feature_types`: a list of `Column`s, which is the name of a feature and the feature's data type. Contains the target.
    - `target`: the target `Column`.
    - `folds`: number of cross validation folds we want to train.
    - `random_seed`: random seed. Optional.

    Get dataframes by calling the following methods:
    - `get_training_df`: returns the training data as a Pandas dataframe.
    - `get_holdout_df`: returns the holdout data as a Pandas dataframe if the field is not a `None`. Otherwise returns a `None`.
    - `get_validation_df`: returns the validation data as a Pandas dataframe if the field is not a `None`. Otherwise returns a `None`.
    """

    random_seed: Optional[int] = Field(
        default=None, description="The random seed for this experiment. Optional."
    )
    validation_data: Optional[str] = Field(
        default=None, description="The validation data uri. Optional"
    )
    holdout_data: Optional[str] = Field(
        default=None, description="The holdout data uri. Optional"
    )
    fold_assignment_column_name: Optional[str] = Field(
        default=None,
        description="The name of the fold assignment column. If not provided, Exodus will cut cross validation folds in a modulo fashion. If this field is defined, it is required to be a valid column in the input dataframe. This column is not included in `feature_types`, and will be discarded during training.",
    )

    @validator("fold_assignment_column_name")
    def validate_fold_column(cls, v, values):
        if v is not None:
            data = values["training_data"]
            header = data.decode("utf-8").split("\n")[0].split(",")
            if v not in header:
                raise ExodusBadRequest(
                    f"fold assignment column = {v} not found in header"
                )
        return v

    class Config:
        schema_extra = {
            "examples": [
                {
                    "training_data": "foo,bar\n0,abc\n1,def\n2,ghi\n3,jkl\n4,mnop\n5,qrs\n",
                    "feature_types": [
                        {"name": "foo", "data_type": "double"},
                        {"name": "bar", "data_type": "string"},
                    ],
                    "target": [{"name": "bar", "data_type": "string"}],
                    "folds": 3,
                    "validation_percentage": 0.2,
                    "holdout_data": "foo,bar\n99,zzz\n",
                }
            ]
        }

    def get_holdout_df(self, client: Minio) -> Optional[pd.DataFrame]:
        """
        Returns the Pandas DataFrame from the bytes in holdout_data field, or `None` if none specified.
        """
        if not self.holdout_data:
            return None
        else:
            return internal.get_df(
                MinioURI.parse(self.holdout_data), client, self.feature_types
            )

    def get_validation_df(self, client: Minio) -> Optional[pd.DataFrame]:
        """
        Returns the Pandas DataFrame from the bytes in holdout_data field, or `None` if none specified.
        """
        if not self.validation_data:
            return None
        else:
            return internal.get_df(
                MinioURI.parse(self.validation_data), client, self.feature_types
            )


class PredictReqBody(AwaitableReq):
    """
    The schema for prediction request body.
    """

    model_id: str = Field(description="The specified model id")
    data: str = Field(description="The prediction data as JSON")
    threshold: Optional[float] = Field(
        default=None, description="The threshold for classification predictions"
    )
    keep_columns: List[str] = Field(
        default=[], description="The columns to keep in the prediction response"
    )

    def get_prediction_df(self, feature_types: List[Column]) -> pd.DataFrame:
        """
        Returns the Pandas DataFrame from the bytes in data field.

        If the input data contains any column that is not in `feature_types`, that column will be \
dropped from the resulting dataframe.
        """
        valid_columns = [f.name for f in feature_types]
        df = pd.DataFrame(pd.read_json(self.data, orient="records"))
        valid_features = [f for f in feature_types if f.name in df.columns.tolist()]

        # We only want to keep the columns that are specified in `feature_types`
        return df.drop(
            [c for c in df.columns.tolist() if c not in valid_columns], axis=1
        ).pipe(internal.cast_df_types, valid_features)


class MigrateAction(str, Enum):
    """
    Defines the migration action. Could only be either one of `up` and `down`.
    """

    up = "up"
    down = "down"


class MigrateReqBody(BaseModel):
    """
    The schema for migrate request body.
    """

    action: MigrateAction = Field(description="The migration action")

    class Config:
        use_enum_values = True


class SimpleIIDTrainRequest(BaseModel):
    """
    Contains the following:
    - Absolute path to a local JSON file containing the configuration values
    - A `InputFile` object containing the absolute path to the local input training CSV file.
    - A optional `InputFile` object containing the absolute path to the local input holdout CSV file.
    - A optional `InputFile` object containing the absolute path to the local input validation CSV file.
    """
    config_path: str = Field(description="The path to the local configuration file.")
    training_file: InputFile = Field(description="The absolute path to the local input training file.")
    holdout_file: Optional[InputFile] = Field(description="The absolute path to the local input holdout file. Optional", default=None)
    validation_file: Optional[InputFile] = Field(description="The absolute path to the local input validation file. Optional", default=None)

    def load(self, minio: Minio):
        """
        Loads the JSON config into a `TrainIIDReqBody`.

        The JSON file should contain the following:
        - **features**: A `dict` from `name` to `data_type` for all the column you wish to use.
        - **target_column_name**: The `name` of the target column.
        - **keep_cols**: The name of the columns you wish to keep.
        - **folds**: The number of folds you want to train with.
        """
        with open(self.config_path) as f:
            meta_data = json.loads(f.read())
            features = meta_data["features"]
            feature_types = [{"name": k, "data_type": v} for k, v in features.items()]
            target = [f for f in feature_types if f["name"] == meta_data["target_column_name"]][0]
        training_data = self.training_file.upload(minio)
        validation_data = None if self.validation_file is None else self.validation_file.upload(minio)
        holdout_data = None if self.holdout_file is None else self.holdout_file.upload(minio)
        return TrainIIDReqBody(
            training_data=training_data,
            target=target,
            feature_types=feature_types,
            folds=int(meta_data.get("folds", 5)),
            validation_data=validation_data,
            holdout_data=holdout_data,
            fold_assignment_column_name=meta_data.get("fold_assignment_column_name", None)
        )
