#!/usr/bin/python3
# @Time : 2021/12/16
# @Author : zhanglin

import pytest
from Driver.StartStopConf import StartStopConf

@pytest.fixture(scope="session")
def start_Services():
    print("starts")
    StartStopConf.appium_start()
    StartStopConf.emulator_start()
    # 后置条件：关闭模拟器，关闭appium服务
    yield
    print("stops")
    StartStopConf.emulator_stop()
    StartStopConf.appium_stop()


