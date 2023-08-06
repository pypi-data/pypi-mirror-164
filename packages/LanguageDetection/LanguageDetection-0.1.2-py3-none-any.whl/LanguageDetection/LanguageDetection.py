# -*- coding: utf-8 -*-
"""Language-detection1.ipynb
This program detects Language from text. Its uses MultinomialNB model to detect/predict the language. It also uses Dataset which helps in detecting the language.

Original file is located at
    https://colab.research.google.com/drive/1TJtP0ZDUo7YZqdEsNpQIFXGeS89HiQ0F

Language Detection made by Mayuresh Choudhary
"""
from importlib import resources
import io
from sklearn.naive_bayes import MultinomialNB
from csv import writer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd

class LanguageDetection:
  #df=pd.read_csv("\\LanguageDetection\\LanguageDetection\\LanguageDetection.csv")
  def __init__(self):
    self.file1="LanguageDetection.csv"
    with resources.open_binary('LanguageDetection', self.file1) as fp:
      self.df=fp.read()
    self.df=pd.read_csv(io.BytesIO(self.df))
    # # df["Language"].value_counts()
    #df

    self.Xfeature=self.df["Text"]
    self.ylable=self.df["Language"]

    self.cv=CountVectorizer()
    self.X=self.cv.fit_transform(self.Xfeature)
    self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X,self.ylable)

    self.nv_model = MultinomialNB()
    self.nv_model.fit(self.X_train,self.y_train)
    self.predict=self.nv_model.predict(self.X_test)

  def LanguageDetect(self,text):
    # text=input("Enter text: ")
    self.text=[text]
    self.vect=self.cv.transform(self.text)
    self.prediction=self.nv_model.predict(self.vect)
    self.res=self.prediction[0]
    # print("Language: ",self.res)
    return self.res

  def __str__(self):
    return f"""
    LanguageDetection Program detects the Language of the Text. Its uses MultinomialNB to predict the Language. It also uses the dataset which helps in predicting the Language, currently program only support Language Detection from Text.

    Original file is located at:
    https://colab.research.google.com/drive/1TJtP0ZDUo7YZqdEsNpQIFXGeS89HiQ0F

    Syntaxt:
      '''from LanguageDetection import LanguageDetection

      lg = LanguageDetection()
      prediction = lg.LanguageDetect("PASS THE TEXT")
      print(prediction)'''

      with just three lines of code you can start detecting the Language from text.
    
    Language Detection made by Mayuresh Choudhary
    """