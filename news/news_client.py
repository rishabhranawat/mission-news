import requests
import os
import json

class NewsClient:

	def __init__(self, api_key=None):
		self.BASE_URL="https://newsapi.org/v1/"
		self.API_KEY=api_key

	def get_headlines(self,source=None, sort_by="top"):
		url = self.BASE_URL+"articles?"+"source="+source+"&sortBy="+sort_by+"&apiKey="+self.API_KEY
		response = requests.get(url)
		if(response.status_code == 200):
			return json.loads(response.content)["articles"]
		return []

	def show_sources(self,language="en"):
		url = self.BASE_URL+"sources?language="+language
		response = requests.get(url)
		if(response.status_code == 200):
			return json.loads(response.content)["sources"]
		return []

	def get_titles(self, source=None, sort_by="top"):
		articles = self.get_headlines(source, sort_by)
		titles = []
		for each_article in articles:
			titles.append(each_article["title"])
		return titles