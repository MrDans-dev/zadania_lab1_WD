from math import *
#Z1
a=1
b=0.5
c=-1
print(a,b,c)
#Z2
print(f"DZIALANIA NA A = {a} , B = {b}")
print(f"Dodawanie {a+b}") #dodawanie
print(f"Odejmowanie {b-a}") #odejmowanie
print(f"Mnozenie {a*b}") #mnozenie
print(f"Dzielenie {a/b}") #dzielenie
print(f"Dzielenie bez reszty {a//b}") # dzielenie bez reszty
print(f"Potega {b**a}") #potęga
#Z3
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=c
print(a)
a**=2
print(a)
b%=a
print(b)
#Z4
print("a)",pow(e,10))
print("b)",pow(log(5+(sin(8)**2),10),1/6))
print("c)",floor(3.55))
print("d)",round(4.80))
#Z5
imie = "DANIEL"
nazwisko = "KUCHARSKI"
print(imie.capitalize(),nazwisko.capitalize())
#Z6
txt = "La la, la la la la la na na na na na La la na na, la la la la la na na na na na La la na na, la la la la la na na na na na La la na na, la la la la la na na na na na"
# Naughty Boy - La la la ft. Sam Smith
print(f"La ={txt.count('la')}")
print(f"Na ={txt.count('na')}")
#Z7
imie = "Daniel"
print(imie[1]+imie[5])
#Z8
txt = "La la, la la la la la na na na na na La la na na, la la la la la na na na na na La la na na, la la la la la na na na na na La la na na, la la la la la na na na na na"
print(txt.split())
#Z9

hex_ = 256
float_ = float(6.9)
int_ = int(60.7)
print(hex(hex_))
print(float_)
print(int_)