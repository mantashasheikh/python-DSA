s = "welcome to all"
u = s.upper()
print(u)
l = u.lower()
print(l)
c = l.capitalize()
print(c)
print("s=", s)
j = "$".join(s)
print(j)
print("length=", len(s))
print("length=", len(j))
w = " keep it up "
print("length = ", len(w))
st = w.strip()
print("length = ", len(st))
p = "--go get it---"
print(p)
print("p=", len(p))
t = p.strip()
print(t)
pt = p.strip("-")
print(pt)
ft = "--go get$ it$$"
print(ft)
fft = ft.strip("$")
print(fft)
# q = "sun mon tues wed thur"
# print(q)
# print(q.split())
# print(q.split(maxsplit = 3))
# z = "jan#feb#mar#apr"
# print(z.split("#"))