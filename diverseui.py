from lxml import html
import requests

url_list = []
i = 1

while len(url_list) < 10:

	url = 'https://d3iw72m71ie81c.cloudfront.net/female-{0}.jpg'.format(i)
	page = requests.get(url)
	tree = html.fromstring(page.content)	
	test = tree.xpath('//p')
	if len(test) > 0:
		url_list.append(url)
	i = i + 1

for url in url_list:
	print(url)