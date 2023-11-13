# coding = utf-8
import crawles


class SavePipeline(crawles.Pipeline):  # 数据存储类
    def __init__(self):  # 初始化文件
        self.file = open('test.txt', 'w+', encoding='utf-8')

    def save_data(self, item):  # 数据存储
        self.file.write(str(item) + '\n')

    def close(self):  # 关闭调用
        self.file.close()


class ThreadSpier(crawles.ThreadPool):
    save_class = SavePipeline  # 存储类
    concurrency = 32  # 并发数量
    info_display = True  # 爬取信息显示
    for_index_range = (1, 2)

    def start_requests(self, request, index):
        request.cookies = {
            'Hm_lvt_01dd6a7c493607e115255b7e72de5f40': '1697184576,1698914854',
            'Hm_lpvt_01dd6a7c493607e115255b7e72de5f40': '1698914854',
        }
        request.headers = {
            'authority': 'www.meishij.net',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://www.meishij.net/chufang/diy/jiangchangcaipu/',
            'sec-ch-ua': '\"Microsoft Edge\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '\"Windows\"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
        }

        request.data = {
            'page': index,
        }
        request.url = 'https://www.meishij.net/chufang/diy/jiangchangcaipu/'
        request.method = 'GET'
        request.callback = self.parse
        yield request

    def parse(self, item, request, response):
        # item:存储对象 request:请求对象 response:响应对象
        print(response.text)
        data = (response.findall('<a target="_blank" href="(.*?)" title="(.*?)" class="big">'))

        for index, url in enumerate(data):
            request.url = url[0]
            request.callback = self.ad
            print(11, request)
            yield request

    def ad(self, item, request, response):
        data = response.findall('<h1 class="recipe_title">(.*?)</h1>')
        print(f'数据:{data}')
        for index, i in enumerate(data):
            item['title'] = i
            yield item


ThreadSpier()
