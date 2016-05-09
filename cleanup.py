import csv
import string

from nltk.corpus import stopwords

tweets = []

with open('dataset.csv', 'rb') as data_file:
    csv_data = csv.reader(data_file)
    for row in csv_data:
        tweets.append(row[3])


def to_lowercase(text):
    return text.lower()


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

def remake_tweet(words):
    return ' '.join(words)


if __name__ == '__main__':
    s = "downloading apps for my iphone! So much fun :-) There literally is an app for just about anything."

    for s in tweets:

        s = to_lowercase(s)
        words = break_into_words(s)
        words = remove_urls(words)
        words = remove_mentions(words)
        words = remove_punctuation(words)
        fresh_words = []
        for word in words:
            new_word_list = break_into_words(word)
            fresh_words += new_word_list

        words = remove_stop_words(fresh_words)
        words = remove_whitespace(words)

        tweet = remake_tweet(words)
        print tweet