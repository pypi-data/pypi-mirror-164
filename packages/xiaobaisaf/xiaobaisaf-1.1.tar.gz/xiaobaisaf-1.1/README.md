# simlpe_automation_framework

### 介绍
    simple_automation_framework(简称：SAF)
    使用最简单的模式就可以实现需要功能和测试效果，也是xiaobaiauto2的简化版
    SAF继承了selenium、requests/httpx、appium、loguru、xiaobaiauto2、飞书机器人、钉钉机器人、企业微信机器人（暂时不支持）、禅道提单API
    

### 软件架构
    xiaobaiauo2的简化版

### 版本注意
    尽量使用Python 3.9.* 版本
    防止某些库出现不兼容问题，导致功能不可使用

### 安装教程
```commandline
pip config set global.index-url https://pypi.douban.com/simple    注：将pip源修改为国内源
pip install saf
```

### 使用说明
- 优先修改saf/data/config.py中飞书/钉钉的webhook
```python
class feishu(object):
    @staticmethod
    def webhook():
        return 'https://open.feishu.cn/open-apis/bot/v2/hook/xxxx'

class dingding(object):
    @staticmethod
    def webhook():
        return 'https://oapi.dingtalk.com/robot/send?access_token=xxxxxxxx'
```
- conftest.py（保持此文件与用例文件在同目录下）
```python
# filename = conftest.py
from saf import *

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    :param item:
    """
    outcome = yield
    report = outcome.get_result()
    if report.outcome == 'failed':
        # 调用机器人发送执行结果
        robot_send_message(robot_name='feishu', msg=f'测试脚本：{report.nodeid.split("::")[0]}\n测试用例：{report.nodeid.split("::")[1]}\n测试结果：{report.outcome}')
        # robot_send_message(robot_name='dingding', msg=f'测试脚本：{report.nodeid.split("::")[0]}\n测试用例：{report.nodeid.split("::")[1]}\n测试结果：{report.outcome}')
        # robot_send_message(robot_name='feishu,dingding', msg=f'测试脚本：{report.nodeid.split("::")[0]}\n测试用例：{report.nodeid.split("::")[1]}\n测试结果：{report.outcome}')
```
- 用例文件
```python
# fielname = test_xiaobai_auto_script.py

def setup_module():
    ''' 用例脚本执行之前需要准备的信息 '''
    ...

def teardown_module():
    ''' 用例脚本执行之后需要清除的信息 '''

def setup_function():
    ''' 初始化测试用例执行之前状态信息 '''
    ...

def teardown_function():
    ''' 清除测试用例执行之后所产生的信息 '''
    ...

def test_yewu_name_a():
    ''' 用例函数
        需要针对业务场景的测试步骤的实现
            1、UI测试就是定位需要操作的界面节点然后执行操作
            2、API测试就是执行相关接口实现接口的功能
        需要针对每次的结果添加断言进行判断处理
    '''

def test_yewu_name_b():
    ''' 用例函数
        需要针对业务场景的测试步骤的实现
            1、UI测试就是定位需要操作的界面节点然后执行操作
            2、API测试就是执行相关接口实现接口的功能
        需要针对每次的结果添加断言进行判断处理
    '''

```
##### saf>=1.0, 拷贝web自动化模板到D:\autoProject目录下
```commandline

xiaobaicmd -t web -d D:\autoProject
```


### 参与贡献
[selenium官网文档](https://www.selenium.dev/documentation/, "selenium官网文档")

[requests官网文档](https://requests.readthedocs.io/en/latest/, "requests官网文档")

[appium官网](http://appium.io/, "appium官网")

[loguru官方文档](https://loguru.readthedocs.io/en/stable/overview.html, "loguru官方文档")

[xiaobaiauto2帮助文档](https://pypi.org/project/xiaobaiauto2/, "xiaobaiauto2帮助文档")

[飞书机器人获取WebHook](https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN?lang=zh-CN, "飞书机器人获取WebHook")

[钉钉机器人获取WebHook](https://open.dingtalk.com/document/group/custom-robot-access, "钉钉机器人获取WebHook")

[163邮箱配置](http://help.163.com/09/1223/14/5R7P3QI100753VB8.html, "163邮箱配置")

[QQ邮箱配置](https://service.mail.qq.com/cgi-bin/help?subtype=1&id=28&no=369, "QQ邮箱配置")

### 更新日志

| version | info            |
|---------|-----------------|
| 1.0     | 基本实现web自动化模板功能  |