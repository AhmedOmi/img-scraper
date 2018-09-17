# model scraping for themodelbot

import requests
from bs4 import BeautifulSoup as bs
import os

# website with model images
requiredImage = 'colors'
url = 'https://unsplash.com/search/photos/' + requiredImage
# image file name variable
x = 0

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for model images
if not os.path.exists(requiredImage):
    os.makedirs(requiredImage)

# move to new directory
os.chdir(requiredImage)



# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open(requiredImage + '-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass






