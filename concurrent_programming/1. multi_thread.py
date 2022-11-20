"""
date: 2022-11
"""
import blog_spider
import threading
from timer import timeit


@timeit
def single_thread():
    for url in blog_spider.urls:
        blog_spider.craw(url)


@timeit
def multi_thread():
    threads = []
    for url in blog_spider.urls:
        threads.append(threading.Thread(target=blog_spider.craw, args=(url,)))

    for thread in threads:
        thread.start()  # 启动

    for thread in threads:
        thread.join()  # 等待结束


if __name__ == '__main__':
    single_thread()
    multi_thread()