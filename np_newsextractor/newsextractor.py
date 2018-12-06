from bs4 import BeautifulSoup


class newsextractor:
    shtml = ""
    soup = None
    feeded = False
    nlist = None

    def feedHTML(self, html):
        try:
            self.soup = BeautifulSoup(html, 'html5lib')
            shtml = html
            self.feeded = True
            print("HTML with length of ",len(html),"feeded")
            with open("cache/last_feed.txt","w", encoding="utf-8",) as f:
                f.truncate()
                f.write(html)
        except Exception as e:
            print("err:",e)
        return True, self.soup

    def digested(self, feeded=False):
        self.feeded = feeded
        return self.feeded

    def getNewsList(self, selector):
        if self.feeded:
            self.nlist = self.soup.select(selector)
            print(self.nlist)
            return True, self.nlist
        return False, "msg"

    def getTitleLinks(self, titlefield, linksfield):
        if self.feeded:
            nllist = []
            for tag in self.nlist:
                nllist.append([tag.string, tag[linksfield]])
            return True, nllist
        return False, "err"

    def getFilteredTitleLinks(self, key, titlefield, linksfield):
        if self.feeded:
            nllist = []
            for tag in self.nlist:
                if key == "" or tag.string.find(key) > -1:
                    nllist.append([tag.string, tag[linksfield]])
            return True, nllist
        return False, "err"

    def select(self,selector):
        """
        select an html element
        :param selector:css selector
        :return:selected element in BS4 variable
        """
        self.nlist = self.soup.select(selector)
        return self.nlist

    def selectAll(self, selector, ignorelist=[]):
        """
        select an html element ignore nth-child() in given index,works only for non-container element.
        :param selector: css selector
        :param ignorelist:ignore nth-child() index, empty list works the same as select()
        :return:selected list filled with elements in BS4 variable
        """
        if len(ignorelist) == 0:
            return self.select(selector)
        nthchild = ":nth-child("
        nthchildlen = len(nthchild)
        if selector.count(nthchild) < len(ignorelist):
            raise Exception("nth-child() not enough.")
        sortedigl = sorted(ignorelist)
        newselector = selector
        for ig in sortedigl:
            begindex = 0
            endindex = 0
            for i in range(1,ig+1):
                begindex = newselector.find(nthchild,begindex)
                endindex = newselector.find(")",begindex)
                begindex += nthchildlen
            begindex -= nthchildlen
            newselector = newselector[:begindex] + newselector[endindex+1:]
            sortedigl = [ ix-1 for ix  in sortedigl ]
        newselector = newselector.replace("nth-child","nth-of-type")
        self.nlist = self.soup.select(newselector)
        #print(len(self.nlist),"selected. New_selector=", newselector)
        return self.nlist

    def getAllFilteredTitleLinks(self,key=[],staglist=[]):
        """
        get filtered title-link list
        :param staglist: selected tag list by selectAll()
        :param key: key to filter titles
        :return: 2D list with title and links
        """
        data = []
        if len(staglist) == 0:
            staglist = self.nlist
        if len(key) > 0:
            for tag in staglist:
                for k in key:
                    if tag.string.find(k) > -1:
                        data.append([tag.string, tag["href"]])
        else:
            for tag in staglist:
                    data.append([tag.string, tag["href"]])
        return data


if __name__ == "__main__":
    with open("../tests/testdata1.txt", encoding="utf-8") as f:
        testhtml = f.read()
        v = newsextractor()
        v.feedHTML(testhtml)
        v.getNewsList(
            "body > div.main-wrap > div.cnbeta-update > div > div.cnbeta-update-list > div.items-area > div > dl > dt > a")
        status, news = v.getTitleLinks("string", "href")
        print(news)
    with open("../tests/td2", encoding="utf-8") as f:
        testhtml = f.read()
        v = newsextractor()
        v.feedHTML(testhtml)
        v.getNewsList(
            "#filtered-post-container > article.post-archive.post.type-post.status-publish.format-standard.hentry.category-pc.tag-windows-insider-program > div > header > h2 > a")
        status, news = v.getTitleLinks("string", "href")
        print(news)
    with open("../tests/td4.1",encoding="utf-8") as f:
        testhtml = f.read()
        v = newsextractor()
        v.feedHTML(testhtml)
        v.selectAll(
            "body > div.Mid > div.Mid1 > div.Mid1_M > div:nth-child(1) > div.Mid1Mcon.block > ul.Ptxt.block > li:nth-child(2) > div.txt > a",
            [2])
        news = v.getAllFilteredTitleLinks()
        print(news)
