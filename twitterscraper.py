from bs4 import BeautifulSoup
import urllib
import urllib.request

theurl = 'https://twitter.com/UWaterloo'
source = urllib.request.urlopen(theurl)
soup = BeautifulSoup(source, 'html.parser')

name = soup.title.text
numb = int(input("How many tweets do you want to print?\n"))
i = 1
substring = "These Tweets are protected"
print("10 MOST RECENT TWEETS AND RETWEETS OF\n" + name + "\n")

for tweets in soup.find_all('div', class_='content'):
  print(i)
  print(tweets.find('p').text)
  print()
  i += 1
  if i == numb+1:
    break
  
