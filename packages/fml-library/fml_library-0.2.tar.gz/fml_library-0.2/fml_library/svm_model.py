import numpy as np

class Support_Vector_Machine:

    def __init__(self, learning_rate=0.001, lambda_param=0.01, no_of_iterations=1000):
        self.learning_rate = learning_rate
        self.lambda_param = lambda_param
        self.no_of_iterations = no_of_iterations
        self.weights = None
        self.bias = None


    def fit(self, X_train, y_train):
        no_of_samples, no_of_features = X_train.shape

        self.weights = np.zeros(no_of_features)
        self.bias = 0

        for itr in range(self.no_of_iterations):
            for i in range(no_of_samples):
                inside_boundary = y_train[i] * (np.dot(X_train[i], self.weights) - self.bias) >= 1
                if inside_boundary:
                    self.weights -= self.learning_rate * (2 * self.lambda_param * self.weights)
                else:
                    self.weights -= self.learning_rate * (2 * self.lambda_param * self.weights - np.dot(X_train[i], y_train[i]))
                    self.bias -= self.learning_rate * y_train[i]
        

    def predict(self, X_test):
        positions = np.dot(X_test, self.weights) - self.bias
        y_predicted = np.sign(positions).astype(int)
        return y_predicted
    

    def accuracy(self, X_test, y_test) :
        y_predicted = self.predict(X_test)
        accuracy = np.sum(y_predicted == y_test) / len(y_test)
        return accuracy


