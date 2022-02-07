# 5-11 Ordinal Numbers

# Store numbers from 1 to 9 in a list.

numbers = range(1,10)

# Print the list with correct ordinal endings (st, nd, rd, th)

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")