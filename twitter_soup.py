import bs4
import urllib.request
import requests
import os
import shutil

#checks to see if the folder 'directory' already exists
#if it does it removes the  directory, then create directory named
#the value of directory
directory = "twitter_grab01_olover011"
if os.path.exists(directory):
    shutil.rmtree(directory)
image_folder = os.mkdir(directory)

#grabbing the string form of the html of twitter user for scraping
web = requests.get("http://twitter.com/RealDonaldTrump")
HTML = web.text

#kinda useless
tweet_class = 'css-1dbjc4n r-my5ep6 r-qklmqi r-1adg3ll'
image_class = "css-1dbjc4n r-1niwhzg r-vvn4in r-u6sd8q r-4gszlv r-1p0dtai r-1pi2tsx r-1d2f490 r-u8s1d r-zchlnj r-ipm5af r-13qz1uu r-1wyyakw"

#list to store the list of actual image urls
img_list  = []

#soupify the  HTML string and rip all the img tags out of it
soup = bs4.BeautifulSoup(HTML, 'lxml')
image_list = soup.find_all("img")
imgs = soup.find_all(lambda tag: tag.name == 'alt' and tag.get('alt') == ['Image'])
print(imgs)
input()
#rip the actual image urls from the img tags
for img in image_list:
    try:
        img_list.append(img["src"])
    except KeyError:
        print('no src')
        continue

img_list1 = []
for item in img_list:
    if item not in img_list1:
        img_list1.append(item)
img_list = img_list1

counter = 0
for item in img_list:
    r = requests.get(item)
    with open(directory+"/img"+str(counter)+".png",'wb') as i:
        i.write(r.content)
    counter+=1





