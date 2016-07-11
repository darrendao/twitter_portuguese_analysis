from twitter import *
import codecs
import os
from datetime import datetime
import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

starttime=time.time()

t = Twitter(auth=OAuth(x,x,x,x))

portuguese_dict = ['contador', 'pequena empresa', 'micro empresa', 'financiamento', 'microempreededor', 'empreendedor', 'autonomo', 'senac']

def search_by_term(term):
    return t.search.tweets(q=term, lang='pt', count=100)['statuses']

def write_tweets(dictionary=portuguese_dict):
    for word in dictionary:
        tweets = search_by_term(word)
        for entry in [tweet['text'] for tweet in tweets]:
            print entry
            producer.send('twitter', entry.encode('utf-8'))
            producer.flush()

while True:
    write_tweets()
    time.sleep(900.0 - ((time.time() - starttime) % 900.0))

