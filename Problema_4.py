"""Elaborați un program care va calcula suma, produsul și media aritmetică a numerelor de la 1 la n,
pentru n introdus de la tastatură."""
n = eval(input("Dati numarul: "))
sum = 0
prod = 1
i = 1
while i<=n:
    sum+=i
    prod=prod*i
    i+=1
    med=sum/n

print("Suma numerelor este", sum, ", produsul este", prod, "iar media aritmetica", med)