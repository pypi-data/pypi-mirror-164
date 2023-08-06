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
						domains=[],
						language=[], 
						page=0):
		url = 'https://newsdata.io/api/1/news'
		hc = Http_Client()
		keyword = q
		if keyword == '':
			keyword = None
		categories = self.newsfeed.array2params(categories)
		language_str = self.newsfeed.array2params(language)
		countries_str = self.newsfeed.array2params(countries)
		domain_str = self.newsfeed.array2param(domains)
		today = curDateString()
		p = {
			'apikey':self.appkey,
			'country':countries_str,
			'category':categories,
			'domain':domain_str,
			'language':language_str,
			'page':page,
			'q':keyword
		}
		print(url, p)
		x = hc.get(url, params=p)
		return x

	def sources_result_mapping(self):
		return {
			'sources':'results'
		}

	def source_mapping(self):
		return {
			'categories':'category',
			'link':'url',
			'countries':'country'
		}

	def sources(self, countries=[], categories=[], language=[]):
		url = 'https://newsapi.org/v2/sources'
		categories = self.newsfeed.array2param(categories)
		language_str = self.newsfeed.array2param(language)
		countries_str = self.newsfeed.array2param(countries)
		p = {
			'apiKey':self.appkey,
			'category':categories, 
			'country':countries_str,
			'language':language
		}
		hc = Http_Client()
		print('url=', url, 'params=', p)
		x = hc.get(url, params=p)
		return x
		
	def topstory(self, q=None, categories=[],
						countries=[], 
						domains=[],
						language=[], 
						from_date=None,
						to_date=None,
						page=0):
		url = 'https://newsdata.io/api/1/archive'
		keyword = q
		if keyword == '':
			keyword = None
		categories = self.newsfeed.array2param(categories)
		language_str = self.newsfeed.array2param(language)
		countries_str = self.newsfeed.array2param(countries)
		domains_str = self.newsfeed.array2param(domains)
		today = curDateString()
		p = {
			'apikey':self.appkey,
			'category':categories, 
			'country':countries_str,
			'language':language_str,
			'domains':domains_str,
			'from_date':from_date,
			'to_date':to_date,
			'page':page,
			'q':keyword
		}
		print('url=', url, 'params=', p)
		hc = Http_Client()
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
