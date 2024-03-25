# 1.导包
import logging
import unittest

# 2.定义测试接口类
import app
from api.user import UserApi


class TestUser(unittest.TestCase):
    # 定义初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.user_api = UserApi()

    # 定义调用接口方法
    # 调用获取token的方法
    def test01_get_token(self):
        # 准备测试数据
        code = app.CODE
        # 发送请求
        response = self.user_api.get_token(code)
        json_data = response.json()
        logging.info(f"获取token的结果为:{json_data}")
        # 结果断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(32, len(json_data.get("token")))  # 断言token值的长度是否为32
        # 断言包含关键词token
        self.assertIn("token", json_data)
        # 保存token值到app.py文件
        # 从header里取token
        app.header["token"] = json_data.get("token")  # 修改字典值,token保存在内存中，app.py文件中不显示
        logging.info(f"保存的token值：{app.header['token']}")

    # 调用验证token接口
    def test01_verify_token(self):
        # 测试数据
        data = app.header.get("token")
        # 发送请求
        response = self.user_api.verify_token(data)
        json_data = response.json()
        logging.info(f"验证token的结果为:{json_data}")
        # 结果断言
        self.assertEqual(200, response.status_code)

        # 断言token值是否为真
        # 第一种
        self.assertEqual(True, json_data.get("isValid"))
        # 第二种
        self.assertTrue(json_data.get("isValid"))

    # 调用获取验证token接口
    def test03_get_address(self):
        # 发送请求
        response = self.user_api.get_address()
        json_data = response.json()
        logging.info(f"获取地址的结果为:{json_data}")
        # 结果断言
        self.assertEqual(200, response.status_code)
        # 断言电话号
        self.assertEqual(app.phone, json_data.get("mobile"))
        self.assertEqual(app.name, json_data.get("name"))
