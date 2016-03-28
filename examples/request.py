from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        the_html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs_obj = BeautifulSoup(the_html.read())
        the_title = bs_obj.body.h1
    except AttributeError as e:
        return None
    return the_title

title = get_title("http://www.pythonscraping.com/pages/page1.html")
if title is None:
    print("Title could not be found.")
else:
    print(title)

# find find_all 方法
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs_obj = BeautifulSoup(html.read())
name_list = bs_obj.find_all("span", {"class": "green"})
print([name.get_text() for name in name_list])



# children(), descendants(), next_siblings(), pre_siblings()
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs_obj = BeautifulSoup(html.read())
print([child for child in bs_obj.find("table", {"id": "giftList"}).children])


