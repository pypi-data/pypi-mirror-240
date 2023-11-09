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

from humanloop.pydantic.feedback_type import FeedbackType

class FeedbackRequest(BaseModel):
    # The type of feedback. The default feedback types available are 'rating', 'action', 'issue', 'correction', and 'comment'.
    type: typing.Union[FeedbackType, str] = Field(alias='type')

    # The feedback value to be set. This field should be left blank when unsetting 'rating', 'correction' or 'comment', but is required otherwise.
    value: str = Field(None, alias='value')

    # ID to associate the feedback to a previously logged datapoint.
    data_id: str = Field(None, alias='data_id')

    # A unique identifier to who provided the feedback.
    user: str = Field(None, alias='user')

    # User defined timestamp for when the feedback was created. 
    created_at: datetime = Field(None, alias='created_at')

    # If true, the value for this feedback is unset.
    unset: bool = Field(None, alias='unset')
