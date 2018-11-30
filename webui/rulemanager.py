import os

PATH_RULE_FOLDER = "../schduled_rulesets/"

def listrules():
    """
    list all rules
    :return:
    """
    rules = os.listdir(PATH_RULE_FOLDER)
    ruledata = []
    for rule in rules:
        ruledata.append(getRuleInfo(PATH_RULE_FOLDER+rule))
    return ruledata

def getRuleInfo(rulepath):
    """
    get all rule's information like rule name,website
    :param rulepath: path to rule file
    :return: a list with rule info [name, website]
    """
    with open(rulepath,encoding="utf-8") as f:
        rd = f.readlines()
        return [ rd[1],rd[2] ]

if __name__ == "__main__":
    print(listrules())