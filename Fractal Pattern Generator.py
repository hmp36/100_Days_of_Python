import matplotlib.pyplot as plt
import numpy as np

def draw_fractal(x, y, angle, depth):
    if depth == 0:
        return

    # Define branch length
    length = depth * 1.5
    x_new = x + length * np.cos(np.radians(angle))
    y_new = y + length * np.sin(np.radians(angle))

    # Draw the branch
    plt.plot([x, x_new], [y, y_new], 'brown', lw=depth)

    # Recursive calls for smaller branches
    draw_fractal(x_new, y_new, angle - 30, depth - 1)
    draw_fractal(x_new, y_new, angle + 30, depth - 1)

# Initialize plot
plt.figure(figsize=(6, 6))
plt.axis('off')

# Start the fractal recursion
draw_fractal(0, -5, 90, 6)

plt.show()
