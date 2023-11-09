# coding: utf-8
"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python SDK.  To install the official Python SDK, run the following command:  ```bash pip install humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://humanloop.gitbook.io/humanloop-docs/).

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

import json
import typing
from humanloop.api_response import AsyncGeneratorResponse
from humanloop.apis.tags.chats_api import ChatsApi
from humanloop.apis.tags.completions_api import CompletionsApi
from humanloop.apis.tags.projects_api import ProjectsApi

from humanloop.configuration import Configuration
from humanloop.api_client import ApiClient
from humanloop.type_util import copy_signature


class ClientCustom:
    def __init__(
        self, configuration: typing.Union[Configuration, None] = None, **kwargs
    ):
        if len(kwargs) > 0:
            configuration = Configuration(**kwargs)
        if configuration is None:
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.chats = ChatsApi(api_client)
        self.completions = CompletionsApi(api_client)
        self.projects = ProjectsApi(api_client)

    def get_configs(self, project_id: str):
        return self.projects.get_configs(project_id)

    async def aget_configs(self, project_id: str):
        return self.projects.aget_configs(project_id)

    async def _parsed_generator(self, generator: typing.AsyncGenerator):
        async for line in generator:
            parsed = _parse_sse_chunk(line)
            if parsed is None:
                continue
            try:
                as_json = json.loads(parsed)

                output = as_json["data"][0]["output"]
                id = as_json["data"][0]["id"]
                yield {"output": output, "id": id}
            except Exception as e:
                # move on silently
                pass

    @copy_signature(ChatsApi.acreate)
    async def chat_stream(self, *args, **kwargs):
        kwargs["stream"] = True
        args = self.chats._create_mapped_args(*args, **kwargs)
        response: AsyncGeneratorResponse = await self.chats._acreate_oapg(stream=True, body=args.body)  # type: ignore
        return AsyncGeneratorResponse(
            headers=response.headers,
            status=response.status,
            content=self._parsed_generator(response.content),
            response=response.response,
        )

    @copy_signature(ChatsApi.acreate_deployed)
    async def chat_deployed_stream(self, *args, **kwargs):
        kwargs["stream"] = True
        args = self.chats._create_deployed_mapped_args(*args, **kwargs)
        response: AsyncGeneratorResponse = await self.chats._acreate_deployed_oapg(stream=True, body=args.body)  # type: ignore
        return AsyncGeneratorResponse(
            headers=response.headers,
            status=response.status,
            content=self._parsed_generator(response.content),
            response=response.response,
        )

    @copy_signature(ChatsApi.acreate_experiment)
    async def chat_experiment_stream(self, *args, **kwargs):
        kwargs["stream"] = True
        args = self.chats._create_experiment_mapped_args(*args, **kwargs)
        response: AsyncGeneratorResponse = await self.chats._acreate_experiment_oapg(stream=True, body=args.body)  # type: ignore
        return AsyncGeneratorResponse(
            headers=response.headers,
            status=response.status,
            content=self._parsed_generator(response.content),
            response=response.response,
        )

    @copy_signature(ChatsApi.acreate_model_config)
    async def chat_model_config_stream(self, *args, **kwargs):
        kwargs["stream"] = True
        args = self.chats._create_model_config_mapped_args(*args, **kwargs)
        response: AsyncGeneratorResponse = await self.chats._acreate_model_config_oapg(stream=True, body=args.body)  # type: ignore
        return AsyncGeneratorResponse(
            headers=response.headers,
            status=response.status,
            content=self._parsed_generator(response.content),
            response=response.response,
        )

    @copy_signature(CompletionsApi.acreate)
    async def complete_stream(self, *args, **kwargs):
        kwargs["stream"] = True
        args = self.completions._create_mapped_args(*args, **kwargs)
        response: AsyncGeneratorResponse = await self.completions._acreate_oapg(stream=True, body=args.body)  # type: ignore
        return AsyncGeneratorResponse(
            headers=response.headers,
            status=response.status,
            content=self._parsed_generator(response.content),
            response=response.response,
        )

    @copy_signature(CompletionsApi.acreate_deployed)
    async def complete_deployed_stream(self, *args, **kwargs):
        kwargs["stream"] = True
        args = self.completions._create_deployed_mapped_args(*args, **kwargs)
        response: AsyncGeneratorResponse = await self.completions._acreate_deployed_oapg(stream=True, body=args.body)  # type: ignore
        return AsyncGeneratorResponse(
            headers=response.headers,
            status=response.status,
            content=self._parsed_generator(response.content),
            response=response.response,
        )

    @copy_signature(CompletionsApi.acreate_experiment)
    async def complete_experiment_stream(self, *args, **kwargs):
        kwargs["stream"] = True
        args = self.completions._create_experiment_mapped_args(*args, **kwargs)
        response: AsyncGeneratorResponse = await self.completions._acreate_experiment_oapg(stream=True, body=args.body)  # type: ignore
        return AsyncGeneratorResponse(
            headers=response.headers,
            status=response.status,
            content=self._parsed_generator(response.content),
            response=response.response,
        )

    @copy_signature(CompletionsApi.acreate_model_config)
    async def complete_model_config_stream(self, *args, **kwargs):
        kwargs["stream"] = True
        args = self.completions._create_model_config_mapped_args(*args, **kwargs)
        response: AsyncGeneratorResponse = await self.completions._acreate_model_config_oapg(stream=True, body=args.body)  # type: ignore
        return AsyncGeneratorResponse(
            headers=response.headers,
            status=response.status,
            content=self._parsed_generator(response.content),
            response=response.response,
        )


def _parse_sse_chunk(chunk: bytes):
    """Parse a single Server-Sent Event byte chunk (e.g. "data: ....") and return the data (e.g. "....") as a string"""
    decoded = chunk.decode("utf-8")
    if "data: " not in decoded:
        return None
    return decoded.split("data: ")[1].strip()
