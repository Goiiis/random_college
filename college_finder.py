from bs4 import BeautifulSoup
import requests
import sqlite3 as sql


def city_string(city_list):
    city_word = ""
    for i in city_list:
        city_word += i
    return city_word

url = "https://www.4icu.org/us/a-z/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tbody = doc.tbody
trs = tbody.contents

ranks = []
names = []
citys = []
test = False
for tr in trs:
    if test:
        break
    loop = 0
    city_letters = []
    for td in tr:
        if test:
            break
        for i in td:
            if test:
                break
            if loop == 1:
                ranks.append(str(i)[str(i).find('<b>')+3:str(i).find('</b>')])
            elif loop == 3:
                names.append(str(i)[str(i).find('">')+2:str(i).find('</a>')])
            elif loop == 5:
                citys.append(i)
                if str(i).find("Youngstown") > -1:
                    test = True
                    break
            loop += 1

connection = sql.connect("college.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE colleges (name, city, rank)")
print(len(names))
for i in range(len(names)):
    try:
        na = names[i]
        ci = citys[i]
        ra = int(ranks[i])
        cursor.execute("INSERT INTO colleges VALUES (?, ?, ?)", (na, ci, ra))
        connection.commit()
    except:
        pass

rows = cursor.execute("SELECT name, city, rank FROM colleges").fetchall()
print(len(rows))
connection.commit()
