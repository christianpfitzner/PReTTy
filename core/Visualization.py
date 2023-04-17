import matplotlib.pyplot as plt
import numpy as np

class Visualization:
    def __init__(self, data):
        self.data = data

    def plot(self):
        plt.plot(self.data)
        plt.show()




data = np.random.randn(100,2)

print(data)

plt.plot(data)