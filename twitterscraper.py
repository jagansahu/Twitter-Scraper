from bs4 import BeautifulSoup
import urllib
import urllib.request

theurl = 'https://twitter.com/UWaterlooNews'
source = urllib.request.urlopen(theurl)
soup = BeautifulSoup(source, 'html.parser')

name = soup.title.text

i = 1
print("10 MOST RECENT TWEETS OF\n" + name + "\n")
for tweets in soup.find_all('div', class_='content'):
  print(i)
  print(tweets.find('p').text)
  print()
  i += 1
  if i == 11:
    break
  
  
