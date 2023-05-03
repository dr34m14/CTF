from Crypto.Util.number import inverse
# n to p,q
# factordb.com
p=61
q=53
m=int(input("m:"))
n=p*q
phi=(p-1)*(q-1)
e=17
d=inverse(e,phi)
c=pow(m,e,n)
print(c)

m=pow(c,d,n)
print(m)