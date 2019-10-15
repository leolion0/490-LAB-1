import pandas as pd
from sklearn.datasets import load_linnerud
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import svm, neighbors
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

linnerud = load_linnerud(return_X_y=False)
X = pd.DataFrame(linnerud.data, columns=linnerud.feature_names)
y = pd.DataFrame(linnerud.target, columns=linnerud.target_names)
both = pd.concat([X,y], axis=1, ignore_index=False)

print(both.isna().sum())
print(both)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
reg = LinearRegression()
reg.fit(X_train,y_train)
y_pred = reg.predict(X_test)
print(mean_squared_error(y_test,y_pred))
print(r2_score(y_test,y_pred))