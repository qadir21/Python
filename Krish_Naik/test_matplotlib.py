import matplotlib.pyplot as plt
import numpy as np

# Simple test plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('Test Matplotlib Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.savefig('test_plot.png')
print("Matplotlib imported and plot created successfully!")
print("Plot saved as test_plot.png")
