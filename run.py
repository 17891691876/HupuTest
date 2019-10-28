from reports.HTMLTestRunner import HTMLTestRunner
import unittest
import time
import logging

#指定测试用例和测试报告的路径
test_dir = "../test_case"
report_dir = "reports"

#加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_startAd_case.py")
#discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_goldCase.py")
#discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

#定义报告的文件格式
now = time.strftime("%Y-%m-%d %H-%M-%S")
report_name = report_dir + "/" + now + "test_report.html"

#运行用例并生成测试报告
with open(report_name,"wb") as f:
    runner = HTMLTestRunner(stream=f,title="Hupu Test Report",description= "HuPu Android app Test Report")
    logging.info("start run testcase....")
    runner.run(discover)