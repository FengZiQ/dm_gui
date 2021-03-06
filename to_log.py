# coding=utf-8

import time


def all_logs(text):
        if text != "'result': 'p'" or text != "'result': 'f'":
            with open("gui_scripts.log", "r+", encoding='utf-8', errors='ignore') as f:
                content = f.read()
                f.seek(0, 0)
                f.write(
                    time.strftime(
                        '%Y-%m-%d %H:%M:%S',
                        time.localtime(time.time())
                    ) + ": " + text + '\n' + content)

                f.close()
            print(text)


def testlink(text=''):
    # for testLink steps populate
    file = open("testLink.notes", "a", encoding='utf-8', errors='ignore')
    file.write(text + '\n')

    file.close()


