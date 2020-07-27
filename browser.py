import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import init

from colorama import Fore, Back, Style


# use Colorama to make Termcolor work 

init()
# argument in the form of list
args = sys.argv

save_path = args[1]


# saving the files in the given directory
try :
    os.mkdir(save_path)

except Exception as e:
    pass


def soup(file):
    soup = BeautifulSoup(file, 'html.parser')
    str1 = ""
    para = ['[document]', 'head',
            'body', 'h1', 'h2', 'h3', 'h4', 'h5', 'a'
            'h6', 'title', 'span',
            'table', 'div', 'li', 'form']

    for y in para:
        for x in soup.find_all('a'):
            str1 += Fore.BLUE + x.get_text() + "\n"

        for x in soup.find_all(y):
            if y == "a":
                pass
            else:
                if x.string != None:
                    str1 += x.string + "\n"

    return str1




stc = deque()


def info(url):

    if url.startswith("https://"):
        r = requests.get(url)

    else:
        r = requests.get(f"https://{url}")

    return r.text


para = ['title' , "a" , "p" , "ul" , "ol" , "li"]
# write your code here

flag = True

# loop

while flag:
    url = input()
    if url == "exit":
        exit()

    elif url == "bloomberg.com":
        r = info(url)
        str1 = soup(r)
        print(str1)
        with open(f"{save_path}\\bloomberg","w") as f:
            f.write(str1)
        stc.append(url)

    elif url == "nytimes.com":
        r = info(url)
        str1 = soup(r)
        print(str1)
        with open(f"{save_path}\\nytimes", "w") as f:
            f.write(str1)
        stc.append(url)

    elif url == "bloomberg":
        with open(f"{save_path}\\bloomberg") as f:
            content = f.read()
            print(content)

    elif url == "nytimes":
        with open(f"{save_path}\\nytimes") as f:
            content = f.read()
            print(content)




    elif url == "back":
        stc.pop()
        command = stc[0]
        if command == "bloomberg.com":
            r = info(command)
            str1 = soup(r)
            print(str1)



        elif command == "nytimes.com":
            r = info(command)
            str1 = soup(r)
            print(str1)

    elif "." not in url:
        print("Error: Incorrect URL")

    else:
        r = info(url)
        str1 = soup(r)
        print(str1)
        with open(f"{save_path}\\{url}", "w") as f:
            f.write(str1)
        stc.append(url)




