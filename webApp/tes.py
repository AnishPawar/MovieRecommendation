import io
from urllib.request import urlopen
import PIL
from scraper_api import ScraperAPIClient
from bs4 import BeautifulSoup
import PIL.Image


client = ScraperAPIClient("c58b550c9190a292b02ba2010be0ca25")
data = client.get('https://www.imdb.com/title/tt2250912/').text

s_data = BeautifulSoup(data,'html.parser')
imdb_dp = s_data.find('meta',property="og:image")

moviePosterLink = imdb_dp.attrs['content']
u= urlopen(moviePosterLink)
rawdata = u.read()

image = PIL.Image.open(io.BytesIO(rawdata))
image.save('1.png')