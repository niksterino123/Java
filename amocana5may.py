from bs4 import BeautifulSoup
import requests


source = requests.get("https://top.ge").text
soup = BeautifulSoup(source, "html.parser")


items = soup.find_all(class_=("stie_title", "row_id"))
new_list = []
for i in items:
    new_list.append(i.contents)

string = ""
for i in range(len(new_list)):
    string += "{}{}\n".format(new_list[i][0] if i % 2 != 0 else"", new_list[i][2][15:17] if i % 2 == 0 else"")

print(string)
