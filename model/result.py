import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,roc_auc_score,roc_curve,classification_report,accuracy_score


df=pd.read_csv(r'C:\Users\Shamali\Desktop\Velocity python 2jan21\Nikita Velocity\FLASK\student\Student.csv')
print(df)

df.info()

df.isnull().sum()

df['total']=df['Maths']+df['Physics']+df['Chemistry']
df['total']

print(df)

df.isnull().sum()

df['total'].max()

df['total'].min()

####################################################################################################

x=df.drop('Result',axis=1)
y=df['Result']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

logistic_model=LogisticRegression()
logistic_model.fit(x_train,y_train)

print(logistic_model.score(x_train,y_train))

y_pred=logistic_model.predict(x_test)
print(y_pred)

print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test,y_pred))

print(accuracy_score(y_test,y_pred))

###################################################################################################

y_pred_prob=logistic_model.predict_proba(x_test)
print(y_pred_prob)

fpr,tpr,threshold=roc_curve(y_test,y_pred_prob[:,1])

print(fpr)

print(tpr)

print(threshold)

print(roc_auc_score(y_test,y_pred_prob[:,1]))

###################################################################################################

plt.plot(fpr,tpr,label='logistic regression')
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.legend(loc='best')

###################################################################################################

############################## SAVE MODEL #########################################################

import pickle

model=[logistic_model]

pickle.dump(model,open("stud_model.pickle",'wb'))

import json

columns={
    'result_columns':[col.lower() for col in x.columns]
}

with open("stud_columns.json",'w') as f:
    f.write(json.dumps(columns))

