# TODO Напишите функцию find_common_participants
def find_common_participants (group1, group2, delitel = ','):
    text1 = set(group1.split(delitel))
    text2 = set(group2.split(delitel))

    intersection_set = text1.intersection(text2)
    print(intersection_set)
    return sorted(intersection_set)

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))


# TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group_I = "Иванов|Петров|Сидоров"
participants_second_group_I= "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group_I, participants_second_group_I, '|'))
