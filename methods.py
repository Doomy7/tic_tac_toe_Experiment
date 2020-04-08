import manip
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn import svm
import keras
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

#neural network test
def Neural(X_train, X_test, y_train):
    y_train = keras.utils.to_categorical(y_train, num_classes=2)
    model = Sequential()
    model.add(Dense(32, activation='relu', input_dim=27))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(2, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=[manip.f1, 'accuracy'])
    model.fit(X_train, y_train, epochs=50, batch_size=4, verbose=2)
    return model.predict_classes(X_test)

#simple svm test
def SupVecMac(X_train, X_test, y_train):
    SVM = svm.SVC(C=10)
    SVM.fit(X_train, y_train)
    return SVM.predict(X_test)

#metrics
def metrics(y_test, y_pred):
    print('Accuracy:', accuracy_score(y_test, y_pred))
    print('Precision:', precision_score(y_test, y_pred))
    print('Recall:', recall_score(y_test, y_pred))
    print('F1:', f1_score(y_test, y_pred, average='micro'))
