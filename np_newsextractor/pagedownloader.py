import urllib.request

class npPageDownloder:
    def getPage(self,url,timeout=30):
        resp = urllib.request.urlopen(url,timeout=timeout)
        html = resp.read()
        return self.convertToString(html)

    def convertToString(self,bhtml):
        shtml = ""
        try:
            shtml = bhtml.decode("utf-8")
        except:
            try:
                shtml = bhtml.decode("gb2312")
            except:
                pass
        return shtml

if __name__ == "__main__":
    v = npPageDownloder()
    t = v.getPage("https://www.cnbeta.com/topics/4.htm")
    print(type(t),t)