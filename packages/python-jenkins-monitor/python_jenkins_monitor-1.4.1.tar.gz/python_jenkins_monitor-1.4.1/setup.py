#############################################
# File Name: setup.py
# Author: wqrf
# Mail: 1074321997@qq.com
# Created Time:  2022-8-24 21:06:00
#############################################

from setuptools import setup, find_packages

setup(
    name = "python_jenkins_monitor",
    version = "1.4.1",
    keywords = ("monitor","jenkins","python","wqrf"),
    description = "Simulate Jenkins scheduled task settings,for monitor.",
    long_description = "If you need help, please email to 1074321997@qq.com \n 根据调用时间和定时设置字符串，返回定时任务的下一次执行时间的时间戳(前10位整数部分)，精确到分。当之后不会再有执行时间，则返回None \n 可完全模拟jenkins的定时任务设置，用在各种自定义的定时任务平台或脚本中",

    license = "MIT",
    url = "https://github.com/Woqurefan",
    author = "wqrf",
    author_email = "1074321997@qq.com",
    packages = ['python_jenkins_monitor'],
)