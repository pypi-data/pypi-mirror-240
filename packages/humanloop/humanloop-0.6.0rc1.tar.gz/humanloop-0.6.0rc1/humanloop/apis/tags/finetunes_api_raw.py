# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from humanloop.paths.projects_project_id_finetunes.post import CreateRaw
from humanloop.paths.projects_project_id_finetunes.get import ListAllForProjectRaw
from humanloop.paths.projects_project_id_finetunes_summary.post import SummaryRaw
from humanloop.paths.finetunes_id.patch import UpdateRaw


class FinetunesApiRaw(
    CreateRaw,
    ListAllForProjectRaw,
    SummaryRaw,
    UpdateRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
