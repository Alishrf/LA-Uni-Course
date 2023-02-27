import numpy as np


def solve_equatoins(a:np.array, b:np.array) -> np.array:
    return 2
    


def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(float, input().split())))

    a = np.array(a)

    b = np.array(list(map(float, input().split())))

    print(solve_equatoins(a, b))


if __name__ == "__main__":
    main()
