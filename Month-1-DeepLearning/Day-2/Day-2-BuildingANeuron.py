import numpy as np
# import matplotlib.pyplot as plt

# inputs = np.array([2,4,6])

# weights = np.array([0.5,0.9,0.1])

# bias = 7

# x = np.dot(inputs,weights)+bias

# print(x)

# def step(x):
#     return 1 if x >= 0 else 0

# def sigmoid(x):
#     return 1/(1+np.exp(-x))

# def relu(x):
#     return np.maximum(0,x)

# print(step(x))
# print(sigmoid(x))
# print(relu(x))

# # 2. Generate data
# x = np.linspace(-10, 10, 100)
# y = relu(x)

# # 3. Create the plot using the OO-style
# fig, ax = plt.subplots(figsize=(6, 4), layout='constrained')

# ax.plot(x, y, label=r'$\sigma(x) = \frac{1}{1 + e^{-x}}$', color='blue', linewidth=2)

# # 4. Add labels, title, and styling
# ax.set_title("Sigmoid Function")
# ax.set_xlabel("x")
# ax.set_ylabel("$\sigma(x)$")
# ax.axhline(0.5, color='gray', linestyle='--', linewidth=0.8) # Reference line
# ax.grid(True, linestyle=':', alpha=0.6)
# ax.legend()

# plt.show()


class Neuron:

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def sigmoid(self, x):
        return 1/(1+ np. exp(-x))
        

    def relu(self, x):
        return np.maximum(0,x)

    def step(self, x):
        return 1 if x>=0 else 0

    def forward(self, inputs):
        weighted_sum = np.dot(inputs, self.weights)
        weighted_sum += self.bias
        sigmoid_output = self.sigmoid(weighted_sum)
        print(sigmoid_output)
        step_output = self.step(weighted_sum)
        print(step_output)
        relu_output = self.relu(weighted_sum)
        print(relu_output)
n = Neuron([0.5, 0.77], 0.21)
print(n.forward([1, 2]))