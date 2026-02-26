import random

def input_keyboard():

    n = int(input("Input N: ")) + 1
    matrix = []
    print("Enter the expanded matrix line by line (your(n) +  1) ")
    for i in range(n):
        row = list(map(lambda x: float(x.replace(',', '.')), input().split()))
        matrix.append(row)
    return n, matrix

def input_file():

    with open("data.txt", 'r') as f:
        n = int(f.readline())
        matrix = []
        for i in range(n):
            row = list(map(lambda x: float(x.replace(',', '.')), f.readline().split()))
            matrix.append(row)
    return n, matrix

def input_random():
    n = int(input("Input N: "))
    matrix = [[random.uniform(-10, 10) for j in range(n+1)] for i in range(n)]
    return n, matrix

def matrix_input():
    while True:
        choice = input("Keyboard Input (1) \n From file 'data.txt' (2) \n Random Matrix (3) \n ")
        
        match choice:
            case '1':
                return input_keyboard()
            case '2':
                try:
                    return input_file()
                except FileNotFoundError:
                    print("File 'data.txt' not found. Try another input method.")
                    continue
            case '3':
                return input_random()
            case _:
                print("Try 1, 2 or 3.")