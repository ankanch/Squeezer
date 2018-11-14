
def loadConfidential(dir):
    with open(dir) as f:
        return f.readlines()[0]


if __name__ == "__main__":
    print(loadConfidential("../confidentials/SendGridAPIKey.txt"))