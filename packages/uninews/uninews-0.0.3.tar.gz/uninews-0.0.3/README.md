# uninews
a universal news feed api for all news provider

## Installation
```
pip install uninews
```

## Supported providers

* [TheNewsApp](https://TheNewsApi.com)
* [NewsCatcherApi](https://newscatcherapi.com)
* [NewsData.io](httsp://newsdata.io)
* [GoogleNews](https://pypi.org/project/pygooglenews)

## Usage
```
from uninews import NewsFeed
from TheNewsApi import set_app_info

set_app_info(appkey=mykey)
nf = NewsFeet('TheNewsApp')
x = nf.news()
print(x)
x = nf.topstorys()
print(x)
x = nf.headline()
print(x)
x = nf.topic('business')
print(x)
```

## Features

NewsFeed provide four type news get methods:
news:
	get news from the specified provider

topic:
	get topiced news from the specified provider

headline:
	get headline news from the specified provider

topstory:
	get top story news from the specified provider

if the method do not provide the method, it will return None

## Return data structure

All the data return by those four method is the same, the top structure
are a dict type with following key:
1. total
	total record returned
2. page
	current page of the data
3. articles
	a array contain all the articles

article is a dict contains following keys:
1. title
	the article's title
2. description
	the summary description
3. content
	the article body
4. link
	the url address to the article
5. img_link
	the article image url address
6. video_link
	the video url address of article
7. publish_date
	the article publish date

## provider

it must implments uninews four same name method



