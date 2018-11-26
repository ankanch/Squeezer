import config as CFG

class newscache:
    path_to_cache = "../tests/news.cache"
    cached_news_list = []
    def load(self):
        """
        load cached news
        :return:
        """
        self.cached_news_list.clear()
        with open(self.path_to_cache,encoding="utf-8") as f:
            self.cached_news_list = f.readlines()
        print(self.cached_news_list)

    def clearExceeds(self):
        """clear news that exceeds maximum limit """
        if len(self.cached_news_list) > CFG.MAX_CACHED_NEWS:
            self.cached_news_list = self.cached_news_list[:CFG.MAX_CACHED_NEWS]
            with open(self.path_to_cache,"w",encoding="utf-8") as f:
                f.truncate()
                f.writelines(self.cached_news_list)

    def filternews(self,newslist):
        """
        filter news (delete news that exist in cached list)
        :param newslist:  news list grabbed
        :return: newslist deleted pushed before
        """
        nnl = []
        for news in newslist:
            if news[0] not in self.cached_news_list and news[0] + "\n" not in self.cached_news_list:
                nnl.insert(0,news)
                self.cached_news_list.insert(0,news[0] + "\n")
        self.clearExceeds()
        return nnl


if __name__ == "__main__":
    nc = newscache()
    nc.load()
    fakenews = [
        ["有趣的微软专利详细介绍了双屏Windows 10设备",1],
        ["年度报告显示微软是 GitHub 最大的贡献者",2],
        ["This is a test 2",3],
        ["This is a test 3",4],
        ["This is a test 1",5],
    ]
    newfakenews = nc.filternews(fakenews)
    print(newfakenews)