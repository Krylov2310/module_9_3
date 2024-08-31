print('\033[30m\033[47mДомашнее задание по теме "Генераторные сборки"\033[0m')
print('\033[30m\033[47mЦель: понять механизм создания генераторных сборок и использования'
      ' встроенных функций-генераторов.\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()

# Дано два списка
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[x]) <= len(second[y]) for x in range(len(first)) for y in range(len(second)) if x == y)

# Пример выполнения кода:
print(list(first_result))
print(list(second_result))
print()
print(thanks)
