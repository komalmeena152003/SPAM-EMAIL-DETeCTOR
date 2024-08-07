import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
tfidf_vectorizer = TfidfVectorizer(lowercase=True)
#not_spam=ham
df=pd.read_csv(r'C:\Users\Komal Meena\Downloads\mail_data.csv')
print(df)
print('********************************************')
data=df.where((pd.notnull(df)), '')
data.head(10)
data.info()
data.shape
data.loc[data['Category'] == 'spam', 'Category'] = 0
data.loc[data['Category'] == 'ham', 'Category'] = 1
X= data['Message']
Y=data['Category']
print('***************************************')

print(X)

print('*********************************************')
print(Y)
X_train, X_test , Y_train, Y_test= train_test_split(X,Y,test_size=0.2, random_state=3)
print('**************************************')

print(X.shape)
print(X_train.shape)
print(X_test.shape)
print('*************************************')

print(Y.shape)
print(Y_train.shape)
print(Y_test.shape)
feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_train_features= feature_extraction.fit_transform(X_train)
X_test_features= feature_extraction.transform(X_test)

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')
print('*************************************')
print(X_train)
print('*************************************')
print(X_train_features)
model = LogisticRegression()
model.fit(X_train_features, Y_train)
prediction_on_traning_data =model.predict(X_train_features)
accuracy_on_training_data= accuracy_score(Y_train , prediction_on_traning_data)
print('*************************************')
print('Acc on training data : ', accuracy_on_training_data)
prediction_on_test_data= model.predict(X_test_features)
accuracy_on_test_data= accuracy_score(Y_test, prediction_on_test_data)
print('*************************************')
print('Acc on test data :' , accuracy_on_test_data)

input_your_mail = ["Congratulations! You've been selected to receive a FREE [insert product name]! Click below to claim your prize now!"]
input_data_features= feature_extraction.transform(input_your_mail)
prediction=model.predict(input_data_features)
print('*************************************')
print(prediction)
if(prediction[0]==1):
    print('Ham mail')

else:
    print('Spam mail')    