user_data = input("Введите любое значение: ")

line_data = "Это строка в которую {} новую строку".format(user_data)
print(line_data)

line_data = "Это строка в которую {} новую строку".format("замена в строке")
print(line_data)
print(len(line_data))
if line_data.find("строка",4,10) != -1  :
    print("Да")
else:
    print("Нет")
