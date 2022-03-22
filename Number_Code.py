#1 code:
def reverse(num): 
    rev=0
    while(num>0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    print(rev)
reverse(num=12345)



def reverse(num):
    print(str(num)[::-1])
reverse(num=12345)





#2 code:
def reverse(s,e):
    for i in range(s,e+1):
        rev=0
        while(i>0):
            rem=i%10
            rev=rev*10+rem
            i=i//10
        print(rev)
reverse(s=10,e=20)

def reverse(s,e):
    for i in range(s,e+1):
        print(str(i)[::-1])
reverse(s=10,e=20)





#3 code:
def Sum_of_no(num):
    summ=0
    while(num>0):
        rem=num%10;
        summ=rem+summ;
        num=num//10
    print(summ)
Sum_of_no(num=12345)





#4 code:
def Sum_of_no(s,e):
    for i in range(s,e+1):
        summ=0
        while(i>0):
            rem=i%10
            summ=summ+rem
            i=i//10
        print(summ)
Sum_of_no(s=120,e=130)





#5 code:
def pallindrom(num):
    p=0
    cp=num
    while(num>0):
        rem=num%10
        p=p*10+rem
        num=num//10
    print("pallindrom no" if(cp==p) else 'not pallindrom no')
pallindrom(num=121)





#6 code:
def pallindrom(s,e):
    for i in range(s,e+1):
        p=0
        cp=i
        while(i>0):
            rem=i%10
            p=p*10+rem
            i=i//10
        if(cp==p):
            print('No is pallindrom',p)
        else:
            print("No is not pallindrom",p)
pallindrom(s=10,e=50)





#7 code:
def string_pallindrom(str1):
    s1=str1[::-1]
    print("pallindrom" if(str1==s1) else "not pallindrom")
string_pallindrom(str1='121')





#8 code:
def arm(num):
    cp=num
    rm=0
    while(num>0):
        rem=num%10
        rm=rem*rem*rem+rm
        num=num//10
    if(cp==rm):
        print("armstrong no",rm)
    else:
        print("Not armstrong no",rm)
arm(151)





#9 code:
def arm(s,e):
    for i in range(s,e+1):
        rm=0
        cp=i
        while(i>0):
            rem=i%10
            rm=rem*rem*rem+rm
            i=i//10
        if(cp==rm):
            print("armstrng no",cp)
        else:
            print("not armstrong no",cp)
arm(s=100,e=1000)





#10 code:
def prime(num):
    c=0
    for i in range(1,num+1):
        if(num%i==0):
            c=c+1
    if(c==2):
        print("prime no")
    else:
        print("Not prime no",c)
prime(13)




    
#11 code:
def prime(s,e):
    for i in range(s,e+1):
        c=0
        for j in range(1,i+1):
            if(i%j==0):
                c=c+1
        if(c==2):
            print("prim no",i)
        else:
            print("not prime no",i)
prime(1,100)






#12 code:
#type-1
def fib(num):
    f,l=0,1
    for i in range(1,num):
        print(f,end=' ')
        f,l=l,f+l
fib(num=10)

#type-2
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for i in fib():
    if(i>20):
        break
    print(i,end=' ')



    

#13 code:
def fib2(self,found):
        f,s=0,1
        lst=[]
        for i in range(20):
            print(f,end=',')
            lst.append(f)
            f,s=s,s+f
        if(found in lst):
            print("prsent data")
        else:
            print("not present")
fib(10)
