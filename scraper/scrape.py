import requests
from bs4 import BeautifulSoup
import pprint



res = requests.get('https://news.ycombinator.com/news')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body.contents)
# print(soup.find_all(div))
# print(soup.find_all('a'))
# print(soup.a)
# print(soup.find_('a')) # finds first

# print(soup.select('.score')) #   css selectors
# print(soup.select('.storylink')[0]) #   css selectors

links = soup.select('.storylink') #   css selectors
votes = soup.select('.score') #   css selectors
subtext = soup.select('.subtext') #   css selectors

print(votes[0])

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, votes):
	hn = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
			# print(points)
			# print(vote)

				hn.append({'title': title, 'link': href, 'votes': points})
	return sort_stories_by_votes(hn)

print(create_custom_hn(links, votes))
pprint.pprint(create_custom_hn(links, subtext))