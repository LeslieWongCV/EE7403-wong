# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 9:09 下午
# @Author  : Yushuo Wang
# @FileName: HistogramEqualization.py
# @Software: PyCharm
# @Blog    ：https://lesliewongcv.github.io/

import cv2
import numpy as np
import matplotlib.pyplot as plt
PATH = '/Users/leslie/PycharmProjects/NTUEEE/EE7403'
img = cv2.imread('len_full.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
count = np.zeros(256, np.float)
x = np.linspace(0, 255, 256)


def pltHistogram(input, name, color):
    plt.figure()
    plt.title(name)
    plt.bar(x, input, color=color)
    plt.savefig(f'Imgs/{name}.png')
    plt.show()


def getHistogram(gray):
    global count
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            count[int(gray[i, j])] += 1
    count = count / (gray.shape[0] * gray.shape[1])  # nt/n


def getCumulative():
    for i in range(1, 256):
        count[i] += count[i - 1]


getHistogram(gray)
count1 = count
pltHistogram(count, "Original", 'b')
getCumulative()

'''
通过累计函数映射，使得处理后的直方图的累计分布函数是一个近似 y = x 的函数

'''
map1 = count * 255
pltHistogram(map1/255, "Original Cumulative", 'r')

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        p = gray[i, j]
        gray[i, j] = map1[p]

count = np.zeros(256, np.float)
getHistogram(gray)

pltHistogram(count, "HistogramEqualization", 'b')
count2 = count
getCumulative()
pltHistogram(count, "Cumulative", 'r')

#cv2.imshow('gray', gray)
#cv2.waitKey(0)
