import datetime
from time import gmtime, strftime

def convertTime(giventime,timezone):
    """
    [UTC TIMEZONE ONLY]
    convert user given time and timezone to local machine time
    :param giventime: given mail delivery time like HH:MM
    :param timezone: given preferred  timezone like +8
    :return: local machine time
    """
    # get local machine timezone (LMT)
    lmt = strftime("%z", gmtime())[:3]
    ilmt = int(lmt)

    # get user timezone (UT)
    ut = timezone[3:]
    iut = int(ut)

    # converse
    gap = iut - ilmt
    hh = int(giventime[:2])
    hh += gap
    if hh >= 24:
        hh -= 24
    if hh < 0:
        hh += 24
    return str(hh) + giventime[2:]

if __name__ == "__main__":
    print(convertTime("11:50","UTC+7"))
    print(convertTime("11:50", "UTC-7"))
    print(convertTime("11:50", "UTC+0"))