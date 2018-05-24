import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":
    # target="http://www.biqukan.com/1_1094/5403177.html"
    target="http://www.biqukan.com/1_1094/"
    req=requests.get(url=target)
    html=req.text
    div_bf = BeautifulSoup(html, "html.parser")
    div=div_bf.find_all("div",class_="listmain")
    print(div[0])