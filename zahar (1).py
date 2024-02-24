def remove_zeroes(numbers: list[int]) -> int:
    non_zero_count = 0
    index_zero = 0

    for num in numbers:
        if num == 0:
            index_zero = numbers.index(0)
            break

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[non_zero_count], numbers[i] = numbers[i], numbers[non_zero_count]
            non_zero_count += 1

    return non_zero_count


# Тестики
numbers_list = [0, 0, 0, 42, 0, 21, 0, 100, 0, 5, 1, 0]
new_len = remove_zeroes(numbers_list)

print(f"Количество ненулевых элементов: {new_len}")
print(f"Обновленный список: {numbers_list[:new_len]}")

numbers_list = [0, 0, 0, 7, 8, 12, 0, 4, 90]
new_len = remove_zeroes(numbers_list)

print(f"Количество ненулевых элементов: {new_len}")
print(f"Обновленный список: {numbers_list[:new_len]}")

numbers_list = [7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 12, 13, 14, 15, 16, 17, 18, 0, 0]
new_len = remove_zeroes(numbers_list)

print(f"Количество ненулевых элементов: {new_len}")
print(f"Обновленный список: {numbers_list[:new_len]}")

numbers_list = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
new_len = remove_zeroes(numbers_list)

print(f"Количество ненулевых элементов: {new_len}")
print(f"Обновленный список: {numbers_list[:new_len]}")

nums = [0, 42, 21, 0, 100, 0, 5, 1, 0, 7, 3, 0, 404, 0]
new_len = remove_zeroes(nums)

assert new_len == 8
assert nums[:new_len] == [42, 21, 100, 5, 1, 7, 3, 404]

print(new_len)
print(nums[:new_len])
print()

nums = []
new_len = remove_zeroes(nums)

assert new_len == 0
assert nums[:new_len] == []

print(new_len)
print(nums[:new_len])
print()

nums = [0]
new_len = remove_zeroes(nums)

assert new_len == 0
assert nums[:new_len] == []

print(new_len)
print(nums[:new_len])
print()

nums = [00000]
new_len = remove_zeroes(nums)

assert new_len == 0
assert nums[:new_len] == []

print(new_len)
print(nums[:new_len])
print()

nums = [0, 0, 0, 0, 42, 21, 0, 100, 0, 5, 1, 0, 7, 3, 0, 404, 0, 0, 0, 0]
new_len = remove_zeroes(nums)

assert new_len == 8
assert nums[:new_len] == [42, 21, 100, 5, 1, 7, 3, 404]

print(new_len)
print(nums[:new_len])
print()