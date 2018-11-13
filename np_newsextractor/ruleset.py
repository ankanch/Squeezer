class ruleset:
    rules = []
    name = ""
    site = ""
    rsc = False
    # Action types definition
    AT_SELECT_ALL = 10
    AT_READ_TITLE_LINKS = 11    # second param is for filtering, keep title with given keyword only

    def createRuleSet(self, name, site):
        if self.rsc != True:
            self.rsc = True
            self.name = name
            self.site = site
            return self.rsc
        return False

    def resetRuleSet(self):
        self.rsc = False
        self.rules = []
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

    def importRules(self, dir, raw=""):
        if self.rsc == False:
            if raw == "":
                with open(dir) as f:
                    v = f.readlines()
                    self.name = v[1]
                    self.site = v[2]
                    self.rules = eval(v[3])
                    return self.rules
            self.rules = eval(raw)
            return self.rules
        return []


if __name__ == "__main__":
    # test for create and export ruleset
    rm = ruleset()
    rm.createRuleSet("tr_1", "http://www.windowslatest.com")
    rm.addStep(rm.AT_SELECT_ALL,
               "#td-outer-wrap > div.td-main-content-wrap.td-main-page-wrap.td-container-wrap > div.td-container.td-pb-article-list > div > div.td-pb-span8.td-main-content > div > div > div.item-details > h3 > a")
    rm.addStep(rm.AT_READ_TITLE_LINKS, "")
    rm.exportRules("../tests/tr_1")

    # test for import ruleset
    rm.resetRuleSet()
    rm.importRules(dir="../tests/tr_1")
    print(rm.name,rm.site)