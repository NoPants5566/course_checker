from bs4 import *
import datetime
import time
import requests
import winsound


def get_html():
    url = 'http://timetable.unsw.edu.au/2017/GSOE9820.html#S2'
    html_source = requests.get(url)
    plain_html = html_source.text
    soup = BeautifulSoup(plain_html, 'html.parser')
    return soup


def get_course(plain_html):
    for a in plain_html.findAll('tr', {'class': 'rowLowlight'}):
        # print(a)
        for teaching_period in a.findAll('td')[1]:
            if teaching_period.text == 'T2':
                # print('Teaching Period: ' + teaching_period.text)
                for status in a.findAll('td')[4]:
                    return status.string


def main():
    plain_html = get_html()
    result = 'Full'
    while result != 'Open':
        result = get_course(plain_html)
        print(result)
        time.sleep(60)
        print(datetime.datetime.now())
    winsound.Beep(3000, 20000)


if __name__ == "__main__":
    main()