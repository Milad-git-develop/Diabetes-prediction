import numpy
import pandas
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

data_frame = pandas.read_csv("diabetes2.csv")
print(data_frame.head(10))
print("")
print(data_frame.describe())


x = data_frame.drop("Outcome",axis=1)
y = data_frame.Outcome

X_train,X_test,y_train,y_test = train_test_split(x,y, test_size=0.2)


#desiagn our model
model = Sequential()
model.add(Dense(12,input_dim=8,activation="relu"))
model.add(Dense(8,activation="relu"))
model.add(Dense(1,activation="sigmoid"))

#compile our model
model.compile(loss="binary_crossentropy",optimizer="adam",metrics=["accuracy"])


#fit our model
model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=200,batch_size=10)
print("")
print("")
#calculate the score of model
scores = model.evaluate(X_train, y_train)
print("Training Accuracy: %.2f%%\n" % (scores[1]*100))
print("")
scores = model.evaluate(X_test, y_test)
print("Testing Accuracy: %.2f%%\n" % (scores[1]*100))
print("")
test = numpy.array([[0, 200, 200, 1, 300, 35, 0.2, 19]])
out_test = model.predict(test)
print("out_test: ",out_test)