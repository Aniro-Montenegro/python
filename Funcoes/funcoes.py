x=int("120")
print(x)
print(type(x))
x=float("120.5")
print(x)
print(type(x))
x=str(120)
print(x)
print(type(x))
x=bool("True")
print(x)
print(type(x))
x=int(4548.545)
print(x)
x=float(10)
print(x)
try:
    x=int("Geek")
    print(x)
except:
    print("Deu erro")

def maior(x,y):
    if x>y:
        return x
    else:
        return y
def busca(lista,elemento):
    for i in range(len(lista)):
        if lista[i]==elemento:
            return i
    return None
s=maior(10,20)
print(s)
b=busca([1,2,3,4,5,6,7,8,9],9)
print(b)

def buscamaior(lista):
    maior=lista[0]
    for i in range(1,len(lista)):
        if lista[i]>maior:
            maior=lista[i]
    return maior
m=buscamaior([1,2,3,4,5,6,7,8,9])
print(m)