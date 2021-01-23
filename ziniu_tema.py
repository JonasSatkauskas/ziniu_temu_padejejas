"""Ši programa padės išsirinkti temą. Pagal tą temą išsirinksit straipsnį.
Realiai ji skirta tiem kurie kartais negali apsispręsti ką paskaityti.
Kategorijos surastos iš svetainės www.15min.lt"""

import random
import time

galimos_temos = ['Lietuva', 'Užsienis', 'Verslas', 'Sportas', 'Gyvenimas',
                 'Gazas', 'Kultūra', 'Maistas', 'Mokslas.IT', 'Koronavirusas',
                 'Pasaulis kišenėje', 'Sveikata', 'Laisvalaikis', 'Ar žinai?',
                 'Tyrimai']

isrinkta = random.choice(galimos_temos)

while True:
    input("Spauskite ENTER, kad programa parinktų temą")
    time.sleep(1)
    print('\nGalvoju...')
    time.sleep(1)
    print('\nRenkuosi...')
    time.sleep(2)
    print(f'\nTema kurios straipsnį siūlau paskaityti yra: {isrinkta}')
    break

