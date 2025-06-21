from scipy.integrate import quad

def uniform_pdf(x, a, b):    
    return 1 / (b - a) if a <= x <= b else 0

def expectation_variance_library(pdf, a, b):    
    # Calculate expectation E(X)
    expectation, _ = quad(lambda x: x * pdf(x, a, b), a, b)

    # Calculate E(X^2)
    expectation_of_squared, _ = quad(lambda x: (x**2) * pdf(x, a, b), a, b)

    # Calculate variance
    variance = expectation_of_squared - (expectation ** 2)

    return expectation, variance

# Calculate expectation and variance for the uniform distribution
expectation, variance = expectation_variance_library(uniform_pdf, 10, 30)

print()
# Output results
print(f"기대값 Library (평균 기온): {expectation:.2f}")
print(f"분산 Library (기온 변동성): {variance:.2f}")
