# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:50:43 2019

@author: Kundan Jha
"""
from Review_it_ui import *
from PyQt5.QtWidgets import QDialog, QApplication
import pickle
import sys

#imports for machine Learning
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
#from sklearn.feature_extraction.text import CountVectorizer


Loaded_model=pickle.load(open("Regression_model.sav","rb"))
transformer_model=pickle.load(open("transformer_model.sav","rb"))

class myApp(QDialog):
    corpus=[]
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.Button.clicked.connect(self.predict)
    
    def predict(self):
        self.review=self.ui.Review.toPlainText()
        self.ps = PorterStemmer()
        self.review = re.sub('[^a-zA-Z]', ' ', self.review)
        self.review = self.review.split()
        self.review = [self.ps.stem(w) for w in self.review if not w in set(stopwords.words('english'))]
        self.review = ' '.join(self.review)
        print(self.review)
        self.corpus.clear()
        self.corpus.append(self.review)
        self.X = transformer_model.transform(self.corpus).toarray()
        self.y_pred = Loaded_model.predict(self.X)
        if self.y_pred[0]==0:
            self.ui.Prediction.setText("Bad")
        if self.y_pred[0]==1:
            self.ui.Prediction.setText("Good")
        
        
        
if __name__ =="__main__":
    app = QApplication(sys.argv)
    #print(app)
    #Dialog = QtWidgets.QDialog()
    #ui = Ui_Dialog()
    #ui.setupUi(Dialog)
    s=myApp()
    s.show()
    sys.exit(app.exec_())
    
