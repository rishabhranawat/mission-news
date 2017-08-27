import requests
import os

url = "https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey="+os.environ.get("TOIAPI")
content = requests.get(url).content

import json
content = json.loads(content)

articles = content["articles"]
for each in articles:
	print(each["title"])