from bs4 import BeautifulSoup
import urllib
import urllib.request
import csv

#asks for twitter user 
while True: 
  try:
    t_user = input("Enter the username of the Twitter User you wish to view tweets of.\n (MUST BE A VALID TWITTER USER)\n");
    theurl = 'https://twitter.com/' + t_user
    source = urllib.request.urlopen(theurl)
  except:
    print("\nPlease enter a valid Twitter username.\n______________________________________\n")
    continue
  else:
    break

soup = BeautifulSoup(source, 'html.parser')

name = soup.title.text 

#takes in number of tweets you want it to output
while True:
  try:
    numb = int(input("How many tweets do you want to print?\n")) #takes in number of tweets to be printed
  except:
    print("\nPlease enter a valid number only.\n_________________________________\n")
  else:
    break

i = 1
substring = "These Tweets are protected"
print(str(numb) + " MOST RECENT TWEETS AND RETWEETS OF\n" + name + "\n")

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
