# coding=utf-8
from __future__ import division
from matplotlib import pyplot as plt
import datetime,random,time
import numpy as np

print "---第二題---"
# lambda
pi = 3.14
x1 = lambda x,pi: x * x * pi
print x1(5,pi)

print "---第三題---"
# random不重複
def randseed():
    rand10 = range(0,10)
    random.shuffle(rand10)
    return rand10

print randseed()
print randseed()
print randseed()

print "---第四題---"
# matplotlib畫圖
date = [datetime.date(2015,1,10),datetime.date(2015,1,11),datetime.date(2015,1,12),datetime.date(2015,1,13),datetime.date(2015,1,14),datetime.date(2015,1,15),datetime.date(2015,1,16),datetime.date(2015,1,17),datetime.date(2015,1,18),datetime.date(2015,1,19),datetime.date(2015,1,20)]
temp = [16.7,17.4,17.1,20.3,16.2,16.1,17.5,15.3,16.8,16,18.4]

plt.plot(date, temp, color='green', marker='o', linestyle='solid')
plt.title("Taipei January Temperture")
plt.ylabel("Temperature")
plt.xlabel("Date")
plt.show()

print "---第五題---"
# 亂數矩陣相加
def rand():
    return [np.random.randint(1, 10,3),np.random.randint(1, 10,3)]

A = rand()
B = rand()
print A
print B

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)]
            for i in range(num_rows)]

def matrix_add(A, B):
    if shape(A) != shape(B):
        raise ArithmeticError("cannot add matrices with different shapes")
    num_rows, num_cols = shape(A)
    def entry_fn(i, j):
        return A[i][j] + B[i][j]
    return make_matrix(num_rows, num_cols, entry_fn)

print matrix_add(A,B)

print "---第六題---"
# 填空題
a1=0
a2=0
aboth=0
n=100000
def random_ball():
    return random.choice(["B", "Y"])

random.seed(2)
for _ in range(n):
    get1 = random_ball()
    get2 = random_ball()
    if get1 == "B":
        a1 += 1
    if get1 == "B" and get2 == "B":
        aboth += 1
    if get2 == "B":
        a2 += 1

print "P(aboth):", aboth / n
print "P(get1): ", a1 / n
print "P(get2): ", a2 / n
print "P(get1,get2): ", a1*a2 / (n*n)
print "P(get1|get2) = p(aboth)/p(get2): ", (aboth / n) / (a2 / n)
print "p(get1|get2)/p(get2) = p(get1)p(get2)/p((get2) = p(get1) : ",a1 / n



