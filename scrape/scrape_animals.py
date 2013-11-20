from bs4 import BeautifulSoup

html = open('animal_names.html', 'r')
target = open('animals.txt', 'w')
soup = BeautifulSoup(html)

table = soup.find_all("table", {"class": "wikitable sortable"})[-1]

for row in table.find_all("tr"):
    animal = row.find("a").get("title")
    str_animal = animal.encode('utf-8')
    target.write("%s\n" % str_animal)

html.close()
target.close()
