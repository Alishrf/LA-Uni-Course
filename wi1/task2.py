import numpy as np

def transpose(mat):
    return map(list,zip(*mat))

def matrix_minor(mat,i,j):
    return [row[:j] + row[j+1:] for row in (mat[:i]+mat[i+1:])]

def determinant(mat):
    if len(mat) == 2:
        return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]

    det = 0
    for c in range(len(mat)):
        det += ((-1)**c)*mat[0][c]*determinant(matrix_minor(mat,0,c))
    return det

def inverse(a:np.array) -> np.array:
    det= determinant(a)
    if len(a) == 2:
        return [[a[1][1]/det, -1*a[0][1]/det],
                [-1*a[1][0]/det, a[0][0]/det]]

    b = []
    for r in range(len(a)):
        bRow = []
        for c in range(len(a)):
            minor = matrix_minor(a,r,c)
            bRow.append(((-1)**(r+c)) * det(minor))
        b.append(bRow)
    b = transpose(b)
    for r in range(len(b)):
        for c in range(len(b)):
            b[r][c] = b[r][c]/det
    return b


def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(float, input().split())))

    a = np.array(a)

    print(inverse(a))
    print(np.linalg.inv(a))

if __name__ == "__main__":
    main()
