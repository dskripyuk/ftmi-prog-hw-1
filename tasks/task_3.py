
person = ['Энакин Скайуокер',
		  41,
		  ['Татуин', 'Набу', 'Джеонозис', 'Корусант', 'Мустафар', 'Звезда Смерти'],
		  {'световой меч': 'синий', 'ранг': 'лорд ситхов'}
		  ]

while True:
	task_number = input("Введите номер задания (или 'выход' для завершения): ")

	if task_number.lower() == 'выход':
		break

	try:
		task_number = int(task_number)
	except:
		print("Пожалуйста, введите число или 'выход'.")
		continue

	if task_number == 1:
		name = person[0].split()
		print(f"Персона: {name[1]}, {name[0]}")

	elif task_number == 2:
		print(f"Возраст Энакина: {person[1]}")

	elif task_number == 3:
		places = ', '.join(person[2])
		print(f"Места, связанные с крупными событиями: {places}")

	elif task_number == 4:
		count_places = len(person[2])
		print(f"Количество мест: {count_places}")

	elif task_number == 5:
		imper = 'Звезда Смерти' in person[2]
		print(f"Служит Империи: {imper}")

	elif task_number ==6:
		color = person[3]['световой меч']
		print(f"Цвет светового меча: {color}")

	elif task_number == 7:
		person[1] = 42
		print(f"Новый возраст Энакина: {person[1]}")

	elif task_number == 8:
		if 'Эндор' not in person[2]:
			person[2].append('Эндор')
		new_places = ', '.join(person[2])
		print(f"Обновленный список мест: {new_places}")

	elif task_number == 9:
		rank = person[3]['ранг']
		if rank == 'лорд ситхов':
			print("Энакин - лорд ситхов")
		else:
			print("Энакин - джедай")

	elif task_number == 10:
		if len(person[2]) > 4:
			print("Энакин побывал во многих местах")
		else:
			print("Энакин не так много путешествовал")

	else:
		print("Неверный номер задания. Пожалуйста, введите число от 1 до 10.")


# Примечание: выполнять данное задание с помощью функций выше необязательно, однако, возможно
# использование данных функций поможет вам на этапе размышлений о дизайне программы
# Your code here /ᐠ˵- ⩊ -˵マ
