To create a line plot in Matplotlib with two y-axes at different scales, you can use `twinx()` to create a second y-axis
that shares the same x-axis. Here's an example of how to plot two lines with different y-axes on the same plot:

```python
import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)  # First y-axis data (e.g., sine wave)
y2 = np.exp(x / 5)  # Second y-axis data (e.g., exponential growth)

fig, ax1 = plt.subplots()  # Create a figure and axis for the first plot

# Plot the first line on the first y-axis
ax1.plot(x, y1, 'b', label='sin(x)')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('sin(x)', color='b')  # Set y-axis label for the first axis
ax1.tick_params(axis='y', labelcolor='b')

# Create a second y-axis sharing the same x-axis
ax2 = ax1.twinx()
ax2.plot(x, y2, 'r', label='exp(x/5)')
ax2.set_ylabel('exp(x/5)', color='r')  # Set y-axis label for the second axis
ax2.tick_params(axis='y', labelcolor='r')

# Show the plot
plt.title('Line Plot with Two Y-Axes')
plt.show()
```

### Explanation:
- `ax1 = plt.subplots()` creates the main axis for the plot.
- `ax1.twinx()` creates a second y-axis sharing the same x-axis as `ax1`.
- `ax1.plot()` and `ax2.plot()` plot the data on the first and second axes respectively.
- `ax1.set_ylabel()` and `ax2.set_ylabel()` are used to label each y-axis, with different colors to distinguish the axes.
- `tick_params(axis='y', labelcolor='b')` and `tick_params(axis='y', labelcolor='r')` are used to change the color of the tick labels on each y-axis to match the respective line color.

This will create a plot with two y-axes, each with its own scale.
