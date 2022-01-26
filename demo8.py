#爬取猫眼电影（使用正则表达式）

import re, requests, json


class Maoyan:

    def __init__(self, url):
        self.url = url
        self.movie_list = []
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
        }
        self.parse()

    def parse(self):
        for i in range(10):
            url = self.url + '?offset={}'.format(i * 10)
            response = requests.get(url, headers=self.headers)

            # 用正则筛选数据，有个原则：不断缩小筛选范围。
            dl_pattern = re.compile(r'<dl class="board-wrapper">(.*?)</dl>', re.S)
            dl_content = dl_pattern.search(response.text).group()

            dd_pattern = re.compile(r'<dd>(.*?)</dd>', re.S)
            dd_list = dd_pattern.findall(dl_content)
            # print(dd_list)
            movie_list = []
            for dd in dd_list:
                print(dd)
                item = {}
                # ------------电影名字
                movie_pattern = re.compile(r'title="(.*?)" class=', re.S)
                movie_name = movie_pattern.search(dd).group(1)
                # print(movie_name)
                actor_pattern = re.compile(r'<p class="star">(.*?)</p>', re.S)
                actor = actor_pattern.search(dd).group(1).strip()
                # print(actor)
                play_time_pattern = re.compile(r'<p class="releasetime">(.*?)：(.*?)</p>', re.S)
                play_time = play_time_pattern.search(dd).group(2).strip()
                # print(play_time)

                # 评分
                score_pattern_1 = re.compile(r'<i class="integer">(.*?)</i>', re.S)
                score_pattern_2 = re.compile(r'<i class="fraction">(.*?)</i>', re.S)
                score = score_pattern_1.search(dd).group(1).strip() + score_pattern_2.search(dd).group(1).strip()
                # print(score)
                item['电影名字：'] = movie_name
                item['主演：'] = actor
                item['时间：'] = play_time
                item['评分：'] = score
                # print(item)
                self.movie_list.append(item)
                # 将电影信息保存到json文件中
            with open('movie.json', 'w', encoding='utf-8') as fp:
                json.dump(self.movie_list, fp)


if __name__ == '__main__':
    base_url = 'https://maoyan.com/board/4'
    Maoyan(base_url)

    with open('movie.json', 'r') as fp:
        movie_list = json.load(fp)
    print(movie_list)

