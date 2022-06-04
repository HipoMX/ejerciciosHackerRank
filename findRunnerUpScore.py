if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    new_arr = [x for x in arr if x != max(arr)]
    print(max(new_arr))
