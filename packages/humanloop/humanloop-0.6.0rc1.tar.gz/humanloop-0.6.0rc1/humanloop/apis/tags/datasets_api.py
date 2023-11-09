# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from humanloop.paths.projects_project_id_datasets.post import Create
from humanloop.paths.datasets_dataset_id_datapoints.post import CreateDatapoint
from humanloop.paths.datasets_id.delete import Delete
from humanloop.paths.datasets_id.get import Get
from humanloop.paths.projects_project_id_datasets.get import ListAllForProject
from humanloop.paths.datasets_dataset_id_datapoints.get import ListDatapoints
from humanloop.paths.datasets_id.patch import Update
from humanloop.apis.tags.datasets_api_raw import DatasetsApiRaw


class DatasetsApi(
    Create,
    CreateDatapoint,
    Delete,
    Get,
    ListAllForProject,
    ListDatapoints,
    Update,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DatasetsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DatasetsApiRaw(api_client)
