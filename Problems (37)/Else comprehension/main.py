# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]

binary_list = [0 if x <= 0 else 1 for x in old_list]
print(binary_list)