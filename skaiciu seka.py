def skaiciu_sekos_skaitmenu_dažnumas(n, m):
    # Sukuriame tuščią žodyną, skirtą skaitmenų dažniui skaičiuoti
    dažnis = {str(i): 0 for i in range(10)}

    # Peržiūrime visus skaičius nuo n iki m (imtinai)
    for sk in range(n, m + 1):
        for skaitmuo in str(sk):
            dažnis[skaitmuo] += 1

    return dažnis

# Pavyzdys
n = int(input("Įveskite pradžios skaičių (n): "))
m = int(input("Įveskite pabaigos skaičių (m): "))

rezultatas = skaiciu_sekos_skaitmenu_dažnumas(n, m)
print("Skaitmenų pasikartojimai sekoje:")
for skaitmuo, kiekis in rezultatas.items():
    print(f"{skaitmuo}: {kiekis}")
