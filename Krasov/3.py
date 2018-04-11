import random
import copy

def sozdan(n):
    matrix = [[str(random.randrange(100)) for i in range(n)] for j in range(n)]
    return matrix

def determinant(matrix):
    result = 0
    length = len(matrix)
    if length == 1:
        return matrix[0][0]
    if length == 2:
        return int(matrix[0][0]) * int(matrix[1][1]) - \
               int(matrix[0][1]) * int(matrix[1][0])
    for i in range(length):
        buf_matrix = copy.deepcopy(matrix)
        for j in range(length):
            del buf_matrix[j][i]
        result += int(matrix[0][i]) * pow((-1), i) * determinant(buf_matrix[1:])
    return result

def turn(matrix, direction):
    if direction:
        buf_matrix = copy.deepcopy(matrix)
        length = len(matrix)
        for i in range(length):
            for j in range(length):
                buf_matrix[i][j] = matrix[j][length - i - 1]
    else:
        buf_matrix = copy.deepcopy(matrix)
        length = len(matrix)
        for i in range(length):
            for j in range(length):
                buf_matrix[i][j] = matrix[length - j - 1][i]
    return buf_matrix

def sort(matrix, sort_by, order):
    flag = True
    length = len(matrix)
    buff_matrix = copy.deepcopy(matrix)
    if sort_by == 1:
        if order:
            for k in range(length):
                for i in range(length - 1):
                    for j in range(length - i - 1):
                        if int(buff_matrix[j][k]) > int(buff_matrix[j + 1][k]):
                            buff = buff_matrix[j][k]
                            buff_matrix[j][k] = buff_matrix[j + 1][k]
                            buff_matrix[j + 1][k] = buff
                            flag = False
                    if flag:
                        break
        else:
            for k in range(length):
                for i in range(length - 1):
                    for j in range(length - i - 1):
                        if int(buff_matrix[j][k]) < int(buff_matrix[j + 1][k]):
                            buff = buff_matrix[j][k]
                            buff_matrix[j][k] = buff_matrix[j + 1][k]
                            buff_matrix[j + 1][k] = buff
                            flag = False
                    if flag:
                        break
    elif sort_by == 2:
        if order:
            for k in range(length):
                for i in range(length - 1):
                    for j in range(length - i - 1):
                        if int(buff_matrix[k][j]) > int(buff_matrix[k][j + 1]):
                            buff = buff_matrix[k][j]
                            buff_matrix[k][j] = buff_matrix[k][j + 1]
                            buff_matrix[k][j + 1] = buff
                            flag = False
                    if flag:
                        break
        else:
            for k in range(length):
                for i in range(length - 1):
                    for j in range(length - i - 1):
                        if int(buff_matrix[k][j]) < int(buff_matrix[k][j + 1]):
                            buff = buff_matrix[k][j]
                            buff_matrix[k][j] = buff_matrix[k][j + 1]
                            buff_matrix[k][j + 1] = buff
                            flag = False
                    if flag:
                        break
    else:
        print('Некорректный ввод')
    return buff_matrix

def sortall(matrix, order):
    buf_matrix = []
    copy_matrix = copy.deepcopy(matrix)
    length = len(matrix)
    flag = True
    for i in range(length):
        for j in range(length):
            buf_matrix.append(matrix[i][j])
    length_buff = len(buf_matrix)
    if order:
        for i in range(length_buff - 1):
            for j in range(length_buff - i - 1):
                if int(buf_matrix[j]) < int(buf_matrix[j + 1]):
                    buff = buf_matrix[j]
                    buf_matrix[j] = buf_matrix[j + 1]
                    buf_matrix[j + 1] = buff
                    flag = False
            if flag:
                break
    else:
        for i in range(length_buff - 1):
            for j in range(length_buff - i - 1):
                if int(buf_matrix[j]) > int(buf_matrix[j + 1]):
                    buff = buf_matrix[j]
                    buf_matrix[j] = buf_matrix[j + 1]
                    buf_matrix[j + 1] = buff
                    flag = False
            if flag:
                break
    for i in range(length):
        for j in range(length):
            copy_matrix[i][j] = buf_matrix[i * length + j]
    return copy_matrix

def minmax(matrix):
    flag = True
    copy_matrix = copy.deepcopy(matrix)
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            if flag:
                minimum = int(matrix[i][j])
                i_min = i
                j_min = j
                maximum = int(matrix[i][j])
                i_max = i
                j_max = j
                flag = False
            else:
                if int(matrix[i][j]) > maximum:
                    maximum = int(matrix[i][j])
                    i_max = i
                    j_max = j
                if int(matrix[i][j]) < minimum:
                    minimum = int(matrix[i][j])
                    i_min = i
                    j_min = j
    buff = copy_matrix[i_min][j_min]
    copy_matrix[i_min][j_min] = copy_matrix[i_max][j_max]
    copy_matrix[i_max][j_max] = buff
    print('Минимальный элемент с индексами [%s][%s]: %s' % (i_min, j_min, minimum))
    print('Максимальный элемент с индексами [%s][%s]: %s' % (i_max, j_max, maximum))
    return copy_matrix

def sorts(matrix, sort_by, order):
    length = len(matrix)
    flag = True
    array_of_summ = [[i, 0] for i in range(length)]
    buff_matrix = [[0 for i in range(length)] for j in range(length)]
    if sort_by == 1:
        if order:
            for i in range(length):
                for j in range(length):
                    array_of_summ[i][1] += int(matrix[j][i])
            for i in range(length - 1):
                for j in range(length - i - 1):
                    if array_of_summ[j][1] > array_of_summ[j + 1][1]:
                        buff_0 = array_of_summ[j + 1][0]
                        buff_1 = array_of_summ[j + 1][1]
                        array_of_summ[j + 1][0] = array_of_summ[j][0]
                        array_of_summ[j + 1][1] = array_of_summ[j][1]
                        array_of_summ[j][0] = buff_0
                        array_of_summ[j][1] = buff_1
                        flag = False
                if flag:
                    break
            for i in range(length):
                if i != array_of_summ[i][0]:
                    for j in range(length):
                        buff_matrix[j][i] = matrix[j][array_of_summ[i][0]]
                else:
                    for j in range(length):
                        buff_matrix[j][i] = matrix[j][i]
        else:
            for i in range(length):
                for j in range(length):
                    array_of_summ[i][1] += int(matrix[j][i])
            for i in range(length - 1):
                for j in range(length - i - 1):
                    if array_of_summ[j][1] < array_of_summ[j + 1][1]:
                        buff_0 = array_of_summ[j + 1][0]
                        buff_1 = array_of_summ[j + 1][1]
                        array_of_summ[j + 1][0] = array_of_summ[j][0]
                        array_of_summ[j + 1][1] = array_of_summ[j][1]
                        array_of_summ[j][0] = buff_0
                        array_of_summ[j][1] = buff_1
                        flag = False
                if flag:
                    break
            for i in range(length):
                if i != array_of_summ[i][0]:
                    for j in range(length):
                        buff_matrix[j][i] = matrix[j][array_of_summ[i][0]]
                else:
                    for j in range(length):
                        buff_matrix[j][i] = matrix[j][i]
    elif sort_by == 2:
        if order:
            for i in range(length):
                for j in range(length):
                    array_of_summ[i][1] += int(matrix[i][j])
            for i in range(length - 1):
                for j in range(length - i - 1):
                    if array_of_summ[j][1] > array_of_summ[j + 1][1]:
                        buff_0 = array_of_summ[j + 1][0]
                        buff_1 = array_of_summ[j + 1][1]
                        array_of_summ[j + 1][0] = array_of_summ[j][0]
                        array_of_summ[j + 1][1] = array_of_summ[j][1]
                        array_of_summ[j][0] = buff_0
                        array_of_summ[j][1] = buff_1
                        flag = False
                if flag:
                    break
            for i in range(length):
                if i != array_of_summ[i][0]:
                    for j in range(length):
                        buff_matrix[i][j] = matrix[array_of_summ[i][0]][j]
                else:
                    for j in range(length):
                        buff_matrix[i][j] = matrix[i][j]
        else:
            for i in range(length):
                for j in range(length):
                    array_of_summ[i][1] += int(matrix[i][j])
            for i in range(length - 1):
                for j in range(length - i - 1):
                    if array_of_summ[j][1] < array_of_summ[j + 1][1]:
                        buff_0 = array_of_summ[j + 1][0]
                        buff_1 = array_of_summ[j + 1][1]
                        array_of_summ[j + 1][0] = array_of_summ[j][0]
                        array_of_summ[j + 1][1] = array_of_summ[j][1]
                        array_of_summ[j][0] = buff_0
                        array_of_summ[j][1] = buff_1
                        flag = False
                if flag:
                    break
            for i in range(length):
                if i != array_of_summ[i][0]:
                    for j in range(length):
                        buff_matrix[i][j] = matrix[array_of_summ[i][0]][j]
                else:
                    for j in range(length):
                        buff_matrix[i][j] = matrix[i][j]
    else:
        print('Некорректный ввод')
    return buff_matrix

def stepen(matrix, q):
    length = len(matrix)
    copy_matrix = [[0 for i in range(length)] for j in range(length)]
    buff_matrix = copy.deepcopy(matrix)
    if q == 0:
        return [['1', '0', '0'], ['0', '1', '0'], ['0', '0', '1']]
    elif q == 1:
        return buff_matrix
    else:
        for st in range(q - 1):
            for i in range(length):
                for j in range(length):
                    for k in range(length):
                        copy_matrix[i][j] += int(matrix[i][k]) * \
                                             int(buff_matrix[k][j])
            buff_matrix = copy.deepcopy(copy_matrix)
            copy_matrix = [[0 for i in range(length)] for j in range(length)]
        for i in range(length):
            for j in range(length):
                buff_matrix[i][j] = str(buff_matrix[i][j])
        return buff_matrix

def transpose(matrix):
    buff_matrix = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            buff_matrix[i][j] = matrix[j][i]
    return buff_matrix

def minor(matrix, i, j):
    buff_matrix = copy.deepcopy(matrix)
    del buff_matrix[i]
    for k in range(len(buff_matrix)):
        del buff_matrix[k][j]
    return buff_matrix

def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        print('Обратная марица не существует\n')
        return ''
    length = len(matrix)
    buff_matrix = copy.deepcopy(matrix)
    buff_matrix = transpose(buff_matrix)
    matrix_of_alg_compl = [['0' for i in range(length)]
                           for j in range(length)]
    for i in range(length):
        for j in range(length):
            matrix_of_alg_compl[i][j] = pow(-1, (i + j + 2)) * \
                                        determinant(minor(buff_matrix, i, j))
    for i in range(length):
        for j in range(length):
            if matrix_of_alg_compl[i][j] == 0:
                buff_matrix[i][j] = '0'
            else:
                buff_matrix[i][j] = str(matrix_of_alg_compl[i][j] / det)
    return buff_matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))
    print('\n')


def main():
    n = int(input('Размер квадратной матрицы: '))
    matrix = sozdan(n)
    print_matrix(matrix)
    qq = int(input('Введите номер задачи 1-8: '))
    if qq == 1:
        print('Определитель : ', determinant(matrix), '\n')
    elif qq == 2:
        dd = bool(input('По часовой сстрелке - True, против часовой стрелки - False '))
        print_matrix(turn(matrix, dd))
    elif qq == 3:
        z = int(input('Стобцы - 1, Строки - 2'))
        dd = bool(input('по возрастаниюе - True, по убыванию - False '))
        print_matrix(sort(matrix, z, dd))
    elif qq == 4:
        dd = bool(input('По возрастаниюе - True, по убыванию - False '))
        print_matrix(sortall(matrix, dd))
    elif qq == 5:
        print('Замена элементов местами \n')
        print_matrix(minmax(matrix))
    elif qq == 6:
        dd = bool(input('по возрастаниюе - True, по убыванию - False '))
        z = int(input('Стобцы - 1, Строки - 2'))
        print_matrix(sorts(matrix, z, dd))
    elif qq == 7:
        l = int(input('Степень'))
        print('Матрица в степени:\n')
        print_matrix(stepen(matrix, l))
    elif qq == 8:
        print('Матрица обратная данной: \n')
        print_matrix(inverse(matrix))


if __name__ == '__main__':
    main()