def calculate_mean(data):    
    return sum(data) / len(data)

def calculate_median(data):    
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:  
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def calculate_mode(data):    
    frequency = {}
    for value in data:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    max_frequency = max(frequency.values())
    modes = [key for key, count in frequency.items() \
        if count == max_frequency]
    return modes



data = [5,2,7,6,4,8,9,1,4,3,6,5,7,9,8,3,4,5,6,6,1]
avg = calculate_mean(data)
med = calculate_median(data)
modes = calculate_mode(data)

print()
print("Statistics Results:")
print(f"Mean: {avg}")
print(f"Median: {med}")
print(f"Mode(s): {modes}")


