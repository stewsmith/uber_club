from BeautifulSoup import BeautifulSoup

beers_html = open('beers.html', 'r')
target = open('beer_manf.txt', 'w')
soup = BeautifulSoup(beers_html)

matches = []

for link in soup.findAll('td', {'class':'t'}):
    matches.append(link)

for i in range(0, len(matches), 3):
    manf = matches[i].text
    beer = matches[i+1].text
    target.write(manf + "|" + beer + "\n")

beers_html.close()
target.close()
