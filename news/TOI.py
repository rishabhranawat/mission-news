import os

from news_client import NewsClient

nc = NewsClient(api_key=os.environ.get("NEWS_API_KEY"))
print(nc.get_titles(source="the-times-of-india"))