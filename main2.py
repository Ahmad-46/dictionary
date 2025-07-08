# Sample dictionary
test_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 10,
    'f': 40
}

# Value to find frequency of
value_to_check = 10

# Count frequency of the value
frequency = list(test_dict.values()).count(value_to_check)

# Display result
print(f"The frequency of value {value_to_check} is: {frequency}")
