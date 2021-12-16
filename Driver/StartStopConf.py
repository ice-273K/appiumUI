
import os
from time import sleep

from Common.Conf import ReadConfig

class StartStopConf():

    cfg = ReadConfig.ReadConfig().readcfg()

    @classmethod
    def appium_start(cls):
        cfgN = cls.cfg['Appium']
        ip = cfgN['appium_start_ip']
        appium_start_appiumport = cfgN['appium_start_appiumport']
        appium_start_emulatorport = cfgN['appium_start_emulatorport']
        # cmd = 'start  appium -a ' + '127.0.0.1'+' -p '+'4723' +' -bp '+ '21503'
        cmd = 'start  appium -a ' + ip +' -p '+appium_start_appiumport +' -bp '+ appium_start_emulatorport
        return os.popen(cmd=cmd)

    @classmethod
    def appium_stop(cls):
        cfgN = cls.cfg['Appium']
        # cmd = 'taskkill /F /IM node.exe /t'
        cmd = cfgN['appium_stop']
        return os.popen(cmd=cmd)

    @classmethod
    def emulator_start(cls):
        cfgN = cls.cfg['Emulator']
        # cmd = 'memuc start -n MEmu'
        cmd = cfgN['emulator_start']
        os.popen(cmd=cmd)

    @classmethod
    def emulator_stop(cls):
        cfgN = cls.cfg['Emulator']
        # cmd = 'memuc stop -n MEmu'
        cmd = cfgN['emulator_stop']
        return os.popen(cmd=cmd)


