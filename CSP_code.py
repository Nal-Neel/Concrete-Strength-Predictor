import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

data = pd.read_csv('concrete.csv')
data = np.array(data)

X = data[1:, 0:-1]
y = data[1:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
randomforest_reg = RandomForestRegressor()
randomforest_reg.fit(X_train, y_train)

pickle.dump(randomforest_reg, open('model.pkl','wb'))
