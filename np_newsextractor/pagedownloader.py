import urllib3

class npPageDownloder:
    def getPage(self,url,timeout=30):
        urllib3.disable_warnings()
        http = urllib3.PoolManager()
        response = http.request('GET', url, headers={'User-Agent': "Mozilla/5.0",'accept': "*/*"},decode_content=True)
        return response.data

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
    print(type(t),len(t))
    t = v.getPage("https://www.qq.com/")
    print(type(t),len(t))
    t = v.getPage("https://blogs.windows.com/windowsexperience/tag/windows-insider-program")
    print(type(t),len(t))
