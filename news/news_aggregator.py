import os
import json

from news_client import NewsClient

class NewsAggregator:

	def __init__(self):
		self.nc = NewsClient(api_key=os.environ.get("NEWS_API_KEY"))

	def get_all_titles(self,sources):
		titles = {}
		for source in sources:
			titles[source] = self.nc.get_titles(source=source)
		return titles

