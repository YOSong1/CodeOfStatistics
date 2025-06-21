def joint_pdf(x, y):    
    if 0 <= x <= 10 and 0 <= y <= 20:  
        return (1 / 200) * (1 + 0.05 * y)  
    else:
        return 0

def marginal_pdf_x(joint_pdf, x, y_min, y_max, num_steps=10000000000):
    step = (y_max - y_min) / num_steps
    total = 0
    for i in range(num_steps):
        y = y_min + i * step
        total += joint_pdf(x, y) * step
    return total

# Numerical integration for marginal PDF of Y
def marginal_pdf_y(joint_pdf, y, x_min, x_max, num_steps=100000000000):
    step = (x_max - x_min) / num_steps
    total = 0
    for i in range(num_steps):
        x = x_min + i * step
        total += joint_pdf(x, y) * step
    return total

# Define ranges
x_range = (0, 10)  # Position error range: 0-10 mm
y_range = (0, 20)  # Speed range: 0-20 cm/s

# Example: Calculate marginal PDF values at specific points
x_point = 5  # Example position error
y_point = 10  # Example speed

marginal_x_value = marginal_pdf_x(joint_pdf, x_point, y_range[0], y_range[1])
marginal_y_value = marginal_pdf_y(joint_pdf, y_point, x_range[0], x_range[1])

print()
print(f"Marginal PDF for X at {x_point} mm: {marginal_x_value:.4f}")
print(f"Marginal PDF for Y at {y_point} cm/s: {marginal_y_value:.4f}")
