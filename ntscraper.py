from ntscraper import Nitter

scraper = Nitter()

handle = "elonmusk"

tweets = scraper.get_tweets(f'{handle}', mode='user', number=5)

for tweet in tweets['tweets']:
    print (tweet['text'])
    print('===============')

file = open(f'{handle}-tweets.txt', 'w')

for tweet in tweets['tweets']:
    file.write(tweet['text']+'\n')
    file.write('===============\n')

file.close()

