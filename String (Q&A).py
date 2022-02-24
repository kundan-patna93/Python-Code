1)String reverse
2)word reverse
3)word particular character reverse
4)even no character reverse

5)Check the string is anagram or not
6)Convert all string in upper case:
7)convert all string in lower case
8)Each word first letter upper case
9)sentence first letter upper case
10)find out char duplicate and how many time comes
11)find out char duplicate values with space and how many time comes
12)Maximum occurring character
13)Program to find second most frequent character

12)Check string reverse or not


16)Python Program To Capitalize The First And Last Character Of Each Word In A String.


#1 code:
s='kunal kumar roy patna'
print(s[::-1])

#type2:
s='kunal kumar roy patna'[::-1]
print(s)

#2 code:
data='kunal kumar roy patna'
lst=data.split()
print(' '.join(lst[::-1]))

#3 code:
data='kunal kumar roy patna'
lst=data.split()
list1=[]
for item in lst:
    list1.append(item[::-1])
print(' '.join(list1))

#4 code:
data='kunal kumar roy patna'
lst=data.split()
list1=[]
for i in range(len(lst)):
    if(i%2==0):
        list1.append(lst[i][::-1])
    else:
	list1.append(lst[i][::])
print(' '.join(list1))

#5 code:
def Anan_gram(str1,str2):
    if(len(str1))==(len(str2)):
        print("Annagram" if((sorted(str1))==(sorted(str2))) else "Not annagram1")
    else:
        print("Not Annagram  no2")            
Anan_gram(str1='earth',str2='hear')

#6 code:
data='kunal kumar roy patna ROY PATNA'
str1=data.upper()
print("upper case ouput",str1)

#7 code:
data='kunal kumar ROY PATNA'
str2=data.lower()
print('lower case:',str2)

#8 code:
data='kunal kumar ROY PATNA'
str3=data.title()
print("title:",str3)

#9 code:
data='kunal kumar ROY PATNA'
tr4=data.capitalize()
print("isupper: ",str4)

#10 code:
data='iamkunalkumar'
lst=list(data)
set_data = set(lst) 
for item in set_data:
    count1=0
    count1=lst.count(item)
    if(count1>1):
        print(item,"-",count1,end='\n')


#11 code:
data='i am kunal kumar'
data=data.replace(" ", "")
lst=list(data)
set_data = set(lst) 
for item in set_data:
    count1=0
    count1=lst.count(item)
    if(count1>1):
        print(item,"-",count1,end='\n')

#12 code:
def fun(data):
    data=data.replace(' ','')
    dic={}
    for i in data:
        dic[i]=(dic.get(i,0))+1
    for k,v in dic.items():
        print(k,"occurance",v)
fun(data='i am amit kumar')

#Type2
def fun(data):
    lst=[]
    for ch in data:
        if(ch not in lst):
            lst.append(ch)
            print(ch,'-',data.count(ch))
fun(data='i am amit kumar')

#16 code:
def string_captilize(str1):
    str2=str1.title()
    string=''
    for word in str2.split():
        string=string+word[:-1] + word[-1].upper()+ ' '
    print(string)
string_captilize('how are you')

