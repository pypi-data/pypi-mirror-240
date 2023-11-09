# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from humanloop.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from humanloop.api_response import AsyncGeneratorResponse
from humanloop import api_client, exceptions
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

from humanloop.model.experiment_config_response import ExperimentConfigResponse as ExperimentConfigResponseSchema
from humanloop.model.label_sentiment import LabelSentiment as LabelSentimentSchema
from humanloop.model.experiment_status import ExperimentStatus as ExperimentStatusSchema
from humanloop.model.create_project_request import CreateProjectRequest as CreateProjectRequestSchema
from humanloop.model.validation_error_loc import ValidationErrorLoc as ValidationErrorLocSchema
from humanloop.model.model_config_evaluator_aggregate_response import ModelConfigEvaluatorAggregateResponse as ModelConfigEvaluatorAggregateResponseSchema
from humanloop.model.evaluator_arguments_type import EvaluatorArgumentsType as EvaluatorArgumentsTypeSchema
from humanloop.model.project_model_config_feedback_stats_response import ProjectModelConfigFeedbackStatsResponse as ProjectModelConfigFeedbackStatsResponseSchema
from humanloop.model.config_response import ConfigResponse as ConfigResponseSchema
from humanloop.model.project_user_response import ProjectUserResponse as ProjectUserResponseSchema
from humanloop.model.project_response import ProjectResponse as ProjectResponseSchema
from humanloop.model.evaluator_response import EvaluatorResponse as EvaluatorResponseSchema
from humanloop.model.feedback_label_request import FeedbackLabelRequest as FeedbackLabelRequestSchema
from humanloop.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from humanloop.model.positive_label import PositiveLabel as PositiveLabelSchema
from humanloop.model.feedback_type_request import FeedbackTypeRequest as FeedbackTypeRequestSchema
from humanloop.model.config_type import ConfigType as ConfigTypeSchema
from humanloop.model.experiment_response import ExperimentResponse as ExperimentResponseSchema
from humanloop.model.project_config_response import ProjectConfigResponse as ProjectConfigResponseSchema
from humanloop.model.evaluator_return_type_enum import EvaluatorReturnTypeEnum as EvaluatorReturnTypeEnumSchema
from humanloop.model.feedback_types import FeedbackTypes as FeedbackTypesSchema
from humanloop.model.feedback_class import FeedbackClass as FeedbackClassSchema
from humanloop.model.base_metric_response import BaseMetricResponse as BaseMetricResponseSchema
from humanloop.model.validation_error import ValidationError as ValidationErrorSchema

from humanloop.type.config_response import ConfigResponse
from humanloop.type.feedback_class import FeedbackClass
from humanloop.type.project_model_config_feedback_stats_response import ProjectModelConfigFeedbackStatsResponse
from humanloop.type.experiment_response import ExperimentResponse
from humanloop.type.evaluator_arguments_type import EvaluatorArgumentsType
from humanloop.type.positive_label import PositiveLabel
from humanloop.type.feedback_types import FeedbackTypes
from humanloop.type.experiment_status import ExperimentStatus
from humanloop.type.config_type import ConfigType
from humanloop.type.validation_error_loc import ValidationErrorLoc
from humanloop.type.create_project_request import CreateProjectRequest
from humanloop.type.model_config_evaluator_aggregate_response import ModelConfigEvaluatorAggregateResponse
from humanloop.type.feedback_label_request import FeedbackLabelRequest
from humanloop.type.validation_error import ValidationError
from humanloop.type.base_metric_response import BaseMetricResponse
from humanloop.type.experiment_config_response import ExperimentConfigResponse
from humanloop.type.project_user_response import ProjectUserResponse
from humanloop.type.project_response import ProjectResponse
from humanloop.type.evaluator_response import EvaluatorResponse
from humanloop.type.label_sentiment import LabelSentiment
from humanloop.type.evaluator_return_type_enum import EvaluatorReturnTypeEnum
from humanloop.type.project_config_response import ProjectConfigResponse
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.feedback_type_request import FeedbackTypeRequest

from ...api_client import Dictionary
from humanloop.pydantic.base_metric_response import BaseMetricResponse as BaseMetricResponsePydantic
from humanloop.pydantic.positive_label import PositiveLabel as PositiveLabelPydantic
from humanloop.pydantic.evaluator_arguments_type import EvaluatorArgumentsType as EvaluatorArgumentsTypePydantic
from humanloop.pydantic.validation_error_loc import ValidationErrorLoc as ValidationErrorLocPydantic
from humanloop.pydantic.experiment_status import ExperimentStatus as ExperimentStatusPydantic
from humanloop.pydantic.config_response import ConfigResponse as ConfigResponsePydantic
from humanloop.pydantic.feedback_type_request import FeedbackTypeRequest as FeedbackTypeRequestPydantic
from humanloop.pydantic.config_type import ConfigType as ConfigTypePydantic
from humanloop.pydantic.project_model_config_feedback_stats_response import ProjectModelConfigFeedbackStatsResponse as ProjectModelConfigFeedbackStatsResponsePydantic
from humanloop.pydantic.model_config_evaluator_aggregate_response import ModelConfigEvaluatorAggregateResponse as ModelConfigEvaluatorAggregateResponsePydantic
from humanloop.pydantic.project_config_response import ProjectConfigResponse as ProjectConfigResponsePydantic
from humanloop.pydantic.create_project_request import CreateProjectRequest as CreateProjectRequestPydantic
from humanloop.pydantic.feedback_class import FeedbackClass as FeedbackClassPydantic
from humanloop.pydantic.evaluator_return_type_enum import EvaluatorReturnTypeEnum as EvaluatorReturnTypeEnumPydantic
from humanloop.pydantic.experiment_response import ExperimentResponse as ExperimentResponsePydantic
from humanloop.pydantic.validation_error import ValidationError as ValidationErrorPydantic
from humanloop.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic
from humanloop.pydantic.evaluator_response import EvaluatorResponse as EvaluatorResponsePydantic
from humanloop.pydantic.project_user_response import ProjectUserResponse as ProjectUserResponsePydantic
from humanloop.pydantic.feedback_types import FeedbackTypes as FeedbackTypesPydantic
from humanloop.pydantic.label_sentiment import LabelSentiment as LabelSentimentPydantic
from humanloop.pydantic.project_response import ProjectResponse as ProjectResponsePydantic
from humanloop.pydantic.experiment_config_response import ExperimentConfigResponse as ExperimentConfigResponsePydantic
from humanloop.pydantic.feedback_label_request import FeedbackLabelRequest as FeedbackLabelRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = CreateProjectRequestSchema


request_body_create_project_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'APIKeyHeader',
]
SchemaFor201ResponseBodyApplicationJson = ProjectResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: ProjectResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: ProjectResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationErrorSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: HTTPValidationError


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: HTTPValidationError


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_mapped_args(
        self,
        name: str,
        feedback_types: typing.Optional[typing.List[FeedbackTypeRequest]] = None,
        directory_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if name is not None:
            _body["name"] = name
        if feedback_types is not None:
            _body["feedback_types"] = feedback_types
        if directory_id is not None:
            _body["directory_id"] = directory_id
        args.body = _body
        return args

    async def _acreate_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_project_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_project_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate(
        self,
        name: str,
        feedback_types: typing.Optional[typing.List[FeedbackTypeRequest]] = None,
        directory_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_mapped_args(
            name=name,
            feedback_types=feedback_types,
            directory_id=directory_id,
        )
        return await self._acreate_oapg(
            body=args.body,
        )
    
    def create(
        self,
        name: str,
        feedback_types: typing.Optional[typing.List[FeedbackTypeRequest]] = None,
        directory_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_mapped_args(
            name=name,
            feedback_types=feedback_types,
            directory_id=directory_id,
        )
        return self._create_oapg(
            body=args.body,
        )

class Create(BaseApi):

    async def acreate(
        self,
        name: str,
        feedback_types: typing.Optional[typing.List[FeedbackTypeRequest]] = None,
        directory_id: typing.Optional[str] = None,
        validate: bool = False,
    ):
        raw_response = await self.raw.acreate(
            name=name,
            feedback_types=feedback_types,
            directory_id=directory_id,
        )
        if validate:
            return ProjectResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectResponsePydantic, raw_response.body)
    
    
    def create(
        self,
        name: str,
        feedback_types: typing.Optional[typing.List[FeedbackTypeRequest]] = None,
        directory_id: typing.Optional[str] = None,
        validate: bool = False,
    ):
        raw_response = self.raw.create(
            name=name,
            feedback_types=feedback_types,
            directory_id=directory_id,
        )
        if validate:
            return ProjectResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        feedback_types: typing.Optional[typing.List[FeedbackTypeRequest]] = None,
        directory_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_mapped_args(
            name=name,
            feedback_types=feedback_types,
            directory_id=directory_id,
        )
        return await self._acreate_oapg(
            body=args.body,
        )
    
    def post(
        self,
        name: str,
        feedback_types: typing.Optional[typing.List[FeedbackTypeRequest]] = None,
        directory_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_mapped_args(
            name=name,
            feedback_types=feedback_types,
            directory_id=directory_id,
        )
        return self._create_oapg(
            body=args.body,
        )

