# matrix_ops.py
# Day 9 AM - Lists Deep Dive
# Matrix Operations using nested lists


def matrix_add(A, B):
    # Check dimensions match
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_transpose(matrix):
    # zip(*matrix) groups columns together
    return [list(row) for row in zip(*matrix)]


def matrix_multiply(A, B):
    # Check if multiplication is valid: cols of A == rows of B
    if len(A[0]) != len(B):
        raise ValueError(
            f"Cannot multiply: A has {len(A[0])} cols but B has {len(B)} rows."
        )
    return [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*B)]
        for row_a in A
    ]


def print_matrix(matrix, label=""):
    if label:
        print(f"{label}:")
    for row in matrix:
        print(" ", row)
    print()


# ---- Tests ----
if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    print("=== 2x2 Matrix Tests ===")
    print_matrix(matrix_add(a, b), "A + B")
    print_matrix(matrix_transpose(a), "Transpose of A")
    print_matrix(matrix_multiply(a, b), "A x B")

    # Test with 2x3 and 3x2
    c = [[1, 2, 3], [4, 5, 6]]       # 2x3
    d = [[7, 8], [9, 10], [11, 12]]   # 3x2

    print("=== 2x3 and 3x2 Matrix Tests ===")
    print_matrix(matrix_transpose(c), "Transpose of C (2x3 -> 3x2)")
    print_matrix(matrix_multiply(c, d), "C x D")

    # Test dimension mismatch
    print("=== Mismatch Test ===")
    try:
        matrix_multiply(a, c)  # 2x2 * 2x3 is valid actually
        matrix_add(a, c)       # 2x2 + 2x3 should fail
    except ValueError as e:
        print(f"  Caught error: {e}\n")
