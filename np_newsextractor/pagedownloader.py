import urllib3

class npPageDownloder:
    def getPage(self,url,timeout=30):
        urllib3.disable_warnings()
        http = urllib3.PoolManager()
        response = http.request('GET', 
                                url.replace("\n","").replace("\r","").replace(" ",""), 
                                headers={
                                    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
                                    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                                    'upgrade-insecure-requests': 1,
                                    },
                                decode_content=True)
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
