import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.cnbc.com/2024/03/04/ford-february-sales-hybrids-evs.html')  # r is how we request the site and store it

# prints all content from web page

print(r.url)  # prints url

# parsing the HTML and making it pretty
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

# print("")
# print("END CONTENT TEST")
# print("")
print(soup.title.string)
print(soup.title)
print(soup.title.name)

s = soup.find('div')
lines = s.find_all('p')
print(s)

for line in lines:
    print(line.text)


# for link in soup.find_all('a'):
    # print(link.get('href'))


URLs = ['https://www.cnbc.com/2024/03/04/ford-february-sales-hybrids-evs.html',
        'https://www.nasdaq.com/articles/macys-surges-after-investor-group-sweetens-take-private-bid-to-%246.6-bln']





