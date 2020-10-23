"""Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. 
Să se afişeze suma tuturor numerelor pare introduse.  
Exemplu: Date de intrare  7  4   6   2   1   9   Date de ieşire 12.  """
n = eval(input("Primul numar:"))
sum=0
while (n%2==0)or(n%3!=0):
    n+=1
    n = eval(input("Urmatorul numar: "))
    if n%2==0:
        sum+=n

print("Suma numerelor pare este" ,sum)