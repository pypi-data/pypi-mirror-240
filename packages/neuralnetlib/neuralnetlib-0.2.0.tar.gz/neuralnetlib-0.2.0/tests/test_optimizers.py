import unittest
import numpy as np
from neuralnetlib.optimizers import SGD, Momentum, RMSprop, Adam

class TestOptimizers(unittest.TestCase):

    def setUp(self):
        self.weights = np.array([[0.1, -0.2], [0.4, 0.5]])
        self.bias = np.array([0.1, -0.3])
        self.weights_grad = np.array([[0.01, -0.02], [0.04, 0.05]])
        self.bias_grad = np.array([0.01, -0.03])

    def test_sgd(self):
        sgd = SGD(learning_rate=0.01)
        initial_weights = self.weights.copy()
        initial_bias = self.bias.copy()
        sgd.update(0, self.weights, self.weights_grad, self.bias, self.bias_grad)
        np.testing.assert_array_almost_equal(self.weights, initial_weights - 0.01 * self.weights_grad)
        np.testing.assert_array_almost_equal(self.bias, initial_bias - 0.01 * self.bias_grad)

    def test_momentum(self):
        momentum = Momentum(learning_rate=0.01, momentum=0.9)
        initial_weights = self.weights.copy()
        initial_bias = self.bias.copy()
        momentum.update(0, self.weights, self.weights_grad, self.bias, self.bias_grad)
        np.testing.assert_array_almost_equal(self.weights, initial_weights - 0.01 * self.weights_grad)
        np.testing.assert_array_almost_equal(self.bias, initial_bias - 0.01 * self.bias_grad)

    def test_adam(self):
        adam = Adam(learning_rate=0.01, beta_1=0.9, beta_2=0.999)
        initial_weights = self.weights.copy()
        initial_bias = self.bias.copy()
        adam.update(0, self.weights, self.weights_grad, self.bias, self.bias_grad)
        np.testing.assert_array_almost_equal(self.weights, initial_weights - 0.01 * self.weights_grad)
        np.testing.assert_array_almost_equal(self.bias, initial_bias - 0.01 * self.bias_grad)

    def test_rmsprop(self):
        rmsprop = RMSprop(learning_rate=0.01, rho=0.9)
        initial_weights = self.weights.copy()
        initial_bias = self.bias.copy()
        rmsprop.update(0, self.weights, self.weights_grad, self.bias, self.bias_grad)
        np.testing.assert_array_almost_equal(self.weights, initial_weights - 0.01 * self.weights_grad)
        np.testing.assert_array_almost_equal(self.bias, initial_bias - 0.01 * self.bias_grad)
        
if __name__ == '__main__':
    unittest.main()
