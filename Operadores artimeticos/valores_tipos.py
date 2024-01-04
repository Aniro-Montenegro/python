# Inteiros (int):
#   1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#   -1, -2, -3, -4, -5, -6, -7, -8, -9, -10
#   0
#   1000
valor=10
print(type(valor))
# Float (float):
#   1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0
#   -1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0, -8.0, -9.0
#   0.0
#   1000.0
valor=10.0
print(type(valor))
# Boolean (bool):
#   True
#   False
valor=True
print(type(valor))
# String (str):
#   '1', '2', '3', '4', '5', '6', '7', '8', '9'
#   '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9'
#   '0'
#   '1000'
valor='10'
print(type(valor))
v="palavra"
x='outra palavra'
tamanho=len(v)
print(tamanho)
n=x+" "+v
print(n)
m=v*10
print(m)
# None (NoneType):
#   None
valor=None
print(type(valor))
#Lista (list):
#   []
#   [1, 2, 3, 4, 5, 6, 7, 8, 9]
#   [-1, -2, -3, -4, -5, -6, -7, -8, -9]
#   [0]
#   [1000]
valor=[]
print(type(valor))
lista=[1,2,3,4,5,6,7,8,9]
tamanho=len(lista)
print(tamanho)
lista.append(10)
print(lista)
lista.remove(10)
print(lista)

#Tupla (tuple):
#   ()
#   (1, 2, 3, 4, 5, 6, 7, 8, 9)
#   (-1, -2, -3, -4, -5, -6, -7, -8, -9)
#   (0,)
#   (1000,)
valor=()
print(type(valor))
#Dicionário (dict):
#   {}
#   {'nome': 'Geek University', 'curso': 'Programação em Python'}
valor={}
print(type(valor))
#Conjunto (set):
#   set()
#   {1, 2, 3, 4, 5, 6, 7, 8, 9}
#   {-1, -2, -3, -4, -5, -6, -7, -8, -9}
#   {0}
#   {1000}
valor=set()
print(type(valor))
#Range (range):
#   range(1, 10)
#   range(10)
valor=range(10)
print(type(valor))
print(valor)

X=1,000,000
print(X)
print(type(X))
