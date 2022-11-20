

import blog_spider
from concurrent.futures import ThreadPoolExecutor, as_completed

# craw
with ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print("craw over")


# parse
with ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    # for future, url in futures.items():
    #     print(url, future.result())

    # as_completed 的顺序是不定的
    for future in as_completed(futures):
        print(futures[future], future.result())










