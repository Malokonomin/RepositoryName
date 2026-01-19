numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing = 4  # Определение индекса элемента, который требуется заменить.

new_list = numbers[:missing] + numbers[missing+1:]
len(new_list)
len(numbers)
average_of_list = sum(new_list)/(len(numbers))
numbers[missing] = average_of_list

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
