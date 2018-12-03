from np_newsextractor.ruleset import ruleset
from np_newsextractor.pagedownloader import npPageDownloder
from np_newsextractor.newsextractor import newsextractor

def executeRuleset(rs):
    name = rs.name
    site = rs.site
    rules = rs.rules

    # download web page
    npd = npPageDownloder()
    rawhtml = npd.getPage(site)

    # feed html ready for extract
    re = newsextractor()
    re.feedHTML(rawhtml)

    data = []
    lastprocess = None

    for rule in rules:
        if rule[0] == ruleset.AT_SELECT_ALL_NEWS:
            re.getNewsList(rule[1])
        if rule[0] == ruleset.AT_READ_TITLE_LINKS:
            status, news = re.getFilteredTitleLinks(rule[1],"string", "href")
            data.extend(news)
        if rule[0] == ruleset.AT_SELECT_ALL:
            re.selectAll(rule[1][0], rule[1][1])
        if rule[0] == ruleset.AT_GETALL_TITLEANDLINKS:
            data.extend(re.getAllFilteredTitleLinks(key=rule[1][0]))
    return data



if __name__ == "__main__":
    # import a ruleset
    rm = ruleset()
    """
    rm.resetRuleSet()
    rm.importRules(dir="../tests/tr_1")
    print(rm.name,rm.site)

    # test interpreter
    data = executeRuleset(rm)
    print(data)
    """
    # import and test
    rm.resetRuleSet()
    rm.importRules(dir="../tests/tr_0")
    print(rm.name,rm.site)
    data = executeRuleset(rm)
    print(data)