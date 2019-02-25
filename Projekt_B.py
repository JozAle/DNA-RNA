import os  # Biblioteka umożliwiająca pracę z folderami.
import random  # Biblioteka umożliwiająca losowanie znaków DNA_strand.


def czytaj_plik(nazwa_pliku):  # Funkcja przyjmująca nazwę pliku tekstowego i zwracająca jego zawartość jako string.
    try:
        plik_tekstowy = open(nazwa_pliku)  # Otwarcie pliku
        tekst = plik_tekstowy.read()  # Czytanie linijka po linijce.
    except IOError:
        print("Nie udalo sie otworzyc pliku!")  # W razie wystąpienia błędu wypisuje na ekranie komunikat.
        tekst = ''  # Oraz zwraca pustą zmienną.
    return tekst


def zapisz_do_pliku(nazwa_pliku, obiekt):  # Funkcja zapisująca podany obiekt do pliku w podanej scieżce.
    try:
        if nazwa_pliku.find('/') > 0:  # Szukanie znaku '/' w nazwie pliku.
            if not os.path.isdir(nazwa_pliku[0:nazwa_pliku.find('/')]):
                os.mkdir(nazwa_pliku[0:nazwa_pliku.find('/')])  # Tworzenie folderu jeśli dany nie istnieje.
        plik_zapisu = open(nazwa_pliku, 'w')  # Otwarcie pliku do zapisu.
        if type(obiekt) == list:  # Sprawdzenie czy podany obiekt jest listą.
            for element in obiekt:
                plik_zapisu.write(str(element) + ' ')  # Zapisanie każdego elementu listy osobno.
        else:
            plik_zapisu.write(str(obiekt))  # Zapis obiektu ktory nie jest lista
        plik_zapisu.close()  # Zamkniecie pliku do zapisu
    except IOError:
        print("Nie udalo sie utworzyc pliku!")


def podzial_tekstu_na_wyrazy(tekst):
    wyrazy = tekst.replace('\n', ' ').replace('\t', ' ').split(' ')
    # Podzielenie podanego tekstu na wyrazy i usuniecie znakow '\n'oraz '\t'
    return wyrazy


assert podzial_tekstu_na_wyrazy('test\ndzialania\t') == ['test', 'dzialania', ''], 'Blad, zle dzieli na wyrazy!'


def dzielenie_na_prefiksy(wyrazy, najkrotsze_slowo):
    prefiksy = list()
    k = input("Prosze o podanie dlugosci prefiksu: ")
    while int(k) > len(
            najkrotsze_slowo):  # Sprawdzenie czy dlugosc prefiksow jest mniejsza od slugosci najkrotszego slowa
        k = input("Prosze o podanie dlugosci prefiksu krotszej lub rownej "
                  "dlugosci najkrotszego slowa rownej " + str(len(najkrotsze_slowo))
                  + ': ')
    for wyraz in wyrazy:  # Dzielenie kazdego wyrazu na prefiksy o wybranej dlugosci.
        prefiksy.append(wyraz[:int(k)])
    return prefiksy


def dzielenie_na_sufiksy(wyrazy, najkrotsze_slowo):
    sufiksy = list()
    k = input("Prosze o podanie dlugosci sufiksu: ")
    while int(k) > len(
            NajkrotszeSlowo):  # Sprawdzenie czy dlugosc sufiksow jest mniejsza od slugosci najkrotszego slowa.
        k = input("Prosze o podanie dlugosci sufiksu krotszej lub rownej "
                  "dlugosci najkrotszego slowa rownej " + str(len(najkrotsze_slowo))
                  + ': ')
    for wyraz in wyrazy:  # Dzielenie kazdego wyrazu na sufiksy o wybranej dlugosci.
        sufiksy.append(wyraz[len(wyraz) - int(k):len(wyraz)])
    return sufiksy


def porzadkowanie_alfabetyczne(wyrazy):
    wyrazy_posortowane = sorted(wyrazy)  # Sortowanie alfabetycznie.
    return wyrazy_posortowane


assert porzadkowanie_alfabetyczne(['Wojtek', 'Ala', 'Olek']) == ['Ala', 'Olek', 'Wojtek'], 'Blad, zle sortuje ' \
                                                                                         'alfabetycznie! '


def porzadkowanie_wzgledem_dlugosci_slow(wyrazy):
    wyrazy.sort(key=len)  # Sortowanie wzgledem dlugosci slow.
    return wyrazy


assert porzadkowanie_wzgledem_dlugosci_slow(['Wojtek', 'Ala', 'Olek']) == ['Ala', 'Olek', 'Wojtek'], 'Blad, zle ' \
                                                                                                     'sortuje ' \
                                                                                                     'wielkosciami! '


def tworzenie_nici(strand, zasady):
    # Tworzenie nowej nici na podstawie zasad podanych w slowniku podanym jako argument.
    complementary_strand = ''
    for nukleotyd in strand:
        complementary_strand += zasady[nukleotyd]
    return complementary_strand


assert tworzenie_nici('ATAT', {'A': 'T', 'T': 'A'}) == 'TATA', 'Blad, zle tworzy nic!'


def translacja(mrna, zasady):
    metionina_znaleziona = 0  # Flaga oznaczajaca czy znaleziono kodon start.
    stop_znaleziony = 0  # Flaga oznaczjaca czy znaleziono kodon stop po kodnie start.
    ciag_aminokwasow = []
    skrot = ''
    wynik_translacji = ''
    mrna = mrna.replace('\n', '')
    for i in range(1, len(mrna) + 1):  # Zbieranie trojek nukleotydow dla nici mRNA.
        if i % 3 == 0:
            skrot += mrna[i - 1]
            ciag_aminokwasow.append(zasady[skrot])
            skrot = ''
        else:
            skrot += mrna[i - 1]

    for aminokwas in ciag_aminokwasow:
        if aminokwas == 'Metionina':  # Dla kazdego aminokwasu, sprawdzenie czy jest kodonem start.
            metionina_znaleziona = 1
        if aminokwas == 'Stop' and metionina_znaleziona == 1:
            stop_znaleziony = 1  # Szukanie kodonu stop po znalezieniu kodonu start.
        if metionina_znaleziona != 0 and stop_znaleziony == 0:
            # Jesli kodon start znaleziony i stop nie znaleziony to zbiera znalezione aminokwasy.
            wynik_translacji += aminokwas + '\n'
        elif metionina_znaleziona != 0 and stop_znaleziony != 0:
            # Jesli znajdzie kodon stop to dopisuje go i konczy petle for.
            wynik_translacji += aminokwas + '\n'
            break
    return wynik_translacji


NazwaPliku = "TEKST.txt"
Tekst = czytaj_plik(NazwaPliku)  # Wczytanie pliku tekstowego.
Wyrazy = podzial_tekstu_na_wyrazy(Tekst)  # Podzielenie tekstu z pliku na wyrazy.
IloscWyrazow = len(Wyrazy)  # Obliczenie liczby wyrazow.
NajkrotszeSlowo = min(Wyrazy, key=len)  # Znalezienie najkrotszego slowa.
NajdluzszeSlowo = max(Wyrazy, key=len)  # Znalezienie najdluzszego slowa.
Prefiksy = dzielenie_na_prefiksy(Wyrazy, NajkrotszeSlowo)  # Zebranie prefiksow z wyrazow.
NapisZPrefiksow = ''.join(Prefiksy)  # Utworzenie napisu z prefiksow.
Sufiksy = dzielenie_na_sufiksy(Wyrazy, NajkrotszeSlowo)  # Zebranie sufiksow z wyrazow.
NapisZSufiksow = ''.join(Sufiksy)  # Utworzenie napisu z sufiksow
WyrazyPosortowaneAlfabetycznie = porzadkowanie_alfabetyczne(Wyrazy)  # Sortowanie alfabetyczne
WyrazyPosortowaneWzgledemDlugosci = porzadkowanie_wzgledem_dlugosci_slow(Wyrazy)  # Sortowanie wzgledem dlugosci.

# Zapisanie wynikow operacji do plikow.
zapisz_do_pliku('Sortowanie/WyrazyPosortowaneAlfabetycznie.txt', WyrazyPosortowaneAlfabetycznie)
zapisz_do_pliku('Sortowanie/WyrazyPosortowaneWzgledemDlugosci.txt', WyrazyPosortowaneWzgledemDlugosci)
zapisz_do_pliku('TworzenieNapisow/NapisZPrefiksow.txt', NapisZPrefiksow)
zapisz_do_pliku('TworzenieNapisow/NapisZSufiksow.txt', NapisZSufiksow)
zapisz_do_pliku('SlowaOSkrajnychDlugosciach/NajkrotszeSlowo.txt', NajkrotszeSlowo)
zapisz_do_pliku('SlowaOSkrajnychDlugosciach/NajdluzszeSlowo.txt', NajdluzszeSlowo)
zapisz_do_pliku('IloscWyrazow/IloscWyrazow.txt', IloscWyrazow)

DNA_strand = ''
Komplementarnosc = {
    'C': 'G',
    'G': 'C',
    'A': 'T',
    'T': 'A',
    '\n': '\n'
}

DNADoRNA = {
    'C': 'G',
    'G': 'C',
    'A': 'U',
    'T': 'A',
    '\n': '\n'
}

# Zebranie danych na temat kodonow z pliku tekstowego do slownika.
Translacja = {}
with open("KODONY.txt") as Plik:
    for Linia in Plik:
        (Klucz, Wartosc) = Linia.split()
        Translacja[str(Klucz)] = Wartosc

n = input('Prosze o podanie dlugosci DNA_strand: ')
n = int(n)
# Losowanie nukleotydow do DNA_strand.
for i in range(1, n + 1):
    Nukleotyd = random.choice(['A', 'T', 'C', 'G'])
    if i % 60 == 0:
        DNA_strand += Nukleotyd + '\n'
    else:
        DNA_strand += Nukleotyd
ComplementaryStrand = tworzenie_nici(DNA_strand, Komplementarnosc)  # Tworzenie nici komplementarnej do DNA_strand.
mRNA_strand = tworzenie_nici(ComplementaryStrand, DNADoRNA)  # Tworzenie nici mRNA.
# Sczytywanie aminokwasow dla 3 roznych pozycji startowych,
CiagAminokwasow1 = translacja(mRNA_strand, Translacja)
CiagAminokwasow2 = translacja(mRNA_strand[1:], Translacja)
CiagAminokwasow3 = translacja(mRNA_strand[2:], Translacja)

# Zapisywanie wynikow do plikow.
zapisz_do_pliku('DNA/DNA_strand.txt', DNA_strand)
zapisz_do_pliku('Komplementarna/NicKomplementarna.txt', ComplementaryStrand)
zapisz_do_pliku('Transkrypcja/mRNA.txt', mRNA_strand)
zapisz_do_pliku('Translacja/CiagAminokwasowOdPierwszegoNukleotydu.txt', CiagAminokwasow1)
zapisz_do_pliku('Translacja/CiagAminokwasowOdDrugiegoNukleotydu.txt', CiagAminokwasow2)
zapisz_do_pliku('Translacja/CiagAminokwasowOdTrzeciegoNukleotydu.txt', CiagAminokwasow3)