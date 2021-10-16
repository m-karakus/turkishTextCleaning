#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importing the libraries 
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import re 
import codecs
import string 
import nltk
# from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
# nltk.download("stopwords")

from TurkishStemmer import TurkishStemmer
stemmer = TurkishStemmer()

import zeyrek
analyzer = zeyrek.MorphAnalyzer()


def main(text):
    # lower
    text = text.lower()

    # remove hyperlinks
    text = re.sub(r"<.*?a>", "", text)

    # remove html
    text = re.sub(r"<[^>]+>", "", text)

    # remove urls
    text = re.sub(r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})", "", text)

    # encoding the text - cleaning the emoji
    # text_encode = text.encode(encoding="utf-8", errors="ignore")
    # text_encode = text.encode(encoding="latin5", errors="ignore")

    # decoding the text
    # text_decode = text_encode.decode("utf-8", errors="replace_with_space")
    # text_decode = text_encode.decode("latin5", errors="replace_with_space")
    # text = text_decode
    
    # Remove ticks and the next character
    text = re.sub(r"\'\w+", "", text)

    # # cleaning the text to remove extra whitespace 
    # text = " ".join([word for word in text_decode.split()])

    # cleaning the text to remove extra whitespace 
    #text = re.sub(r'\s{2,}', " ", text)

    # removing stopwords
    # stop_words = set(stopwords.words("turkish"))
    stop_words = ['acaba', 'ama', 'aslında', 'az', 'bazı', 'belki', 'biri', 'birkaç', 'birşey', 'biz', 'bu', 'çok', 'çünkü', 'da', 'daha', 'de', 'defa', 'diye', 'eğer', 'en', 'gibi', 'hem', 'hep', 'hepsi', 'her', 'hiç', 'için', 'ile', 'ise', 'kez', 'ki', 'kim', 'mı', 'mu', 'mü', 'nasıl', 'ne', 'neden', 'nerde', 'nerede', 'nereye', 'niçin', 'niye', 'o', 'sanki', 'şey', 'siz', 'şu', 'tüm', 've', 'veya', 'ya', 'yani','cok','nun','varmı','bir','ben','kardeş','abla','arkadaş','Selamun','aleyküm','sevmek','demek','iyi']
    # text = " ".join([word for word in text.split() if word not in stop_words])
    # pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('turkish')) + r')\b\s*')
    # text = pattern.sub('', text)

    # # removing mentions 
    # text = re.sub(r"@\S+", "", text)

    # # Remove Hashtags
    # text = re.sub(r"#\S+", "", text)
    
    # remove market tickers
    # text = re.sub(r"\$", "", text)

    # remove punctuation
    # stringPunct= '''!"$%&'()*+,-./:;<=>?[\]^_`{|}~'''
    # text = text.translate(str.maketrans('', '',stringPunct))

    # Remove numbers
    text = re.sub(r'\w*\d+\w*', '', text)

    # Tokenizer
    tt = TweetTokenizer()
    words = tt.tokenize(text)

    hastags = []
    [hastags.append(token) for token in words if token.startswith("#") ]

    mentions = []
    [mentions.append(token) for token in words if token.startswith("@") ]
    
    # print(hastags)
    # print(mentions)

    tokens = []
    tokens = [stemmer.stem(token) for token in words if len(token) >1 ]
    

    # for t in tokens:
    #     if re.match(r"^\#\w+", t):
    #         hastags.append(t)
    #     if re.match(r"^\@\w+", t):
    #         mentions.append(t)
    whitelist = ['omo']
    # for word in words: 
    #     try:
    #         orginal = analyzer.analyze(word)[0][0][0]
    #         lemma = analyzer.analyze(word)[0][0][1]
    #         pos = analyzer.analyze(word)[0][0][2]

    #         if pos == 'Unk'and len(orginal)>2 and lemma not in stop_words and orginal in whitelist:
    #             tokens.append(orginal)
            
    #         # ['Adj', 'Verb', 'Punc', 'Noun', 'Pron', 'Adv', 'Conj', 'Unk', 'Postp', 'Det', 'Num', 'Interj', 'Ques', 'Dup']
    #         elif pos=='Adj' or pos=='Verb' or pos=='Noun' or pos=='Adv' or pos=='Interj':
    #             if len(lemma)>2 and lemma not in stop_words:
    #                 # tokens.append([lemma,pos])
    #                 tokens.append(lemma)
    #     except:
    #         continue
    print(tokens)
    # print(len(tokens))
    return(tokens,hastags,mentions)

if __name__ == '__main__':
    text = '''
algı*, algi*,öfke*, kişisel gelişim*, kurumsal gelişim*, protokol*, meslek*, iletişim*, iletisim*, motivasyon*, cv*
'''
    main(text)
