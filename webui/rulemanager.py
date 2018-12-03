import os
from np_newsextractor.ruleset import ruleset
from np_newsextractor.rsinterpreter import executeRuleset

PATH_RULE_FOLDER = "schduled_rulesets/"

def listrules():
    """
    list all rules
    :return:
    """
    rules = os.listdir(PATH_RULE_FOLDER)
    ruledata = []
    for rule in rules:
        ruledata.append(getRuleInfo(PATH_RULE_FOLDER+rule))
        print(ruledata)
    return ruledata

def getRuleInfo(rulepath):
    """
    get all rule's information like rule name,website
    :param rulepath: path to rule file
    :return: a list with rule info [name, website]
    """
    with open(rulepath,encoding="utf-8") as f:
        rd = f.readlines()
        return [ rd[1],rd[2], "-SP;".join(rd).replace("\n","") ]

def testRuleset(website,rulesets):
    """
    test if a given ruleset is correct.
    :param website: website of this rule
    :param ruleset: rules for news grab
    :return:  grab result
    """
    rm = ruleset()
    rm.createRuleSet("test rule", website)
    rm.parseRules(raw=rulesets)
    data = executeRuleset(rm)
    return data

if __name__ == "__main__":
    print(listrules())