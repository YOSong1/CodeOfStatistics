import numpy as np

def calculate_joint_probability(x_values, y_values, joint_prob_matrix):
        
    joint_prob_matrix = np.array(joint_prob_matrix)

    # Marginal probabilities
    marginal_x = np.sum(joint_prob_matrix, axis=1)  
    marginal_y = np.sum(joint_prob_matrix, axis=0)  

    # Conditional probabilities P(Y|X)
    conditional_y_given_x = joint_prob_matrix / marginal_x[:, None]  

    return marginal_x, marginal_y, conditional_y_given_x

# Example data for discrete variables
x_values = [1, 2, 3]  # Values for X
y_values = ['A', 'B', 'C']  # Values for Y
joint_prob_matrix = [
    [0.1, 0.2, 0.1],  # P(X=1, Y)
    [0.1, 0.2, 0.2],  # P(X=2, Y)
    [0.1, 0.05, 0.05]  # P(X=3, Y)
]

# Calculate probabilities
marginal_x, marginal_y, conditional_y_given_x =\
      calculate_joint_probability(x_values, y_values, joint_prob_matrix)

print()
# Output results
print("Marginal probabilities for X:", marginal_x)
print("Marginal probabilities for Y:", marginal_y)
print("Conditional probabilities P(Y|X):")
print(conditional_y_given_x)
