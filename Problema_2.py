"""Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. 
Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative. 
Exemplu: Date de intrare  -5  -3  1  8  12  17  20  21  18  10  6  -2  
Date de ieşire  medie_poz=12.55  medie_neg=-3.33.
"""
n=1
t=0
suma_n=0
suma_p=0
n_p=0
n_n=0
while n<=12:
    t=eval(input("Da temperatura medie a lunii:"))
    n+=1
    if t>=0:
        suma_p+=t
        n_p+=1
    if t<0:
        suma_n+=t
        n_n+=1

print("Temperatura medie pozitiva este" ,round(suma_p/n_p, 2))
print("Temperatura mdeie negativa este" ,round(suma_n/n_n, 2))