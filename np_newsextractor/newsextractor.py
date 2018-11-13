from bs4 import BeautifulSoup

class newsextractor:

    shtml = ""
    soup = None
    feeded = False
    nlist = None

    def feedHTML(self,html):
        try:
            self.soup = BeautifulSoup(html, 'html.parser')
            shtml = html
            self.feeded = True
        except:
            print("err")
        return True,self.soup

    def digested(self,feeded=False):
        self.feeded = feeded
        return self.feeded

    def getNewsList(self,selector):
        if self.feeded:
            self.nlist = self.soup.select(selector)
            print(self.nlist)
            return True,self.nlist
        return False,"msg"

    def getTitleLinks(self,titlefield,linksfield):
        if self.feeded:
            nllist = []
            for tag in self.nlist:
                if titlefield == "string":
                    nllist.append([tag.string, tag[linksfield]])
                else:
                    nllist.append( [ tag[titlefield],tag[linksfield] ] )
            return True,nllist
        return False,"err"

    def getFilteredTitleLinks(self,key,titlefield,linksfield):
        if self.feeded:
            nllist = []
            for tag in self.nlist:
                if tag[titlefield].find(tag[titlefield]) > -1:
                    nllist.append( [ tag[titlefield],tag[linksfield] ] )
            return True,nllist
        return False,"err"

if __name__ == "__main__":
    with open("../data/testdata1.txt",encoding="utf-8") as f:
        testhtml = f.read()
        v = newsextractor()
        v.feedHTML(testhtml)
        v.getNewsList("body > div.main-wrap > div.cnbeta-update > div > div.cnbeta-update-list > div.items-area > div > dl > dt > a")
        status,news = v.getTitleLinks("string","href")
        print(news)
    with open("../data/td2",encoding="utf-8") as f:
        testhtml = f.read()
        v = newsextractor()
        v.feedHTML(testhtml)
        v.getNewsList("#filtered-post-container > article.post-archive.post.type-post.status-publish.format-standard.hentry.category-pc.tag-windows-insider-program > div > header > h2 > a")
        status,news = v.getTitleLinks("string","href")
        print(news)