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
from humanloop.pydantic.model_config_evaluator_aggregate_response import ModelConfigEvaluatorAggregateResponse
from humanloop.pydantic.project_model_config_feedback_stats_response import ProjectModelConfigFeedbackStatsResponse

class ProjectConfigResponse(BaseModel):
    # String ID of project the model config belongs to. Starts with `pr_`.
    project_id: str = Field(alias='project_id')

    # Name of the project the model config belongs to.
    project_name: str = Field(alias='project_name')

    created_at: datetime = Field(alias='created_at')

    updated_at: datetime = Field(alias='updated_at')

    last_used: datetime = Field(alias='last_used')

    config: ConfigResponse = Field(alias='config')

    # Feedback statistics for the project model config.
    feedback_stats: typing.List[ProjectModelConfigFeedbackStatsResponse] = Field(None, alias='feedback_stats')

    # Number of datapoints associated with this project model config.
    num_datapoints: int = Field(None, alias='num_datapoints')

    # The ID of the experiment the model config has been registered to. Only populated when registering a model config to an experiment.
    experiment_id: str = Field(None, alias='experiment_id')

    # Aggregates of evaluators for the model config.
    evaluation_aggregates: typing.List[ModelConfigEvaluatorAggregateResponse] = Field(None, alias='evaluation_aggregates')
