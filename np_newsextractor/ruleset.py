class ruleset:
    rules = []
    name = ""
    site = ""
    rsc = False
    # Action types definition
    AT_SELECT_ALL_NEWS = 10       # 2 element list to match getNewsList(self, selector):
    AT_READ_TITLE_LINKS = 11        # second param is for filtering, keep title with given keyword only , matching getFilteredTitleLinks(self, key, titlefield, linksfield):
    AT_SELECT_ALL = "SELECT_ALL"         #12            # 4 element list to match selectAll(self, selector, ignorelist=[])
    AT_GETALL_TITLEANDLINKS = "GET_NEWS" #13  #2 element list to match getAllFilteredTitleLinks(self,key=[],staglist=[]):

    def createRuleSet(self, name, site):
        if self.rsc != True:
            self.rsc = True
            self.name = name
            self.site = site
            return self.rsc
        return False

    def resetRuleSet(self):
        self.rsc = False
        self.rules.clear()
        self.name = ""
        self.site = ""

    def addStep(self, type, condition):
        if self.rsc:
            ins = [type, condition]
            self.rules.append(ins)
            return True
        return False

    def exportRules(self, dir):
        if self.rsc:
            raw = str(self.rules)
            with open(dir, "w") as f:
                heads = "Squeezer by kanch. This is the rule definition for grabber.\n" + self.name + "\n" + self.site + "\n"
                f.write(heads + raw)
            return raw
        return ""

    def importRules(self, dir):
        if self.rsc == False:
            with open(dir) as f:
                v = f.readlines()
                self.name = v[1]
                self.site = v[2]
                self.rules = eval(v[3])
                return self.rules
        return []

    def parseRules(self,raw=""):
        self.rules = eval(raw)
        return self.rules


if __name__ == "__main__":
    # test for create and export ruleset     AT_SELECT_ALL_NEWS  + AT_READ_TITLE_LINKS
    rm = ruleset()
    rm.createRuleSet("tr_1", "http://www.windowslatest.com")
    rm.addStep(rm.AT_SELECT_ALL_NEWS,
               "#td-outer-wrap > div.td-main-content-wrap.td-main-page-wrap.td-container-wrap > div.td-container.td-pb-article-list > div > div.td-pb-span8.td-main-content > div > div > div.item-details > h3 > a")
    rm.addStep(rm.AT_READ_TITLE_LINKS, "")
    rm.exportRules("../tests/tr_1")
    print(rm.name,rm.site)
    # test for import ruleset
    rm.resetRuleSet()

    # test for create and export ruleset     AT_SELECT_ALL  + AT_GETALL_TITLEANDLINKS
    rm = ruleset()
    rm.createRuleSet("tr_0", "https://www.gamersky.com/")
    rm.addStep(rm.AT_SELECT_ALL,
               ["body > div.Mid > div.Mid1 > div.Mid1_M > div:nth-child(1) > div.Mid1Mcon.block > ul.Ptxt.block > li:nth-child(1) > div.txt > a"
                ,[2],[]])
    rm.addStep(rm.AT_GETALL_TITLEANDLINKS,["",[]])
    rm.exportRules("../tests/tr_0")
    print(rm.name, rm.site)