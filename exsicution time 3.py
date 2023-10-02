import time

def my_function():
    # code to be timed
    sum = 0
    for i in range(100000):
        sum += i
    return sum

start_time = time.time()

result = my_function()

end_time = time.time()

print("Result:", result)
print("Execution time:", end_time - start_time, "seconds")
