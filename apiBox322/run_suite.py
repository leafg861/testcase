# 1.导包
import unittest

import app
from script.test_index import TestIndex
from script.test_user import TestUser
from unittestreport import TestRunner

# 2.创建测试套件对象
suite = unittest.TestSuite()
# 3.添加测试用例到套件
suite.addTest(unittest.makeSuite(TestIndex))  # 添加测试类的名字
suite.addTest(unittest.makeSuite(TestUser))
# 4.批量执行测试用例
# runner = unittest.TextTestRunner()  # 实例化执行器
# runner.run(suite)

# 5.生成测试报告
# 5.1定义测试报告文件
rep_file = app.BASE_DIR + "/report/Ego.html"
# 5.2创建第三方执行器对象
# 参数：
# filename="report.html",
# report_dir="./reports",
# title='测试报告',
# tester='测试员',
# desc="XX项目测试生成的报告",
# templates=1
runner = TestRunner(suite,
                    filename=rep_file,
                    title="Ego微商项目的接口测试报告",
                    tester="Liang",
                    desc="V1.0",
                    templates=1)
# 5.3执行器调用run方法生成测试报告
runner.run()
