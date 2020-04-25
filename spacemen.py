import requests
import datetime


def curr_spacemen():
    r = requests.get('http://api.open-notify.org/astros.json')
    res = r.json()["number"]
    ppl = r.json()["people"]
    now = datetime.datetime.now()
    ppl_cur = ''
    for i in ppl:
        ppl_cur += i.get('name') + ', '

    return f'Current number of spacemen as of {now.strftime("%d-%m-%Y %H:%M")}: {res}. They are: {ppl_cur}'

