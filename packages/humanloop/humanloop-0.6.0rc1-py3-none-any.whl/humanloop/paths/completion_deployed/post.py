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

from humanloop.model.completion_response import CompletionResponse as CompletionResponseSchema
from humanloop.model.data_response import DataResponse as DataResponseSchema
from humanloop.model.tool_result_response import ToolResultResponse as ToolResultResponseSchema
from humanloop.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from humanloop.model.validation_error_loc import ValidationErrorLoc as ValidationErrorLocSchema
from humanloop.model.usage import Usage as UsageSchema
from humanloop.model.provider_api_keys import ProviderApiKeys as ProviderApiKeysSchema
from humanloop.model.completion_deployed_request import CompletionDeployedRequest as CompletionDeployedRequestSchema
from humanloop.model.completion_response_provider_responses import CompletionResponseProviderResponses as CompletionResponseProviderResponsesSchema
from humanloop.model.validation_error import ValidationError as ValidationErrorSchema

from humanloop.type.completion_deployed_request import CompletionDeployedRequest
from humanloop.type.provider_api_keys import ProviderApiKeys
from humanloop.type.validation_error import ValidationError
from humanloop.type.completion_response_provider_responses import CompletionResponseProviderResponses
from humanloop.type.data_response import DataResponse
from humanloop.type.validation_error_loc import ValidationErrorLoc
from humanloop.type.usage import Usage
from humanloop.type.completion_response import CompletionResponse
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.tool_result_response import ToolResultResponse

from ...api_client import Dictionary
from humanloop.pydantic.completion_deployed_request import CompletionDeployedRequest as CompletionDeployedRequestPydantic
from humanloop.pydantic.usage import Usage as UsagePydantic
from humanloop.pydantic.validation_error import ValidationError as ValidationErrorPydantic
from humanloop.pydantic.validation_error_loc import ValidationErrorLoc as ValidationErrorLocPydantic
from humanloop.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic
from humanloop.pydantic.data_response import DataResponse as DataResponsePydantic
from humanloop.pydantic.completion_response import CompletionResponse as CompletionResponsePydantic
from humanloop.pydantic.provider_api_keys import ProviderApiKeys as ProviderApiKeysPydantic
from humanloop.pydantic.tool_result_response import ToolResultResponse as ToolResultResponsePydantic
from humanloop.pydantic.completion_response_provider_responses import CompletionResponseProviderResponses as CompletionResponseProviderResponsesPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = CompletionDeployedRequestSchema


request_body_completion_deployed_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'APIKeyHeader',
]
SchemaFor200ResponseBodyApplicationJson = CompletionResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CompletionResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CompletionResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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
    '200': _response_for_200,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_deployed_mapped_args(
        self,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if project is not None:
            _body["project"] = project
        if project_id is not None:
            _body["project_id"] = project_id
        if session_id is not None:
            _body["session_id"] = session_id
        if session_reference_id is not None:
            _body["session_reference_id"] = session_reference_id
        if parent_id is not None:
            _body["parent_id"] = parent_id
        if parent_reference_id is not None:
            _body["parent_reference_id"] = parent_reference_id
        if inputs is not None:
            _body["inputs"] = inputs
        if source is not None:
            _body["source"] = source
        if metadata is not None:
            _body["metadata"] = metadata
        if provider_api_keys is not None:
            _body["provider_api_keys"] = provider_api_keys
        if num_samples is not None:
            _body["num_samples"] = num_samples
        if logprobs is not None:
            _body["logprobs"] = logprobs
        if stream is not None:
            _body["stream"] = stream
        if suffix is not None:
            _body["suffix"] = suffix
        if user is not None:
            _body["user"] = user
        if environment is not None:
            _body["environment"] = environment
        args.body = _body
        return args

    async def _acreate_deployed_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Completion Deployed
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
        serialized_data = request_body_completion_deployed_request.serialize(body, content_type)
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


    def _create_deployed_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Completion Deployed
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
        serialized_data = request_body_completion_deployed_request.serialize(body, content_type)
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


class CreateDeployedRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_deployed(
        self,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_deployed_mapped_args(
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
            environment=environment,
        )
        return await self._acreate_deployed_oapg(
            body=args.body,
        )
    
    def create_deployed(
        self,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_deployed_mapped_args(
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
            environment=environment,
        )
        return self._create_deployed_oapg(
            body=args.body,
        )

class CreateDeployed(BaseApi):

    async def acreate_deployed(
        self,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
        validate: bool = False,
    ):
        raw_response = await self.raw.acreate_deployed(
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
            environment=environment,
        )
        if validate:
            return CompletionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CompletionResponsePydantic, raw_response.body)
    
    
    def create_deployed(
        self,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
        validate: bool = False,
    ):
        raw_response = self.raw.create_deployed(
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
            environment=environment,
        )
        if validate:
            return CompletionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CompletionResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_deployed_mapped_args(
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
            environment=environment,
        )
        return await self._acreate_deployed_oapg(
            body=args.body,
        )
    
    def post(
        self,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_deployed_mapped_args(
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
            environment=environment,
        )
        return self._create_deployed_oapg(
            body=args.body,
        )

