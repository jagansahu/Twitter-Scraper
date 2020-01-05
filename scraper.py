from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'html5lib')

article = soup.find('article')

for article in soup.find_all('article'):
  header = article.header.h2.a.text
  print(header)

  summary = article.find('div', class_= 'entry-content').p.text
  print(summary)

  try:
  	vid_src = article.find('iframe')['src']
  	vid_id = vid_src.split('/')[4]
  	yt_link = f'https://youtube.com/watch?v={vid_id}'
  except Exception as e:
  	yt_link = None

  print(yt_link)

  print()
 
