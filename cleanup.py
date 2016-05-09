import csv
import string

import HTMLParser

from nltk.corpus import stopwords

tweets = []

with open('dataset.csv', 'rb') as data_file:
    csv_data = csv.reader(data_file)
    for row in csv_data:
        tweets.append(row[3])


def to_lowercase(text):
    return text.lower()


def unescape_html(text):
    html_parser = HTMLParser.HTMLParser()
    return html_parser.unescape(text)


def break_into_words(tweet):
    """
    Break the tweet into words
    :return:
    """
    tweet_words = tweet.split()
    return tweet_words


def remove_urls(words):
    """
    removes url's from a list of words
    :return:
    """

    ## www or http

    for word in words:
        if word.startswith('www') or word.startswith('http'):
            words.remove(word)
    return words


def remove_mentions(words):
    """
    remove @mentions from the list of words
    :return:
    """

    for word in words:
        if word.startswith("@"):
            words.remove(word)
    return words


def remove_punctuation(words):
    """
    remove punctuatuion from the words
    :return:
    """

    punctuation = list(string.punctuation)

    for count, word in enumerate(words):
        for punc in punctuation:
            if punc in word:
                word = word.replace(punc, " ")
                words[count] = word
    return words


def remove_stop_words(words):
    """
    remove stop words from a list of words
    :return:
    """

    stop_words = stopwords.words('english')

    for word in stop_words:
        if word in words:
            words.remove(word)

    return words


def remove_whitespace(words):
    """
    remove leading and trailing whitespace in words
    :return:
    """

    for count, word in enumerate(words):
        word = word.strip()
        words[count] = word
    return words


def remove_numbers(words):
    """
    remove any numbers remaining
    :param words:
    :return:
    """
    digits = []
    for word in words:
        if word.isdigit():
            digits.append(word)

    return [x for x in words if x not in digits]


def remake_tweet(words):
    return ' '.join(words)


def to_ascii(text):
    """
    downgrade text from utf-8 to ascii
    :param text:
    :return:
    """
    return text.decode('utf8').encode('ascii', 'ignore')


if __name__ == '__main__':
    s = "downloading apps for my iphone! So much fun :-) There literally is an app for just about anything."

    for text in tweets:

        text = to_lowercase(text)
        text = to_ascii(text)
        text = unescape_html(text)
        words = break_into_words(text)
        words = remove_urls(words)
        words = remove_mentions(words)
        words = remove_punctuation(words)
        fresh_words = []
        for word in words:
            new_word_list = break_into_words(word)
            fresh_words += new_word_list

        words = remove_stop_words(fresh_words)
        words = remove_whitespace(words)
        words = remove_numbers(words)

        tweet = remake_tweet(words)
        print tweet
