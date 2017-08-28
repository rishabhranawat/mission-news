import json
from news_aggregator import NewsAggregator

s = []
with open("temp_sources.json", "r") as f:
	s = json.load(f)

na = NewsAggregator()
titles = na.get_all_titles(s)
message = ""
for key, value in titles.items():
	message += key+":"+"\n"+"\t"
	for i in range(0, len(value), 1):
		v = value[i]
		if(i < len(value)-1):
			message +=v+"\n \t"
		else:
			message += v+"\n"
