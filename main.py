import time
import math
import random as r
from tkinter import filedialog
from tkinter import *  
from tkinter import scrolledtext
from tkinter import messagebox as mb
def prost(n):
    p = n
    c = 0
    for i in range(50):
        x = int(2+(math.sqrt(p)-2)*r.random())
        b = int(x**2) # Квадратичные вычеты
        # Проверка тестов Ферма и Соловея-Штрассена
        if (pow(b,int((p-1)/2),p) != 1) or (pow(b,(p-1), p) != 1):
            break
        else: 
            c += 1
    if c == 50:
        return 1
    else:
        return 0
def sum_ravn(a,b):
    c = []
    for i in range(len(a)):
        c.append((a[i]+b[i])%2)
    return c
# Наибольший общий делитель
def gcd(a, b):
    if b>a:
        c = a
        a = b
        b = c
    while b!=0:
        c = a % b
        a = b
        b = c
    return a
# Символ Лежандра расширенный
def L(a,p):
    if p == 2:
        if (a % 8 == 1) or ((a % 8) - 8 == -1):
            return 1
        elif (a % 8 == 3) or ((a % 8) - 8 == -3):
            return -1
        else:
            return 0
    elif a % p == 0:
        return 0
    elif pow(a,int((p-1)/2),p) == 1:
        '''a**((p-1)/2) % p '''
        return 1
    else:
        return -1
# Создание факторной базы    
def prost_base(n, B):
    # Генерация простых дисел до B с помощью решета Эратосфена
    sieve = set(range(2, B+1))
    arr_prime = []
    while sieve:
        prime = min(sieve)
        sieve -= set(range(prime, B+1, prime))
        arr_prime.append(prime)
    arr_prime
    # Формирование базы
    base = []
    for i in range(len(arr_prime)):
        if L(n,arr_prime[i]) == 1:
            base.append(arr_prime[i])
    if not 2 in base:
        base.append(2)
    return base
# Проверка на гладкость
def is_smooth(n,k):
    g = gcd(n,k)
    while g > 1:
        while  n/g == n//g:
            n = n//g
        if n == 1:
            return 1
        else:
            g = gcd(n,k)
    return 0 
def fac_smooth(x, base):
    vec = []
    for i in range(len(base)):
        j = 0
        while x/base[i] == x//base[i]:
            j += 1
            x = x//base[i]
        vec.append(j)
    return vec        
def fac(a,b,n):
    a = a%n
    b = b%n
    
    p = int(gcd(a+b,n))
    q = int(gcd(a-b,n))
    return [p,q]
def sqrt_convergents(n):
    if prost(n) == 1:
        mb.showerror("Error", "Число простое")
        return
    n_sqrt = int(math.sqrt(n)) # 
    a = 2*n_sqrt #
    y = n_sqrt #
    z = 1 #
    E0 = 1
    E1 = 0
    F0 = 0
    F1 = 1
    A = [] #
    B = [] #
    Bp = int(math.exp(math.sqrt(math.log(n)*math.log(math.log(n)))/2)) #
    base = [] #
    base = list(prost_base(n, Bp))
    k = 1
    for i in range(len(base)):
        k = k*base[i]
    while 1 == 1:
        A.append(E1 + n_sqrt*F1)
        B.append(F1)
        y = a*z - y
        z = int((n - y**2)/z)
        a = int((n_sqrt+y)/z)
        E0, E1 = E1, a*E1 + E0
        F0, F1 = F1, a*F1 + F0
        E0 = E0 % n
        E1 = E1 % n
        F0 = F0 % n
        F1 = F1 % n
        if z == 1:
            break
    r = []
    for i in range(len(A)):
        if ((A[i])**2) % n > n/2:
            r.append(abs(((A[i])**2) % n - n))
        else:
            r.append(((A[i])**2) % n)
    Q = []
    for i in range(len(A)):
        if is_smooth(r[i] ,k) == 1:
            Q.append([A[i]%n,r[i]])
    vec = []
    for i in range(len(Q)):
        vec.append(fac_smooth(Q[i][1], base))
    vecbin = [[0]*len(vec[0]) for i in range(len(vec))]
    for i in range(len(vec)):
        for j in range(len(vec[i])):
            vecbin[i][j] = vec[i][j] % 2 

    return [Q,vec, vecbin]
def  gaussian_elimination(vecbin, Q, n):
    global bB
    c = 0
    h = []
    if vecbin == []:
        return vecbin
    for i in range(len(vecbin)):
        k = 0
        for j in range(len(vecbin[i])):
            if vecbin[i][j] == 0:
                k += 1
            else:
                continue
        #print(k)
        if k == len(vecbin[i]):
            h.append(i)
    for i in range(len(h)):
        a = Q[h[i]][0]
        b = math.sqrt(Q[h[i]][1])
        c = fac(a,b,n)
        if 1 in c:
            continue
        else:
            return c
    h = []
    for i in range(len(vecbin[0])):
        index = []
        print(vecbin)
        u = 0
        for j in range(len(vecbin)):
            if (vecbin[j][i] == 1) and (not j in index):
                index.append(j)
                u = 1
        if u == 0:
            #index.append(-1)
            continue
        for j in range(len(vecbin)):
            if (vecbin[j][i] == 1) and (not j in h): 
                vecbin[j] = sum_ravn(vecbin[j], vecbin[index[-1]])
        h.append(index[-1])
        for ii in range(len(vecbin)):
            t = 0
            for jj in range(len(vecbin[ii])):
                if vecbin[ii][jj] == 0:
                    t += 1
            if t == len(vecbin[ii]):
                I = ii
                print(I)
                aA = Q[I][0]
                print(aA)
                bB = Q[I][1]
                print(bB)
                print(h)
                for iii in range(len(h)):
                    if h[iii] == -1:
                        continue
                    aA = aA*Q[h[iii]][0]
                    print(aA)
                    bB = bB*Q[h[iii]][1]
                    print(bB)
                    print(Q[h[iii]])
                bB = int(math.sqrt(bB))  
                cC = fac(aA,bB,n)
                print(vecbin)
                print('!')
                return cC
    return c
def btn():
    n = int(n_entry.get())
    t0 = time.perf_counter()
    c = sqrt_convergents(n)
    p = gaussian_elimination(c[2],c[0], n)[0]
    q = gaussian_elimination(c[2],c[0], n)[1]
    t1 = time.perf_counter()
    txt1.delete(1.0, END)
    txt1.insert(INSERT, p) 
    txt2.delete(1.0, END)
    txt2.insert(INSERT, q)
    print(t1-t0)
window = Tk()  
window.title("CFRAC")  
window.geometry('310x195')  
btn1 = Button(window, text="Факторизовать число", command=btn)  
btn1.grid(column=1, row=0)  
lbl = Label(window, text="Введите m: ")  
lbl.grid(column=0, row=1)  
n_entry = Entry(window,width=19) 
n_entry.grid(column=1, row=1)
lbl1 = Label(window, text="Множитель 1: ")  
lbl1.grid(column=0, row=2)  
txt1 = scrolledtext.ScrolledText(window, width=19, height=1)  
txt1.grid(column=1, row=2)
lbl2 = Label(window, text="Множитель 2: ")  
lbl2.grid(column=0, row=3)  
txt2 = scrolledtext.ScrolledText(window, width=19, height=1)  
txt2.grid(column=1, row=3)
window.mainloop()
