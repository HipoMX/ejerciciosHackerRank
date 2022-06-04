if __name__ == '__main__':
    python_students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        arr = [name, score]
        python_students.append(arr)
    print(python_students)
    print("Sorted List A based on index 0: % s" % (sorted(python_students, key=lambda x: x[0])))
    print("Sorted List A based on index 1: % s" % (sorted(python_students, key=lambda x: x[1])))

