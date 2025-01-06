first_list = []
second_list = []
while True:
    try:
        numbers = [int(x) for x in input().split()]
        first_list.append(numbers[0])
        second_list.append(numbers[1])
    except EOFError:
        break
first_list.sort()
second_list.sort()

similarity = 0
occurrences = {}
for num in second_list:
    if num in occurrences:
        occurrences[num] += 1
    else:
        occurrences[num] = 1
for num in first_list:
    if num in occurrences:
        similarity += num * occurrences[num]
print(similarity)