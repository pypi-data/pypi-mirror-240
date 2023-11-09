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

from humanloop.type.create_experiment_request_config_ids import CreateExperimentRequestConfigIds
from humanloop.type.positive_label import PositiveLabel

class RequiredCreateExperimentRequest(TypedDict):
    # Name of experiment.
    name: str

    # Feedback labels to treat as positive user feedback. Used to monitor the performance of model configs in the experiment.
    positive_labels: typing.List[PositiveLabel]

class OptionalCreateExperimentRequest(TypedDict, total=False):
    config_ids: CreateExperimentRequestConfigIds

    # Whether to set the created project as the project's active experiment.
    set_active: bool

class CreateExperimentRequest(RequiredCreateExperimentRequest, OptionalCreateExperimentRequest):
    pass
