from preprocessing import Cleantweet
from flask import jsonify
import pandas as pd
import json
import logging

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import svm

def Process():
    
    # CLEAN DATA (PREPROCESSING)
    dataset = "dataset_tweet_sentimen.csv"
    data = pd.read_csv(dataset)

    # CONCAT DATA CLEAN FROM PREPROSESSING WITH RAW DATA
    data["Cleantweet"] = data["tweet"].apply(Cleantweet)

    # TURN DATA TO JSON
    # dataJson = json.loads(data.to_json(orient="records"))
    

    # SPLITTING X AND Y
    x = data["Cleantweet"]
    y = data["Sentimen"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


    # PERFORM COUNT VECTORIZER
    vectorizer = CountVectorizer()
    vectorizer.fit(x_train) 
    # vectorizer.get_feature_names_out()

    x_train = vectorizer.transform(x_train)
    x_test = vectorizer.transform(x_test)
    
    clf = svm.SVC(kernel='linear') 
    clf.fit(x_train, y_train) 
    y_pred = clf.predict(x_test)

    confusion_matrix(y_test, y_pred)
    y_pred = clf.predict(x_test)

    # print(confusion_matrix)
    result = classification_report(y_test, y_pred)

    return  jsonify ({
        "data":{
            "sentimen": json.loads(data["Sentimen"].to_json(orient="records")),
            "cleantweet": json.loads(data["Cleantweet"].to_json(orient="records")),
            "result": result
        }
    })

