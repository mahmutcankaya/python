numbers=[1, 2, 3, 4, 5]
for ar in numbers:
    print('a')
names=['Almıla', 'Aytöre', 'Alp']
for name in names:
    print(f'My name is {name}')
name='Almıla'
for n in name:
    print(n)
tuple=(1, 2, 3, 4 , 5)
for t in tuple:
    print(t)
tuple=[(1, 2), (2, 3), (3, 4), (4, 5)]
for t in tuple:
    print(t)
for t, b in tuple:
    print(t)
for t,b in tuple:
    print(b)
for t,b in tuple:
    print(t,b)
d={'k1':1, 'k2':2, 'k3':3}
for item in d:
    print(item)
for item in d.items():
    print(item)
for k,v  in d.items():
    print(k, v)

    #uygulama
sayilar=[1, 3, 5, 7, 9, 12, 19, 21]
# #1 
# a=0
# for n in sayilar:
#     if n%3==0:
#         a+=1
# print(f'Sayılar listesinde üçe bölünebilen sayıların sayısı= {a}')

# #2
# a=0
# for n in sayilar:
#     a+=n
# print(a)

# #3
# a=[]
# for n in sayilar:
#     if n%2==1:
#         a.append(n**2)
# print(a)

sehirler=['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']
# #4
# a=0
# for n in sehirler:
#     if len(n)<=5:
#         a+=1
# print(a)

urunler=[
    {'name':'Samsung S6', 'price':'3000'},
    {'name':'Samsung S7', 'price':'4000'},
    {'name':'Samsung S8', 'price':'5000'},
    {'name':'Samsung S9', 'price':'6000'},
    {'name':'Samsung S10', 'price':'7000'}
]
# #5
# a=0
# for n in urunler:
#     a+=int(n['price'])
# print(a)

# #6
# for n in urunler:
#     if ( int(n['price'])<=5000):
#         print(n['name'])