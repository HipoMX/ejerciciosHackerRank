if __name__ == '__main__':
    second_place_students = []
    python_students = []
    scores = set()

    for i in range(int(input())):
        name = input()
        score = float(input())
        arr = [name, score]
        scores.add(score)
        python_students.append(arr)

    second_lowest = sorted(scores)[1]

    for name, score in python_students:
        if score == second_lowest:
            second_place_students.append(name)

    second_place_students.sort()

    for name in second_place_students:
        print(name, end='\n')
