# Z podanego zbioru danych wyselekcjonuj 5 o największej wartości na jednostkę, znając kategorię obiektu
# Dane znajdują się w folderze "dane" w pliku "zbiór_wejściowy.json" oraz "kategorie.json"
# Wynik przedstaw w czytelnej formie na standardowym wyjściu
import json

# Nie wiem czy "Z podanego zbioru danych wyselekcjonuj 5 o największej wartości na jednostkę" 
# oznacza 1. najdroższe na uncję (bez uwzględnienia masy) czy 2. cenę jednostkową klejnotu
z = 0 # w przypadku 1. opcji (bez uwzględnienia masy) zmienić wartość zmiennej 'z' na 1

g_na_uncje = 0.03527396195
ct_na_uncje = 0.0070548

if z == 0:
    klucz = 'Wartość (USD)'
else:
    klucz = 'Wartość za uncję (USD)'

with open('..\\dane\\kategorie.json', encoding='utf-8') as file:
    kategorie = json.load(file)

with open('..\\dane\\zbiór_wejściowy.json', encoding='utf-8') as file:
    dane = json.load(file)

def Znajdz(x,y):
    for kategoria in kategorie:
        if kategoria['Typ']==x and kategoria['Czystość']==y:
            return float(kategoria['Wartość za uncję (USD)'])
    return 0

for klejnot in dane:
    if(wartosc:=Znajdz(klejnot['Typ'],klejnot['Czystość'])):
        if 'ct' in klejnot['Masa']:
            masa = float(klejnot['Masa'].replace('ct','').replace(',','.'))
            przelicznik = ct_na_uncje
        else:
            masa = float(klejnot['Masa'].replace('g','').replace(',','.'))
            przelicznik = g_na_uncje
        klejnot['Wartość (USD)'] = masa * wartosc * przelicznik
        klejnot['Wartość za uncję (USD)'] = wartosc
    else:
        klejnot['Wartość (USD)'] = 0
        klejnot['Wartość za uncję (USD)'] = 0
dane.sort(key=lambda x: x[klucz], reverse=True)

print(f"\033[1m\033[31m{klucz:<{len(klucz)+5}} {'Typ':<15} {'Masa':<15} {'Czystość':<15} {'Barwa':<15} {'Pochodzenie':<15} {'Właściciel':<25}\033[0m")
print('\033[1m\033[31m-\033[0m' * (len(klucz)+30+17*5))
for klejnot in dane[:5]:
    print(f"{klejnot[klucz]:<{len(klucz)+5}.2f} {klejnot['Typ']:<15} {klejnot['Masa']:<15} {klejnot['Czystość']:<15} {klejnot['Barwa']:<15} {klejnot['Pochodzenie']:<15} {klejnot['Właściciel']:<25}")
