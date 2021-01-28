'''
url이 존재할 경우 up 
존재하지 않을 경우 down
url 자체가 아닐 경우 is not url
다시 실행 하고 싶으면 y/n 
y/n 둘중 하나가 아니라 다른값을 입력하면 
That's not a valid answer
'''

import requests
import os

def check_url(url):
    if "." in url:
        if "http" in url:
            pass
        else:
            url = "http://" + url
            pass
        try:
            if requests.get(url).status_code == 200:
                print(f"{url} is up")
        except:    
                print(f"{url} is down")
    else:
        print(f"{url} is not URL")


while True:
    os.system('cls') # 리눅스 환경일경우 'clear'
    print("Welcome to IsItDown.py!")
    print("please write a URLs you want to check.(separated by comma)")
    url = input().split(",")
    for i in url:
        check_url(i.strip())
    while True:
        answer = input("Do you want to start over? y/n")
        if answer == 'y':
            break
        elif answer == 'n':
            print("k. bye!")
            exit()
        else:
            print("That's not a valid answer")
            continue