#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""多维表记录变更
@author:lenovo
@file: bitable.py
@time: 2022/8/23  16:09
"""
from .base import EventContent


class Bitable_Record_Changed_Event(EventContent):
    """
    事件类型：接收消息
    飞书文档地址：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/events/receive
    """

    @staticmethod
    def event_type():
        return "drive.file.bitable_record_changed_v1"
