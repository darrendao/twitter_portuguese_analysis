from twitter import *
import pandas as pd
import codecs
import os
from datetime import datetime
import time

starttime=time.time()

t = Twitter(auth=OAuth(consumer_key, consumer_secret, access_token_key, access_token_secret))

portuguese_dict = ['contador', 'pequena empresa', 'micro empresa', 'financiamento', 'microempreededor', 'empreendedor', 'autonomo', 'senac']

def search_by_term(term):
    return t.search.tweets(q=term, lang='pt', count=100)['statuses']

def write_tweets(dest_file, dictionary=portuguese_dict):
    result = []
    for word in dictionary:
        result += search_by_term(word)
    df = pd.DataFrame(result)
    print 'TOTAL NUMBER OF TWEETS: ', len(df)
    print 'TIME: ', str(datetime.now())
    df.to_csv(dest_file, columns=['text', 'id’, ’created_at’], encoding='utf-8')

while True:
    write_tweets('portuguese_input'+ 'tweets' + str(time.time()) + '.csv')
    time.sleep(900.0 - ((time.time() - starttime) % 900.0))