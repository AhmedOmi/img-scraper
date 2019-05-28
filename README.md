# Image Scraper
A small python image scraper to get images from Unsplash.

## How To Use
0. Clone the repo
1. Install the requirements either by doing `pip install -r requirements.txt`
2. Open up the `get-images.py` in a code editor
3. Change the `Image` var as required
4. Run the `get-images.py` file.


## Requirements
1. Python (any version)
2. Pip

## The Code 

```
# Commented every line, for solid understanding.

# import required modules
import requests # for get requests
from bs4 import BeautifulSoup as bs # for scraping
import os # for creating dirs & writing files,


Image = 'colors' # the required image
url = 'https://unsplash.com/search/photos/' + Image # the unsplash api for searching a required image
x = 0 # set the var x to 0
filePath = 'images/' + Image # file path for the directory

# download page for parsing
page = requests.get(url) # get the url 
soup = bs(page.text, 'html.parser') # parse it with beautifulSoup, imported as bs, store it in soup var

# locate all elements with image tag
image_tags = soup.findAll('img') 

# create directory for required images
if not os.path.exists(filePath): # if the dir doesn't exist
    os.makedirs(filePath) # create the dir

# move to new directory
os.chdir(filePath)

# writing images in the created folder
for image in image_tags: # for each image in the image_tags array,
    try: # go thru this loop
        url = image['src'] # set the url variable to the src of the image tags
        response = requests.get(url) # go to the url and store it in the response var
        if response.status_code == 200: # if the status code === 200
            with open(Image + '-' + str(x) + '.jpg', 'wb') as f: # open the image as the mentioned file format, (w for writing, and b for binary)
                # as the format is jpg, it needs to be saved as a binary file
                # here "f" is just a variable assignment
                f.write(requests.get(url).content) # get the content of the url and write/save in the created dir
                f.close() # stop writing/saving the image
                x += 1 # increment x by 1
    except: # on excpetion (i.e, status code !== 200, or other errors)
        pass # repeat the loop again
```

