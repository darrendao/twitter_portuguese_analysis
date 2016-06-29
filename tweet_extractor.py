from twitter import *
import pandas as pd
import codecs

t = Twitter(auth=OAuth(consumer_key, consumer_secret, access_token_key, access_token_secret))

portuguese_dict = ['contador', 'pequena empresa', 'micro empresa', 'financiamento', 'microempreededor', 'empreendedor', 'autonomo', 'senac']

def search_by_term(term):
    return t.search.tweets(q=term, lang='pt', count=100)['statuses']

def write_tweets(dest_file, dictionary=portuguese_dict):
    result = []
    for word in dictionary:
        result += search_by_term(word)
    df = pd.DataFrame(result)
    df.to_csv(dest_file, columns=['text'], index_label='search_trans_id', encoding='utf-8')
    
write_tweets(open('tweets.csv','w'))