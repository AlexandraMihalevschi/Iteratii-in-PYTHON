"""Se introduc succesiv numere nenule până la introducerea numărului 0. 
Să se afişeze suma tuturor numerelor introduse. 
Exemplu: Date de intrare   3  5  4  2  0  Date de ieşire 14."""
n = eval(input("Dati primul numar: "))
sum = 0
while n!=0:
    sum+=n 
    n= eval(input("Dati urmatorul numar: "))

print("Suma numerelor este", sum)