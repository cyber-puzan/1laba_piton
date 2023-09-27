num_count = int(input("Введите количество чисел в списке: "))

my_list = []

for i in range(num_count):
    num = int(input("Введите число " + str(i + 1) + ": "))
    my_list.append(num)

product_even_indices = 1
for i in range(0, len(my_list), 2):
    product_even_indices *= my_list[i]

list_length = len(my_list)

print("Произведение элементов с четными индексами:", product_even_indices)
print("Длина списка:", list_length)
