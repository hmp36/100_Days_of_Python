import numpy as np

# Define choices and criteria
choices = ["Option A", "Option B", "Option C"]
criteria = ["Cost", "Efficiency", "Flexibility"]
weights = np.array([0.4, 0.3, 0.3])  # Adjust based on importance

# Sample scores for each choice (rows) across criteria (columns)
scores = np.array([
    [8, 7, 6],  # Option A
    [6, 9, 7],  # Option B
    [7, 8, 8]   # Option C
])

# Calculate weighted scores
weighted_scores = scores * weights
total_scores = np.sum(weighted_scores, axis=1)

# Display results
best_option = choices[np.argmax(total_scores)]
for i, choice in enumerate(choices):
    print(f"{choice}: {total_scores[i]:.2f}")

print(f"Best choice based on weighted criteria: {best_option}")
