import time

start_time = time.time()

total = 0
for i in range(1, 10000):
    for j in range(1, 10000):
        total += i + j

print(f"The result is {total}")

end_time = time.time()
print(f"It took {end_time-start_time:.2f} seconds to compute")