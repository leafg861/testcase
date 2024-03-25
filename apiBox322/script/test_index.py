# 导包
import logging
import unittest
import app
# 2.定义测试类

from api.index import IndexApi


class TestIndex(unittest.TestCase):
    # 初始化方法：已封装类实例化类对象
    @classmethod
    def setUpClass(cls) -> None:
        cls.index_api = IndexApi()  # 拿到类对象，直接调用类方法

    # 调用已封装的测试接口
    # 调用获取轮播图接口的方法
    def test01_get_banner(self):
        # 测试数据
        banner_id = app.bid
        # 发送请求
        response = self.index_api.get_banner(banner_id)
        json_data = response.json()  # 将结果转为json数据
        logging.info(f"获取轮播图的结果为:{json_data}")  # 结果通过日志信息打印
        # 结果断言
        self.assertEqual(200, response.status_code)  # 断言响应状态码
        self.assertEqual(banner_id, json_data.get("id"))

    # 调用获取专题栏位的接口
    def test02_get_theme(self):
        # 测试数据
        ids = app.ids
        # 发送请求
        response = self.index_api.get_theme(ids)
        json_data = response.json()
        logging.info(f"获取专题栏的结果为:{json_data}")
        # 结果断言
        # 响应状态码
        self.assertEqual(200, response.status_code)
        # 断言列表的长度
        self.assertIsNotNone(len(json_data))
        # 将列表元素取出之后再断言
        # self.assertEqual(1,json_data[0].get("id"))

    # 获取最近新品接口
    def test03_get_recent_product(self):
        # 测试数据
        response = self.index_api.get_recent_prodict()
        # 发送请求
        json_data = response.json()
        logging.info(f"获取商品的结果为:{json_data}")
        # 结果断言
        self.assertEqual(200,response.status_code)
        self.assertIsNotNone(len(json_data))
