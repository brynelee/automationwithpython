#! /usr/bin/python3

# downloadXkcd.py - downloads every single XKCD comic

import requests, os, bs4

url = 'http://xkcd.com'

# starting url

os.makedirs('xkcd', exist_ok=True)

# store comics in ./xkcd

MaxNumber = 5 # Max Number of images to download
counter = 1

while not url.endswith('#') and counter in range(MaxNumber+1):

    # Download the page.
    print('Downloading page No.%d %s...' %(counter, url))
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    # TODO: Find the URL of the comic image

    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')

    # TODO: Download the image

    print('Downloading image %s...' %(comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()

    # TODO: Save the image to ./xkcd

    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # TODO: Get the Prev button's url.

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

    # count up
    counter += 1

print('Done.')