import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

search_term_input = input('Please enter a search term: ')
search_terms = search_term_input.replace(' ','+')

payload = {'term': search_terms, 'entity':'album'}
url = 'https://itunes.apple.com/search?'
webpage_response = requests.get(url,params=payload).text
response_info = json.loads(webpage_response)

result_count = response_info['resultCount']
print(f'Your search returned {result_count} results.')

search_results = []
for result_info in response_info['results']:
	search_results.append([result_info['collectionName'],[result_info['artistName']],[result_info['trackCount']]])

music_search_df = pd.DataFrame(data=search_results, columns = ['Album','Artist','Track Count'])

for x in range(len(music_search_df)):
	print(f'Artist: {music_search_df.loc[x].at["Artist"][0]} - Album: {music_search_df.loc[x].at["Album"]} - Track Count: {music_search_df.loc[x].at["Track Count"][0]}')