# Funkcija pradiniams duomenims skaityti
def skaityti_duomenis(filename):duomenys.txt
with open("duomenys.txt", "r", encoding='utf-8') as file:
        duomenys = file.readline().strip().split()
        [float(x) for x in duomenys]

# Funkcija sportininkams atrinkti
def atrinkti_sportininkus(duomenys, kvalifikacine_norma):
    kvalifikuoti = [rez for rez in duomenys if rez >= kvalifikacine_norma]
    likusieji = sorted([rez for rez in duomenys if rez < kvalifikacine_norma], reverse=True)
    
    if len(kvalifikuoti) >= 12:
        galutiniai = kvalifikuoti[:12]
    else:
        galutiniai = kvalifikuoti + likusieji[:12 - len(kvalifikuoti)]

    return sorted(galutiniai, reverse=True)

# Funkcija rezultatams įrašyti į failą
def irasyti_rezultatus(filename, rezultatai):
    with open(filename, 'w') as file:
        for rez in rezultatai:
            file.write(f"{rez:.2f}\n")

# Pagrindinė programos dalis
if __name__ == "__main__":
    # Parametrai
    input_file = "duomenys.txt"
    output_file = "Rezultatai4.txt"
    kvalifikacine_norma = 60.0

    # Programos vykdymas
    pradiniai_duomenys = skaityti_duomenis(input_file)
    galutiniai_rezultatai = atrinkti_sportininkus(pradiniai_duomenys, kvalifikacine_norma)
    irasyti_rezultatus(output_file, galutiniai_rezultatai)

    print("Rezultatai sėkmingai įrašyti į failą!")


