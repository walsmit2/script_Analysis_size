#!/usr/bin/env python3

import os

# Изменяемая переменная, для указания пути
way = os.getcwd()

# Функция преобразования из байта в килобайт, мегабайт, гигабайт, терабайт
def humanBytes(B):
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2)
    GB = float(KB ** 3)
    TB = float(KB ** 4)

    if B < KB:
        return '{0}\t{1}'.format(B, 'byte' if 0 == B > 1 else 'byte')
    elif KB <= B < MB:
        return '{0:.1f}\tKB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.1f}\tMB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.1f}\tGB'.format(B / GB)
    elif TB < B:
        return '{0:.1f}\tTB'.format(B / TB)

# Функция анализа размера файла, директории
def sizeAnalysis(path):

    res = []
    path = os.listdir(path)

    # Добавдение содержимого в массив
    for i in path:
        res.append((humanBytes(os.path.getsize(i)), i))

    # Сортировка массива по значению i[1], по уменьшению размера
    sort_res = sorted(res, key=lambda x: x[1], reverse=True)

    # Форматирование вывода, убирание лишних знаков
    for i in sort_res:
        print("{}\t\t{}".format(i[0], i[1]))

print("РАЗМЕР\tЕД-ИЗМ\t\tНАЗВАНИЕ")
sizeAnalysis(way)
