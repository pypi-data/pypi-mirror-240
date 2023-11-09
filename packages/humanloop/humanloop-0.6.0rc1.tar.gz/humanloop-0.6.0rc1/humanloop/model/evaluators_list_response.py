# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from humanloop import schemas  # noqa: F401


class EvaluatorsListResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['EvaluatorResponse']:
            return EvaluatorResponse

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['EvaluatorResponse'], typing.List['EvaluatorResponse']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EvaluatorsListResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'EvaluatorResponse':
        return super().__getitem__(i)

from humanloop.model.evaluator_arguments_type import EvaluatorArgumentsType
from humanloop.model.evaluator_response import EvaluatorResponse
from humanloop.model.evaluator_return_type_enum import EvaluatorReturnTypeEnum
