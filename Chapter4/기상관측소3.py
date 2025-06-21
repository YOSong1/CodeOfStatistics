def uniform_pdf(x, a, b):
    
    return 1 / (b - a) if a <= x <= b else 0

def calculate_continuous_expectation_variance(pdf, a, b, num_steps=10000):
    
    step = (b - a) / num_steps  # Width of each step
    expectation = 0
    expectation_of_squared = 0

    for i in range(num_steps):
        x = a + i * step  # Current x value
        weight = pdf(x, a, b) * step  # Approximation of the area for this step
        expectation += x * weight
        expectation_of_squared += (x ** 2) * weight

    variance = expectation_of_squared - (expectation ** 2)
    return expectation, variance

# Calculate expectation and variance for the uniform distribution
expectation, variance = calculate_continuous_expectation_variance(uniform_pdf, 10, 30)

print()
# Output results
print(f"기대값 (평균 기온): {expectation:.2f}")
print(f"분산 (기온 변동성): {variance:.2f}")