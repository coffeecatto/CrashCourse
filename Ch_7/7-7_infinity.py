# 7-7 Infinity
# Write a loop that never ends, then use CTR+C to stop it manually. 
number = 1

while True:
    number += 1
    print(number)

# The above ramps up VSCodium's CPU usage up to 50%. Oops. 