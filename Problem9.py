import sys

def read_matrix(n, m):
    matrix = [[0]*m for _ in range(n)]
    for i in range(n):
        matrix[i] = list(map(int, input().split()))
    return matrix

def matrix_dot_transpose(n, m, k, lhs, rhs):
    ans = [[0]*n for _ in range(k)]
    for i in range(k):
        for j in range(n):
            ans[i][j] = sum([lhs[j][t]*rhs[t][i] for t in range(m)]) 
    return ans

def write_matrix(n, m, matrix):
    for i in range(n):
        print(' '.join(map(str, matrix[i])))

def main():
    n, m, k = map(int, input().split())
    lhs = read_matrix(n, m)
    rhs = read_matrix(m, k)
    write_matrix(k, n, matrix_dot_transpose(n, m, k, lhs, rhs))
    

if __name__ == '__main__':
    main()
