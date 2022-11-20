"""
1. 多组件的pipline计数架构
    - 复杂的事情不会一下子做完， 而是会分很多的中间步骤去完成
2. 生产者-消费者架构
    待爬取的url列表 -> 线程组1（网页下载） -> 下载好的网页队列 -> 线程组2解析存储 -> 解析后的结果数据 -> mysql

3.多线程数据通信 queue.Queue, 用于多线程之间线程安全的数据通信

"""
import queue
import blog_spider
import time
import random
import threading


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)
        html_queue.put(html)
        print(threading.current_thread().name, f"craw {url}", "url_queue.size=", url_queue.qsize())
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, f_out):
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        for result in results:
            f_out.write(str(result) + " \n")
        print(threading.current_thread().name, f"result.size", len(results), "url_queue.size=", html_queue.qsize())
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    u_queue = queue.Queue()
    h_queue = queue.Queue()
    for url in blog_spider.urls:
        u_queue.put(url)

    for idx in range(3):
        t = threading.Thread(target=do_craw, args=(u_queue, h_queue), name=f"craw{idx}")
        t.start()

    out = open("2.data.txt", "w")
    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(h_queue, out), name=f"craw{idx}")
        t.start()

