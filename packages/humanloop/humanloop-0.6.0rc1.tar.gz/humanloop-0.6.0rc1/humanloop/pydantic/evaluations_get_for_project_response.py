# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal
from pydantic import BaseModel, Field, RootModel

from humanloop.pydantic.config_response import ConfigResponse
from humanloop.pydantic.dataset_response import DatasetResponse
from humanloop.pydantic.evaluation_response import EvaluationResponse
from humanloop.pydantic.evaluation_status import EvaluationStatus
from humanloop.pydantic.evaluator_arguments_type import EvaluatorArgumentsType
from humanloop.pydantic.evaluator_response import EvaluatorResponse
from humanloop.pydantic.evaluator_return_type_enum import EvaluatorReturnTypeEnum
from humanloop.pydantic.model_config_evaluator_aggregate_response import ModelConfigEvaluatorAggregateResponse

EvaluationsGetForProjectResponse = typing.List[EvaluationResponse]
