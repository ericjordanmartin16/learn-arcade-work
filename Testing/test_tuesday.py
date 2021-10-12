my_list = [3, 4, 2, 54, 11, 9]
print(my_list)
for item in my_list:
    print(item)

for i in range(len(my_list)):
    my_list[i] = 0

print(my_list)


hourly_temperature = [56, 58, 59, 62]
hourly_temperature.append(65)
print(hourly_temperature)

daily_cars_sold_list = [5, 3, 0, 2, 4, 3]
total_cars_sold = 0
for daily_cars_sold in daily_cars_sold_list:
    total_cars_sold += daily_cars_sold

print(total_cars_sold)

my_list = [3, 5, 2, 1]
for i in range(len(my_list)):
    print(my_list[0], end=" ")

my_list = [[3, 2], [1, 4]]
print(my_list[0])

my_text = "Simpson"
print(my_text[3:])