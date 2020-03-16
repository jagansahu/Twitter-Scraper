from bs4 import BeautifulSoup
import urllib
import urllib.request
import csv

theurl = 'https://twitter.com/UWaterloo'
source = urllib.request.urlopen(theurl)
soup = BeautifulSoup(source, 'html.parser')

name = soup.title.text 
numb = int(input("How many tweets do you want to print?\n")) #takes in number of tweets to be printed
i = 1
substring = "These Tweets are protected"
print("10 MOST RECENT TWEETS AND RETWEETS OF\n" + name + "\n")

file = open("list_of_tweets.csv", "w") #opens csv file
writer = csv.writer(file)
writer.writerow({'Tweet #', 'Tweets'})

#loops through to print the given number of tweets 
for tweets in soup.find_all('div', class_='content'):
  print(i)
  print(tweets.find('p').text)
  print()
  i += 1
  tweet = tweets.find('p').text
  writer.writerow([i, tweet]) #stores data in csv file
  if i == numb+1:
    break

file.close() #closes csv file
