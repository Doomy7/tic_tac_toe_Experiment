import manip
import csv
import numpy as np
import pandas as pd
from keras import backend as K
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
pd.options.mode.chained_assignment = None

def getData():
    tic_tac_toe_data = pd.read_csv('tic-tac-toe.data')
    y = tic_tac_toe_data['Class']
    X = tic_tac_toe_data.drop(['Class'], 1)
    return y, X

#data builder
def preprocData(X, y):
    X = manip.Xlencoder(X)
    X = manip.custom_onehot_5moves_restricted(X)
    y = manip.ylencoder(y)
    y = np.ravel(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2)
    return X_train, X_test, y_train, y_test

def save_to_csv(data):
    with open('y_pred.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Id', 'Label'])
        for i in range(data.shape[0]):
            writer.writerow([i, data[i]])


#helper f1 calculation by Keras Backend
def f1(y_true, y_pred):
    def recall(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        return recall
    def precision(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision
    precision = precision(y_true, y_pred)
    recall = recall(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))

#custon data label encoder
def Xlencoder(X):
    for index, row in X.iterrows():
        for square in X.columns:
            if row.loc[square] == 'x':
                row.loc[square] = 0
            elif row.loc[square] == 'o':
                row.loc[square] = 1
            elif row.loc[square] == 'b':
                row.loc[square] = 2
    return X

#label encoder for y
def ylencoder(y):
    le = LabelEncoder()
    le.fit(y)
    y = le.transform(y)
    return y

#one hoting each vector with only the first 5 legal moves.  Blanks dont count as legal move
def custom_onehot_5moves_restricted(dataframe):
    dataframe_onehotted = []
    for index, row in dataframe.iterrows():
        #init a 3 times 9 list. (3 values for each cell in tic-tac-toe ['x', 'o', 'b']
        legal_moves_one_hot = np.zeros(27)
        #indexing every 3 cells
        index = -1
        #counting legal moves
        legal_moves_found = 0
        for item in row:
            index += 1
            #if x [1, 0, 0]
            if item == 0:
                legal_moves_one_hot[index*3] = 1
                legal_moves_found += 1
            #if o [0, 1, 0]
            elif item == 1:
                legal_moves_one_hot[index*3 + 1] = 1
                legal_moves_found += 1
            #if b [0, 0, 1]
            else:
                legal_moves_one_hot[index*3 + 2] = 1
            if legal_moves_found == 5:
                dataframe_onehotted.append(legal_moves_one_hot)
                break
    return np.array(dataframe_onehotted)

