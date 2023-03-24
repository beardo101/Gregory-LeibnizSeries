estimatedPi = 0
a = 1
b = 3

# Number interations
tries = int(input("How many iterations "))

# Loop through iterations
for x in range(tries):
    mid = (4/a - 4/b)
    # Uncomment the line below to show progress each iteration
    #print(f"After {x + 1:,d} interations pi is estimated = {estimatedPi}")
    a += 4
    b += 4
    estimatedPi += mid

# print results
print(f"After {x + 1:,d} interations pi is estimated = {estimatedPi}")
