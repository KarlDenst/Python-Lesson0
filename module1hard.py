grades = [[5, 3, 3, 5, 4],[2, 2, 2, 3],[4, 5, 5, 2],[4, 4, 3],[5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students=list(students)
students.sort()


student_ave_marks={students[0]:sum(grades[0])/len(grades[0]),
                   students[1]:sum(grades[1])/len(grades[1]),
                   students[2]:sum(grades[2])/len(grades[2]),
                   students[3]:sum(grades[3])/len(grades[3]),
                   students[4]:sum(grades[4])/len(grades[4])}
print(student_ave_marks)

# или так

ave_marks=[sum(grades[0])/len(grades[0]),
                   sum(grades[1])/len(grades[1]),
                   sum(grades[2])/len(grades[2]),
                   sum(grades[3])/len(grades[3]),
                   sum(grades[4])/len(grades[4])]

new_student_ave_marks=dict(zip(students,ave_marks))
print(new_student_ave_marks)


#интерфейс для учителя

name=input('Введите имя студента: ')
print('Средний балл студента',name,new_student_ave_marks[name])


