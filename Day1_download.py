# first do the following: pip install requests
import requests
txt_url = 'https://adventofcode.com/2018/day/1/input'
r = requests.get(txt_url)
with open ('input_download.txt','wb') as f:
  f.write(r.content)
