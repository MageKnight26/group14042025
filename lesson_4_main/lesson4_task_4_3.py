import random

# generate a random number of elements from 3 to 10
length = random.randint(3, 10)
main_list = [random.randint(0, 100) for _ in range(length)]
# creating a list taking into account the technical task, taking the first, third and penultimate element from the generated list by index
second_list = [main_list[0], main_list[2], main_list[-2]]

print(f"Генерація основного списку: {main_list}")
print(
    f"Новий список після обробки з першим, третім і передостаннім елементом: {second_list}"
)
