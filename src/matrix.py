def input_matrix_2x2():
    try:
        print("Masukkan matriks 2x2:")
        return [[float(input(f"a{i + 1}{j + 1}: ")) for j in range(2)] for i in range(2)]
    except ValueError:
        print("Masukkan angka yang valid.")
        return input_matrix_2x2()

def input_matrix_3x3():
    try:
        print("Masukkan matriks 3x3:")
        return [[float(input(f"a{i + 1}{j + 1}: ")) for j in range(3)] for i in range(3)]
    except ValueError:
        print("Masukkan angka yang valid.")
        return input_matrix_3x3()

def input_vector_2():
    try:
        print("Masukkan vektor:")
        return [float(input(f"b{i + 1}: ")) for i in range(2)]
    except ValueError:
        print("Masukkan angka yang valid.")
        return input_vector_2()


def add_matriks(matrix_a, matrix_b):
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(2)] for i in range(2)]

def sub_matriks(matrix_a, matrix_b):
    return [[matrix_a[i][j] - matrix_b[i][j] for j in range(3)] for i in range(3)]

def transpose_2x2(matrix):
    return [[matrix[j][i] for j in range(2)] for i in range(2)]

def transpose_3x3(matrix):
    return [[matrix[j][i] for j in range(3)] for i in range(3)]

def inverse_matrix_2x2(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        print("Peringatan: Determinan matriks nol. Matriks balikan tidak tersedia.")
        return "Matriksnya tidak bisa dibalik."

    result = [
        [matrix[1][1] / det, -matrix[0][1] / det],
        [-matrix[1][0] / det, matrix[0][0] / det]
    ]

    return result

def determinan_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def determinan_3x3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

def gauss_elimination(matrix_a, vector_b):
    n = len(matrix_a)

    for i in range(n):
        if matrix_a[i][i] == 0:
            print("Peringatan: Elemen diagonal utama nol. Mohon masukkan matriks yang valid.")
            return gauss_elimination(input_matrix_2x2(), input_vector_2())

        try:
            pivot = float(matrix_a[i][i])
            for j in range(n):
                matrix_a[i][j] /= pivot
            vector_b[i] /= pivot

            for k in range(i + 1, n):
                factor = matrix_a[k][i]
                for j in range(n):
                    matrix_a[k][j] -= factor * matrix_a[i][j]
                vector_b[k] -= factor * vector_b[i]

        except ValueError:
            print("Masukkan angka yang valid.")
            return gauss_elimination(input_matrix_2x2(), input_vector_2())

    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = vector_b[i]
        for j in range(i + 1, n):
            solution[i] -= matrix_a[i][j] * solution[j]

    return solution


# Main program
while True:
    print("MENU")
    print("1. Penjumlahan dan Pengurangan Matriks")
    print("2. Matriks Transpose")
    print("3. Matriks Balikan")
    print("4. Determinan")
    print("5. Sistem Persamaan Linier")
    print("6. Keluar")

    choice = input("Pilih menu (1-6): ")

    if choice == '1':
        print("Pilihan 1: Penjumlahan dan Pengurangan Matriks")
        print("1. Penjumlahan Matriks")
        print("2. Pengurangan Matriks")
        operation = input("Pilih operasi (1-2): ")

        matrix_a = input_matrix_2x2()
        matrix_b = input_matrix_2x2()

        if operation == '1':
            result = add_matriks(matrix_a, matrix_b)
            print("Hasil penjumlahan matriks:")
        elif operation == '2':
            result = sub_matriks(matrix_a, matrix_b)
            print("Hasil pengurangan matriks:")

        for row in result:
            print(" ".join(map(str, row)))

    elif choice == '2':
        print("Pilihan 2: Matriks Transpose")
        print("1. Matriks Transpose 2x2")
        print("2. Matriks Transpose 3x3")
        operation = input("Pilih operasi (1-2): ")

        if operation == '1':
            matrix_a = input_matrix_2x2()
            result = transpose_2x2(matrix_a)
            print("Hasil transpose matriks:")
        elif operation == '2':
            matrix_a = input_matrix_3x3()
            result = transpose_3x3(matrix_a)
            print("Hasil transpose matriks:")

        for row in result:
            print(" ".join(map(str, row)))

    elif choice == '3':
        print("Pilihan 3: Matriks Balikan")
        print("1. Matriks Balikan 2x2")
        operation = input("Pilih operasi (1): ")

        matrix_a = input_matrix_2x2()

        if operation == '1':
            result = inverse_matrix_2x2(matrix_a)
            print("Hasil invers matriks:")
            if isinstance(result, list):
                for row in result:
                    print(" ".join(map(str, row)))
            else:
                print(result)

    elif choice == '4':
        print("Pilihan 4: Determinan")
        print("1. Determinan 2x2")
        print("2. Determinan 3x3")
        operation = input("Pilih operasi (1-2): ")

        if operation == '1':
            matrix_a = input_matrix_2x2()
            result = determinan_2x2(matrix_a)
            print("Determinan matriks:", result)
        elif operation == '2':
            matrix_a = input_matrix_3x3()
            result = determinan_3x3(matrix_a)
            print("Determinan matriks:", result)

    elif choice == '5':
        print("Pilihan 5: Sistem Persamaan Linier (SPL)")
        try:
            matrix_a = input_matrix_2x2()
            vector_b = input_vector_2()
            result = gauss_elimination(matrix_a, vector_b)
            print("Hasil solusi SPL:", result)
        except Exception as e:
            print(f"Terjadi kesalahan pada SPL: {e}")

    elif choice == '6':
        print("Keluar dari program. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")
