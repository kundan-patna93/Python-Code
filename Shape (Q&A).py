1)
*
* *
* * *
* * * *
* * * * *


2)
    *
   * *
  * * *
 * * * *
* * * * *


3)
        *
      * *
    * * *
  * * * *
* * * * *



4)
* * * * *
 * * * *
  * * *
   * *
    *


5)
* * * * *
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
* * * * *


6)
* * * * *
*       *
*       *
*       *
* * * * * 


7)
a
a a
a a a
a a a a
a a a a a


8)
a
b b
c c c
d d d d
e e e e e


9)
a
a b
a b c
a b c d
a b c d e


10)
         *
        ***
       *****
      *******
     *********


#1 code:
def shap(num):
    for i in range(1,num+1):
        for j in range(0,i):
            print("*",end=' ')
        print()
shap(10)

#2 code:
def shap(num):
    for i in range(1,num+1):
        for j in range(num,(i-1),-1):
            print(" ",end='')
        for k in range(0,i):
            print("*",end=' ')
        print()
shap(5)

#3 code:
def shap(num):
    for i in range(1,num+1):
        for j in range(num,(i-1),-1):
            print(" ",end=' ')
        for k in range(1,i+1):
            print("*",end=' ')
        print()
shap(5)

#4 code:
def shap(num):
    for i in range(1,num+1):
        for j in range(1,i):
            print(" ",end='')
        for k in range(num,(i-1),-1):
            print("*",end=" ")
        print()
shap(5)

#5 code:
def shap(num):
    for i in range(1,num+1):
        for j in range(1,i):
            print(" ",end="")
        for k in range(num,(i-1),-1):
            print("*",end=" ")
        print()
    for z in range(1,num+1):
        for x in range(num,z,-1):
            print(" ",end="")
        for y in range(1,z+1):
            print("*",end=' ')
        print()
shap(5)

#6 code:
def shap(num):
    print("* "*num)
    for i in range(1,num-1):
        for i in range(num-1,num):
            print("*",end='')
        for j in range(0,num+2):
            print(" ",end='')
        for k in range(num-1,num):
            print("*")
    print("* "*num)
shap(5)

#7 code:
def shap(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("a",end=' ')
        print()
shap(5)

#8 code:
def shap(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(chr(64+i),end=' ')
        print()
shap(5)

#9 code:
def shap(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(chr(64+j),end=' ')
        print()
shap(5)

#10 code:
def ten(data):
    t=2
    for i in range(data):
        for j in range(data,i+1,-1):
            print(" ",end='')
        for k in range(1,t+1):
            print("*",end='')
        t=t+2
        print()
ten(10)
