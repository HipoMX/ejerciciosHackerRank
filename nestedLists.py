if __name__ == '__main__':
    second_place_students = []
    python_students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        arr = [name, score]
        python_students.append(arr)
    python_students = sorted(python_students, key=lambda x: x[1], reverse=True)
    second_place = python_students[0][1]

    for name, score in python_students:
        if score == second_place:
            second_place_students.append(name)

    second_place_students.sort()

    for name in second_place_students:
        print(name, end='\n')
