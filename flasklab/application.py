import flask
from flask import Flask

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('https://raw.githubusercontent.com/jfkoehler/toolkit/master/content/data/SMSSpamCollection.txt', sep='\t', header=None)
df.columns = ['target', 'msg']
y = df['target']
X = df['msg']

cvec = TfidfVectorizer(stop_words='english', max_features = 300)
X = cvec.fit_transform(X)
clf = MultinomialNB()
clf.fit(X, y)



app = flask.Flask(__name__)

@app.route('/is_spam', methods=["GET"])
def is_spam():
    msg = pd.Series(flask.request.args['msg'])
    X_new = cvec.transform(msg)
    score = clf.predict(X_new)
    results = {'prediction': score[0]}
    return flask.jsonify(results)


if __name__ == '__main__':
	HOST = '127.0.0.1'
	PORT = '4000'
	app.run(HOST, PORT)