# 1.导包
import requests

# 2.封装测试类
import app


class IndexApi(object):
    # 定义初始化方法(作用:定义实例化之后的对象和属性)
    def __init__(self):
        self.banner_url = app.URL + "/api/v1/banner/{}"  # 设置全局变量
        self.theme_url = app.URL + "/api/v1/theme"
        self.recent_product_url = app.URL + "/api/v1/product/recent"

    # 定义接口方法
    # 获取轮播图
    def get_banner(self, banner_id):
        new_url = self.banner_url.format(banner_id)  # 格式化输出，替换占位符
        return requests.get(new_url)

    # 获取专题栏位
    def get_theme(self, ids):
        # ?ids=1,2,3 转化为JSON数据,然后和url拼接，再通过get方法发送
        # {“ids”:1,2,3}
        data = {"ids": ids}
        return requests.get(self.theme_url, params=data)  # 添加查询参数

    # 获取最新商品
    def get_recent_prodict(self):
        return requests.get(self.recent_product_url)
