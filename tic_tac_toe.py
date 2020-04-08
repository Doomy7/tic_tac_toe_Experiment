import manip
import methods

#get init data
y, X = manip.getData()
#preprocessing
X_train, X_test, y_train, y_test = manip.preprocData(X, y)
#execute methods
y_pred_nn = methods.Neural(X_train, X_test, y_train)
y_pred_svm = methods.SupVecMac(X_train, X_test, y_train)

print('Neural Network: =========')
methods.metrics(y_test, y_pred_nn)
manip.save_to_csv(y_pred_nn)
print('Support Vector Machine: =========')
methods.metrics(y_test, y_pred_svm)

