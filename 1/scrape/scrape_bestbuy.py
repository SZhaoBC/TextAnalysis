import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


#my_url = 'https://www.bestbuy.com/site/reviews/zagg-invisibleshield-hd-screen-protector-for-samsung-galaxy-s9-and-s8-clear/5781704'
#opening up the connection grapping the page
#uClient = uReq(my_url)
#page_html = uClient.read()
#uClient.close()

#page_soup = soup(page_html,"html.parser")

#containers = page_soup.findAll("li",{"class":"review-item"})

filename="scape1.csv"
f=open(filename,"w")
header = "reviews\n"
f.write("")
for i in range(1,200):
  my_url = 'https://www.bestbuy.com/site/reviews/zagg-invisibleshield-glass-screen-protector-for-samsung-galaxy-s7/4953402?page='
  #opening up the connection grapping the page
  my_url=my_url+str(i)
  uClient = uReq(my_url)
  page_html = uClient.read()
  

  page_soup = soup(page_html,"html.parser")

  containers = page_soup.findAll("li",{"class":"review-item"})
  for container in containers:
   
    comment = container.find("p",{"class":"pre-white-space"})
    comment_text = comment.text.strip()
    print(str(i))
    f.write(comment_text.replace(",","|").replace(".","|").replace("\n","").replace("\r","")+"\n")

  
uClient.close()
f.close()
