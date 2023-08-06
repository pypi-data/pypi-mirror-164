# /usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Tuple

from .base import BaseAPI, allow_async_call


class CloudAPI(BaseAPI):

    @allow_async_call
    def get_cloud_allfiles(self, folder_token: str, page_size: int = 10, page_token: str = ''):
        """获取文件夹下的清单

        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list
        注：需要将文件夹分享至应用所在群，并给于管理权限
        Returns:
            json
        """
        api = "/drive/v1/files"
        payload = dict(
            app_id=self.client.app_id,
            app_secret=self.client.app_secret,
        )
        params = dict(
            page_size=page_size,
            page_token=page_token,
            folder_token=folder_token,
        )
        result = self.client.request("GET", api=api, payload=payload, params=params)
        return result

    @allow_async_call
    def get_cloud_folderdata(self, folderToken: str):
        """获取文件夹元信息

        https://open.feishu.cn/document/ukTMukTMukTM/uAjNzUjLwYzM14CM2MTN

        Returns:
            json
        """
        api = "/drive/explorer/v2/folder/" + folderToken + "/meta"
        payload = dict(
            app_id=self.client.app_id,
            app_secret=self.client.app_secret,
        )
        params = dict(
        )
        result = self.client.request("GET", api=api, payload=payload, params=params)
        # 返回 Body ：
        # {
        #     "code":0,
        #     "msg":"ok",
        #     "tenant_access_token":"xxxxx",
        #     "expire":7200  // 过期时间，单位为秒（两小时失效）
        # }
        return result

    @allow_async_call
    def creat_cloud_folder(self, name, folder_token: str = ''):
        """在云文件夹下创建文件夹

        https://open.feishu.cn/open-apis/drive/v1/files/create_folder

        Returns:
            json
        """
        api = "/drive/v1/files/create_folder"
        payload = dict(
            app_id=self.client.app_id,
            app_secret=self.client.app_secret,
            name=name,
            folder_token=folder_token,
        )
        result = self.client.request("POST", api=api, payload=payload)
        # 返回 Body ：
        # {
        #     "code":0,
        #     "msg":"ok",
        #     "tenant_access_token":"xxxxx",
        #     "expire":7200  // 过期时间，单位为秒（两小时失效）
        # }
        return result

    @allow_async_call
    def creat_cloud_table(self, title, folder_token: str = ''):
        """在云文件夹下创建表格
        https://open.feishu.cn/open-apis/sheets/v3/spreadsheets

        Args:
            title: 表格名字
            folder_token: 表格所在文件
        Returns:
            json
        Raises:
            FeishuException
        """
        api = "/sheets/v3/spreadsheets"
        payload = dict(
            app_id=self.client.app_id,
            app_secret=self.client.app_secret,
            title=title,
            folder_token=folder_token,
        )
        result = self.client.request("POST", api=api, payload=payload)
        # 返回 Body ：
        # {
        #     "code":0,
        #     "msg":"ok",
        #     "tenant_access_token":"xxxxx",
        #     "expire":7200  // 过期时间，单位为秒（两小时失效）
        # }
        return result

    @allow_async_call
    def get_cloud_tabledata(self, spreadsheetToken: str):
        """获取表格元数据

        https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/metainfo

        Returns:
            json
        """
        api = "/sheets/v2/spreadsheets/" + spreadsheetToken + "/metainfo"
        payload = dict(
            app_id=self.client.app_id,
            app_secret=self.client.app_secret,
        )
        result = self.client.request("GET", api=api, payload=payload)
        return result

    @allow_async_call
    def get_bitable(self, app_token: str):
        """获取多维表格元数据

        https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token

        Returns:
            json
        """
        api = "/bitable/v1/apps/" + app_token
        payload = dict(
            app_id=self.client.app_id,
            app_secret=self.client.app_secret,
        )
        result = self.client.request("GET", api=api, payload=payload)
        return result

    @allow_async_call
    def get_bitable_data(self, app_token: str, page_token: str = None, page_size: int = None):
        """列出数据表

        https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token/tables

        Returns:
            json
        """
        api = "/bitable/v1/apps/" + app_token + '/tables'
        payload = dict(
            app_id=self.client.app_id,
            app_secret=self.client.app_secret,
        )
        params = dict(
            page_token=page_token,
            page_size=page_size,
        )
        result = self.client.request("GET", api=api, payload=payload, params=params)
        return result

    @allow_async_call
    def get_bitable_view_data(self, app_token: str, table_id: str, page_token: str = None, page_size: int = None):
        """列出视图

        https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token/tables/:table_id/views

        Returns:
            json
        """
        api = "/bitable/v1/apps/" + app_token + '/tables/' + table_id + '/views'
        payload = dict(
            app_id=self.client.app_id,
            app_secret=self.client.app_secret,
        )
        params = dict(
            page_token=page_token,
            page_size=page_size,
        )
        result = self.client.request("GET", api=api, payload=payload, params=params)
        return result

    @allow_async_call
    def get_bitable_table_by_record_id(self, app_token: str, table_id: str, record_id: str):
        """根据record_id获取一行数据

        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/get

        Returns:
            json
        """
        api = "/bitable/v1/apps/" + app_token + '/tables/' + table_id + '/records/' + record_id
        payload = dict(
            app_id=self.client.app_id,
            app_secret=self.client.app_secret,
        )
        result = self.client.request("GET", api=api, payload=payload)
        return result

    @allow_async_call
    def get_bitable_table_records(self, app_token: str, table_id: str, view_id: str = None, filter: str = None,
                                  sort: str = None, field_names: str = None, text_field_as_array: bool = True,
                                  user_id_type: str = 'open_id', display_formula_ref: bool = True,
                                  automatic_fields: bool = True, page_token: str = None, page_size: int = None):
        """
        列出记录,根据条件查找，常用字段filter、sort

        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/list

        Returns:
            json
        """
        api = "/bitable/v1/apps/" + app_token + '/tables/' + table_id + '/records'
        payload = dict(
            app_id=self.client.app_id,
            app_secret=self.client.app_secret,
        )
        params = dict(
            view_id=view_id,
            filter=filter,
            sort=sort,
            field_names=field_names,
            text_field_as_array=text_field_as_array,
            user_id_type=user_id_type,
            display_formula_ref=display_formula_ref,
            automatic_fields=automatic_fields,
            page_token=page_token,
            page_size=page_size,
        )
        result = self.client.request("GET", api=api, payload=payload, params=params)
        return result

    @allow_async_call
    def creat_one_bitable_table_record(self, app_token: str, table_id: str, user_id_type: str = 'open_id',
                                       fields: dict = {}):
        """
        新增记录,根据fields

        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/create

        Returns:
            json
        """
        api = "/bitable/v1/apps/" + app_token + '/tables/' + table_id + '/records'
        payload = dict(
            app_id=self.client.app_id,
            app_secret=self.client.app_secret,
            fields=fields,
        )
        params = dict(
            user_id_type=user_id_type,
        )
        result = self.client.request("POST", api=api, payload=payload, params=params)
        return result

    @allow_async_call
    def update_one_bitable_record(self, app_token: str, table_id: str, record_id: str, user_id_type: str = 'open_id',
                                  fields: dict = {}):
        """
        更新记录,根据fields

        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/update

        Returns:
            json
        """
        api = "/bitable/v1/apps/" + app_token + '/tables/' + table_id + '/records'
        payload = dict(
            app_id=self.client.app_id,
            app_secret=self.client.app_secret,
            record_id=self.record_id,
            fields=fields,
        )
        params = dict(
            user_id_type=user_id_type,
        )
        result = self.client.request("PUT", api=api, payload=payload, params=params)
        return result

    @allow_async_call
    def event_by_folder_token(self, file_token: str, file_type: str = 'bitable'):
        """订阅云文档事件

        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/subscribe

        Returns:
            json
        """
        api = "/drive/v1/files/" + file_token + '/subscribe'
        payload = dict(
            app_id=self.client.app_id,
            app_secret=self.client.app_secret,
        )
        params = dict(
            file_type=file_type
        )
        result = self.client.request("POST", api=api, payload=payload, params=params)
        return result
