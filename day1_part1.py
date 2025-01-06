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

distance = 0
for i, first in enumerate(first_list):
    distance += abs(first - second_list[i])
print(distance)