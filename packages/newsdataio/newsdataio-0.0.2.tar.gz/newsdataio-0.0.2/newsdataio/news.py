import requests
from appPublic.http_client import Http_Client
from appPublic.timeUtils import curDateString
from uninews.baseprovider import BaseProvider
from .version import __version__
app_info = {}

def set_app_info(appkey):
	app_info.update({
		'appkey':appkey
	})

def buildProvider(newsfeed):
	print(f'TheNewsApi version {__version__}')
	return NewsDataIo(newsfeed)

class NewsDataIo(BaseProvider):
	def __init__(self, newsfeed):
		self.newsfeed = newsfeed
		self.appkey = app_info.get('appkey')

	def get_result_mapping(self):
		return {
			'total':'totalResults',
			'articles':'results'
		}
	
	def get_article_mapping(self):
		return {
			'img_link':'image_url',
			'publish_date':'pubDate'
		}
	
	def news(self, q=None, 
						categories=[],
						countries=[], 
						language=[], 
						page=0):
		url = 'https://newsdata.io/api/1/news'
		hc = Http_Client()
		keyword = q
		if keyword == '':
			keyword = None
		categories = None if len(categories) == 0 else categories[0]
		language_str = None if len(language) == 0 else language[0]
		countries_str = None if len(countries) == 0 else countries[0]
		today = curDateString()
		p = {
			'apikey':self.appkey,
			'country':countries_str,
			'categories':categories,
			'language':language_str,
			'page':page,
			'q':keyword
		}
		x = hc.get(url, params=p)
		return x

	def topstory(self, q=None, categories=[],
						countries=[], language=[], page=0):
		url = 'https://newsapi.org/v2/top-headlines'
		hc = Http_Client()
		keyword = q
		if keyword == '':
			keyword = None
		categories = self.newsfeed.array2param(categories)
		language_str = self.newsfeed.array2param(language)
		countries_str = self.newsfeed.array2param(countries)
		today = curDateString()
		p = {
			'apiKey':self.appkey,
			'category':categories, 
			'country':countries_str,
			'pageSize':100,
			'page':page,
			'q':keyword
		}
		print('url=', url, 'params=', p)
		x = hc.get(url, params=p)
		return x

if __name__ == '__main__':
	print('input appkey:')
	appkey=input()
	set_app_info(appkey)
	nc = NewsDataIo()
	while True:
		print('key word to search news, ":quit" to exit')
		x = input()
		if x == ':quit':
			break
		news = nc.getNews(x)
		print(news.keys())
		print(news['results'][0].keys())
