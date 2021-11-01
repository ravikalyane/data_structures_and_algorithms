# Bubble Sort
import time

elements = [6, 5, 3, 2, 7, 9, 1, 4]
count = 0
print("Original List", elements)
start = time.time()
for p in range(len(elements) - 1):
    print(p, elements)
    count = count + 1
    for i in range(len(elements) - 1):
        if elements[i] > elements[i + 1]:
            temp = elements[i]
            elements[i] = elements[i + 1]
            elements[i + 1] = temp
end = time.time()
time_taken = end - start

print(f'Sorted list - {elements}')
print(f'Iterations - {count}')
print(f'Time - {time_taken * 1000} ms')
