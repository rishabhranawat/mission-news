import os

from news_client import NewsClient

nc = NewsClient(api_key=os.environ.get("TOIAPI"))
print(nc.get_titles(source="the-times-of-india"))