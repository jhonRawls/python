#python 学习
print("hello this is my first python program")

print(' 300 + 200 =',300+200)

print('i j\'m ok ')

print("中文测试")

print('Hi, %s, you have $%08d.' % ('Michael', 1))


#list
arrayList=['a','b','c']
print(len(arrayList))
print(arrayList[-1])
arrayList.append('d')

#input
print(arrayList)
print('please input something')
# age=int(input('age:'))
age=12
if age>=18:
	print('you age is ',age)
	print('adult')
else:
	print('you age is ',age)
	print('teenager')

#for
names=['michel','bob','jhon']
for name in names:
	print(name)

sum=0
for x in [1,2,3,4,5,6,7,8,9]:
	sum=sum+x
print(sum)
print(list(range(10)))

#dict
d={"jhon":83,"david":37}
print(d["jhon"])
print(d.get("jhon"))

#define function
def my_abs(x):
	if x>0:
		return x;
	else:
		return -x;

print(my_abs(-8999))

def fact(n):
	if(n==1):
		return 1
	else:
		return n*fact(n-1)
print(fact(100))


l=[]
n=1
while n<=99:
	l.append(n)
	n=n+2
	pass
print(len(l))

print(l[0:20])c


from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance(l,Iterable))

import urllib.request


userId=[1143718680]


response=urllib.request.urlopen('https://pan.baidu.com/share/home?uk=1143718680&view=follow')


print(response.read().decode('UTF-8'))

/pcloud/friendpage?type=follow&uk=1143718680&self=0