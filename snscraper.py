
import snscrape.modules.twitter as sntwitter


scraper = sntwitter.TwitterSearchScraper('#python')

for i, tweet in scraper.get_items():
    if i>10:
        break
    print(tweet)
    print('========')