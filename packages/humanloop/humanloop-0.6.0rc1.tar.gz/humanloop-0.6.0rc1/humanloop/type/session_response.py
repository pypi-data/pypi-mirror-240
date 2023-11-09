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

from humanloop.type.session_project_response import SessionProjectResponse

class RequiredSessionResponse(TypedDict):
    # String ID of session. Starts with `sesh_`.
    id: str

    # List of projects that have datapoints associated to this session.
    projects: typing.List[SessionProjectResponse]

    # Number of datapoints associated to this session.
    datapoints_count: int

    created_at: datetime

class OptionalSessionResponse(TypedDict, total=False):
    # Unique user-provided string identifying the session.
    reference_id: str

    # Inputs for the first datapoint in the session.
    first_inputs: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Output for the last datapoint in the session.
    last_output: str

class SessionResponse(RequiredSessionResponse, OptionalSessionResponse):
    pass
