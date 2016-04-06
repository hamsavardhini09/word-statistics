# -*- coding: UTF-8 -*-

import flask;
import json;
import string;
import operator;
from collections import OrderedDict;

text = "Welcome to to to the online text analysis tool, the  refer detailed statistics of your text, perfect for translators " \
       "(quoting), for webmasters (ranking) or for normal users, to know the subject of a text. Now with new features " \
       "as the analysis of words groups, solos finding out the keyword density, analyse the prominence of word or " \
       "expressions. Webmasters can analyse the links on their pages. More instructions are about to be written, " \
       "please civic send us your feedback !";

clean_text = ''
for x in text:
    if x not in string.punctuation:
        clean_text += x

#test

app = flask.Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to p1 Docker project!<br>Add below keys at the end of url to see statistics<br>wordstatistics"

@app.route('/wordstatistics', methods=['GET', 'POST'])
def wordstatistics1():
    #curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
    if flask.request.method == 'POST':
        print "test"
        fp = flask.request.files['the_file']
        print "test"
        #print fp.read()
        abc = fp.read()
        print abc
        fp.close()
        res_word = word_wc(abc)
        return res_word
    else:
        res_word = word_wc(text)
        return res_word


def word_wc(given_text):
    words = given_text.split();
    unique_words = list(set([word for word in words if words.count(word) == 1]))
    dupes = list(set([word for word in words if words.count(word) > 1]))

    word_dict = dict()
    word_dict['text'] = given_text
    word_dict['word_count'] = len(words)
    word_dict['words'] = words
    word_dict['unique_words'] = unique_words
    word_dict['unique_word_count'] = len(unique_words)
    word_dict['duplicate_words_list'] = dupes
    word_dict['duplicate_word_count'] = len(dupes)

    wordfreq_unfiltered = dict()
    for rawWord in clean_text.lower().split():
        if rawWord not in wordfreq_unfiltered.keys():
            wordfreq_unfiltered[rawWord] = 0
        wordfreq_unfiltered[rawWord] += 1

    wordfreq_unfiltered = sorted(wordfreq_unfiltered.items(), key=operator.itemgetter(1), reverse =True)[:10]
    order_wordfreq = OrderedDict();

    for item in wordfreq_unfiltered:
        order_wordfreq[item[0]] = item[1]

    word_dict['top10_word_freq'] = order_wordfreq

    stoppers = ["the","for","of","to","or","are","be","as", "a", "i", "u", ]

    tempText_filtered = clean_text.lower().split()
    for x in stoppers:
        tempText_filtered = list(filter((x).__ne__,tempText_filtered))

    wordfreq_filtered = dict()
    for rawWord in tempText_filtered:
        if rawWord not in wordfreq_filtered.keys():
            wordfreq_filtered[rawWord] = 0
        wordfreq_filtered[rawWord] += 1

    wordfreq_filtered = sorted(wordfreq_filtered.items(), key=operator.itemgetter(1), reverse =True)[:10]
    order_wordfreq = OrderedDict();

    for item in wordfreq_filtered:
        order_wordfreq[item[0]] = item[1]

    word_dict['word_freq_no_stop_words'] = order_wordfreq

    vowels = ['a','e','o','i','u']

    def hasvowel(word):
        a = 0
        for vowel in vowels:
            if vowel in word:
                a = 1
        if a > 0:
            return True
        else:
            return False

    count_vowel =0
    for word in words:
        if hasvowel(word):
            count_vowel += 1
    word_dict['words_with_vowels'] = count_vowel
    word_dict['Words_with_consonats'] = len(words) - count_vowel

    count_beg =0
    for word in words:
        if word[0].lower() in'aeiou':
            count_beg +=1
    word_dict['words_beginwith_vowels'] = count_beg
    word_dict['Words_beginwith_consonats'] = len(words) - count_beg
    return json.dumps(word_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0'); # default http://127.0.0.1:5000 or http://0.0.0.0:5000
    #print cc()