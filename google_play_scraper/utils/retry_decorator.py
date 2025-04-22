# coding=utf-8
import random
import time


def retry_with_exponential_backoff(max_retries, initial_delay=1.0, backoff_factor=2.0, max_delay=None):
    """
    重试装饰器，使用指数退避策略。

    参数:
    - max_retries: 最大重试次数
    - initial_delay: 初始等待时间（秒）
    - backoff_factor: 退避因子，每次重试等待时间将乘以这个因子
    - max_delay: 最大等待时间（秒）
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            delay = initial_delay
            for i in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == max_retries - 1:
                        raise  # 重试次数耗尽后，重新抛出最后一次的异常
                    else:
                        # 计算下一次的延迟
                        time_to_wait = min(delay, max_delay) if max_delay else delay
                        time.sleep(time_to_wait)
                        print(f"Retry {i + 1}: Waiting {time_to_wait} seconds after an error: {e}")
                        # 更新延迟时间
                        delay *= backoff_factor
                        # 可以选择加入随机性来避免冲突
                        delay += random.uniform(0, delay * 0.1)

        return wrapper

    return decorator
