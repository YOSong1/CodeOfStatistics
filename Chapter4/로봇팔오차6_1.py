from scipy.integrate import dblquad

def joint_pdf(x, y):    
    if 0 <= x <= 10 and 0 <= y <= 20:  
        return (1 / 200) * (1 + 0.05 * y) 
    else:
        return 0

def marginal_pdf_x(joint_pdf, x_range, y_range):
    return lambda x: dblquad(joint_pdf, y_range[0], y_range[1], 
                             lambda _: x, lambda _: x_range[1])[0]

def marginal_pdf_y(joint_pdf, x_range, y_range):
    return lambda y: dblquad(joint_pdf, x_range[0], x_range[1], 
                             lambda _: y, lambda _: y_range[1])[0]

# Define ranges
x_range = (0, 10)  # Position error range: 0-10 mm
y_range = (0, 20)  # Speed range: 0-20 cm/s

# Marginal PDF calculations
marginal_x = marginal_pdf_x(joint_pdf, x_range, y_range)
marginal_y = marginal_pdf_y(joint_pdf, x_range, y_range)

# Example: Calculate marginal PDF values at specific points
x_point = 5  # Example position error
y_point = 10  # Example speed

print()
print(f"Marginal PDF for X at {x_point} mm: {marginal_x(x_point):.4f}")
print(f"Marginal PDF for Y at {y_point} cm/s: {marginal_y(y_point):.4f}")
