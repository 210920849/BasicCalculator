"""
    加载case包下所有测试用例，并使用HTMLTestRunner执行
"""
from unittest import TestLoader

from lib.HTMLTestRunner import HTMLTestRunner
from common.utils import now

suite = TestLoader().discover("case", "test*.py")  # 加载了所有的测试用例的套件


report_file = f"../report/BasicCalculator_Report_{now()}.html"
with open(report_file, "wb") as f:  # 执行测试用例
    r = HTMLTestRunner(f, title="BasicCalculator测试报告")
    r.run(suite)
