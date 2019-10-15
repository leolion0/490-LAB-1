import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import svm, neighbors

#https://stackoverflow.com/a/38105540



# save load_iris() sklearn dataset to iris
# if you'd like to check dataset type use: type(load_iris())
# if you'd like to view list of attributes use: dir(load_iris())
iris = load_iris()

# np.c_ is the numpy concatenate function
# which is used to concat iris['data'] and iris['target'] arrays
# for pandas column argument: concat iris['feature_names'] list
# and string list (in this case one string); you can make this anything you'd like..
# the original dataset would probably call this ['Species']
data1 = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                     columns=iris['feature_names'] + ['target'])

X = data1.drop(columns=['target'])
y = data1[['target']]

# print(data1.isnull().sum())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

gauss = GaussianNB()
gauss.fit(X_train, y_train.values.ravel())
y_pred = dict()
y_pred['gauss'] = gauss.predict(X_test)
# print(y_pred)

svmModel = svm.SVC(gamma='scale')
svmModel.fit(X_train, y_train.values.ravel())
y_pred['svmModel'] = svmModel.predict(X_test)

k = 15
knn = neighbors.KNeighborsClassifier(k, weights='uniform')
knn.fit(X_train, y_train.values.ravel())
y_pred['knn'] = knn.predict(X_test)




for k, v in y_pred.items():
    print(k + ": " + str(f1_score(y_test, v, average='weighted')))

# export_csv = data1.to_csv (r'C:\Users\Leo\Desktop\export_dataframe.csv', index = None, header=True)
