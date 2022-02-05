# 4-5 Summing a million

# Create a list going from 1 to 1 million, then use min() and and max() to check if it is correct. 
# Next, use sum() on the list. 

numbers = [value for value in range(1, 1000001)]
print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")

# NOTE: Counting all these numbers took only about a half of a second O_O