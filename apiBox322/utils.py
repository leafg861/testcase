# 1.导包
import logging
import app
from logging import handlers


# 2.定义初始化日志函数
def init_log():
    # 定义日志器
    logger = logging.getLogger()  # 初始化日志器对象
    logger.setLevel(logging.INFO)  # 设置日志器对应的日志格式，对应级别
    # 定义处理器
    sh = logging.StreamHandler()  # 控制台处理器
    log_file = app.BASE_DIR + "/log/Ego.log"

    # 文件处理器
    fh = logging.handlers.TimedRotatingFileHandler(log_file,  # 定义日志文件
                                                   when="D",  # 记录日志时间：每天
                                                   interval=1,  # 记录日志的频率
                                                   backupCount=7,  # 保存日志的时间
                                                   encoding="UTF-8",  # 记录日志的编码方式
                                                   )  # 文件处理器
    # 定义格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"  # 字符串格式化输出
    formatter = logging.Formatter(fmt)  # 通过格式化器实例化一个对象
    # 设置处理器的格式
    sh.setFormatter(formatter)  # 将对象添加到处理器中
    fh.setFormatter(formatter)
    # 将处理器添加到日志中
    logger.addHandler(sh)  # 将处理器添加到日志器中
    logger.addHandler(fh)
