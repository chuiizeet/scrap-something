# https://www.facebook.com/1937414583010493/posts/2306382189447062?s=100006769265762&v=e&sfns=mo

import requests
import re
from bs4 import BeautifulSoup
url = "https://www.facebook.com/1937414583010493/posts/2306382189447062?s=100006769265762&v=e&sfns=mo"

r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, 'lxml')

video_url = re.search('sd_src_no_ratelimit:"(.+?)"', soup.text).group(1)
print(video_url)
