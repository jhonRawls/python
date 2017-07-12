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
age=int(input('age:'))
if age>=18:
	print('you age is ',age)
	print('adult')
else:
	print('you age is ',age)
	print('teenager')