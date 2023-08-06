#! /usr/bin/env python
'''
@Author: xiaobaiTser
@Time  : 2022/8/20 22:22
@File  : __init__.py
'''
from typing import Union

# 将pip更新源设置为：https://pypi.douban.com/simple
# pip config set global.index-url https://pypi.douban.com/simple

from selenium import webdriver as selenium_webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys     # 键盘事件
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标事件
# import os; os.system('pip install selenium -i https://pypi.douban.com/simple')

from webdriver_manager.chrome import ChromeDriverManager
# import os; os.system('pip install webdriver_manager -i https://pypi.douban.com/simple')

import pytest
# import os; os.system('pip install pytest pytest-HTML pytest-ordering -i https://pypi.douban.com/simple')

from loguru import logger
# import os; os.system('pip install loguru -i https://pypi.douban.com/simple')

# 当前版本的httpx，只有在异步请求时才略优于requests，此处可使用到发送消息使用
# from httpx import request
# import os; os.system('pip install httpx -i https://pypi.douban.com/simple')

from requests import request
# import os; os.system('pip install requests -i https://pypi.douban.com/simple')

from appium import webdriver as appium_webdriver
# import os; os.system('pip install Appium-Python-Client -i https://pypi.douban.com/simple')

from jmespath import search
# import os; os.system('pip install jmespath -i https://pypi.douban.com/simple')

from yaml import full_load
# import os; os.system('pip install pyyaml -i https://pypi.douban.com/simple')

import click
# import os; os.system('pip install click -i https://pypi.douban.com/simple')

from shutil import copytree
# import os; os.system('pip install shutil -i https://pypi.douban.com/simple')

try:
    from ddddocr import DdddOcr
    img2str = DdddOcr(show_ad=False).classification
except ImportError as e:
    import os; os.system('pip install ddddocr -i https://pypi.douban.com/simple')
    # 如果运行ddddocr运行报错更新opencv库：
    os.system('pip uninstall opencv-python')
    os.system('pip uninstall opencv-contrib-python')
    os.system('pip install opencv-contrib-python')
    os.system('pip install opencv-python')

from iniconfig import IniConfig
from saf.data.config import *

'''
调用飞书机器人发送飞书群消息
@feishu_help_document = https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN

调用钉钉机器人发送钉钉群消息
@dingding_help_document = https://open.dingtalk.com/document/group/custom-robot-access
'''

def send_message(
        url: str = None,
        msg: dict = None,
        assert_path: str = None,
        assert_value: Union[str, int] = None
):
    '''
    发送消息函数
    :param url:             WebHook的URL地址
    :param msg:             WebHook发送的信息
    :param assert_path:     判断内容的路径
    :param assert_value:    判断内容的值
    :return:
    '''
    if not url and not msg:
        raise ('url或者msg信息不能为空，必填内容！')
    else:
        response = request(
                        method='POST',
                        url=url,
                        headers={'Content-Type': 'application/json'},
                        json=msg
                    )
    if assert_path and assert_value:
        try:
            assert assert_value == search(assert_path, response.json())
        except AssertionError as e:
            raise ('信息发送失败！')

def feishu_webhook_send_message(msg:str = '本次测试结束'):
    '''
    使用飞书的webhook发送机器人消息
    :param msg:     需要发送的信息内容，
    :return:
    '''
    send_message(url=feishu.webhook(),
                 msg={
                     'msg_type': 'text',
                     'content': {
                         'text': msg
                     }
                 },
                 assert_path='StatusCode',
                 assert_value=0
    )

def dingding_webhook_send_message(msg:str = '本次测试结束'):
    '''
    使用钉钉的webhook发送机器人消息
    :param msg:     需要发送的信息内容，
    :return:
    '''
    send_message(url=dingding.webhook(),
                 msg={'msgtype': 'text',
                        'text': {
                         'content': msg
                        }
                 },
                 assert_path='errcode',
                 assert_value=0
    )

def robot_send_message(robot_name: str= 'feishu', msg: str = '本次测试结束'):
    ''' 统一调用机器人发送消息 '''
    if 'feishu' in robot_name:
        feishu_webhook_send_message(msg)
    if 'dingding' in robot_name:
        dingding_webhook_send_message(msg)


# if __name__ == '__main__':
#     robot_send_message(robot_name='feishu')