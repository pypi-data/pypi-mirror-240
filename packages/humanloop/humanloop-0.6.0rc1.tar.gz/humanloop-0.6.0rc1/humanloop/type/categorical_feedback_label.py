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

from humanloop.type.label_sentiment import LabelSentiment

class RequiredCategoricalFeedbackLabel(TypedDict):
    value: str

    # Whether the feedback sentiment is positive or negative.
    sentiment: LabelSentiment

class OptionalCategoricalFeedbackLabel(TypedDict, total=False):
    pass

class CategoricalFeedbackLabel(RequiredCategoricalFeedbackLabel, OptionalCategoricalFeedbackLabel):
    pass
