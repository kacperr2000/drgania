# To jest program sterujacy.

import sys

print(70 * '-')
print('Ten program zajmuje sie modelowaniem ruchu drgajacego.\n')
print('Obslugiwane sa trzy podstawowe postacie drgan:\n')
print('drgania swobodne, drgania tlumione i drgania wymuszone.\n')
print(70 * '-')
print('Jaka postac drgan chcesz rozpatrzec?\n')
print('Nacisnij 1 jezeli wybierasz drgania swobodne.\n')
print('Nacisnij 2 jezeli wybierasz drgania tlumione.\n')
print('Nacisnij 3 jezeli wybierasz drgania wymuszone.\n')

wybor = input()

if wybor != '1' and wybor != '2' and wybor != '3':
    print('Podano niewlasciwy znak/znaki. Dozwolone sa tylko 1, 2 lub 3.\n')
    print('Dzialanie programu zostalo przerwane.\n')
    sys.exit(0)

else:
    w = int(wybor)
    if w == 1:
        print(70 * '-')
        print('Wybrano drgania swobodne.\n')
        print('Nastepny krok to podanie niezbednych parametrow.\n')
        print('Uwaga 1!: W celu uzyskania poprawnych rezultatow nalezy wszystkie wartosci podac w podstawowych'
              ' jednostkach ukladu SI.\n')
        print('Analiza przeprowadzana jest dla wychylenia w metrach.\n')
        print('Wartosci o nieodpowiednich jednostkach uzytkownik podaje na wlasna odpowiedzialnosc.\n')
        print('W takim wypadku reinterpretacja pozostawiana jest użytkownikowi.\n')
        print('Uwaga 2!: Wartosci "ekstremalne" uzytkownik podaje rowniez na wlasna odpowiedzialnosc.\n')
        print('Wykresy moga "dziwnie" sie zachowywac np. dla masy 1000 kg.')
        print(70 * '-')
        print('Podaj wychylenie poczatkowe(w metrach): \n')
        wych_pocz = input()
        try:
            w_pocz = float(wych_pocz)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        print('Podaj predkosc poczatkowa(w m/s): \n')
        pred_pocz = input()
        try:
            p_pocz = float(pred_pocz)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        print('Podaj mase(w kg): \n')
        masa = input()
        try:
            m = float(masa)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        if m <= 0:
            print('Masa musi byc dodatnia.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        else:
            m = m

        print('Podaj wspolczynnik sprezystosci/proporcjonalnosci wychylenia: \n')
        wsp_spr = input()
        try:
            w_spr = float(wsp_spr)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        if w_spr <= 0:
            print('Nalezy podac dodatni wspolczynnik sprezystosci/proporcjonalnosci wychylenia.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        else:
            w_spr = w_spr

        # drg_swobodne(w_pocz, p_pocz, m, w_spr)

    elif w == 2:
        print(70 * '-')
        print('Wybrano drgania tlumione.\n')
        print('Nastepny krok to podanie niezbednych parametrow.\n')
        print('Uwaga 1!: W celu uzyskania poprawnych rezultatow nalezy wszystkie wartosci podac w podstawowych'
              ' jednostkach ukladu SI.\n')
        print('Analiza przeprowadzana jest dla wychylenia w metrach.\n')
        print('Wartosci o nieodpowiednich jednostkach uzytkownik podaje na wlasna odpowiedzialnosc.\n')
        print('W takim wypadku reinterpretacja pozostawiana jest użytkownikowi.\n')
        print('Uwaga 2!: Wartosci "ekstremalne" uzytkownik podaje rowniez na wlasna odpowiedzialnosc.\n')
        print('Wykresy moga "dziwnie" sie zachowywac np. dla masy 1000 kg.')
        print(70 * '-')
        print('Podaj wychylenie poczatkowe(w metrach): \n')
        wych_pocz = input()
        try:
            w_pocz = float(wych_pocz)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        print('Podaj predkosc poczatkowa(w m/s): \n')
        pred_pocz = input()
        try:
            p_pocz = float(pred_pocz)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        print('Podaj mase(w kg): \n')
        masa = input()
        try:
            m = float(masa)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        if m <= 0:
            print('Masa musi byc dodatnia.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        else:
            m = m

        print('Podaj wspolczynnik sprezystosci/proporcjonalnosci wychylenia: \n')
        wsp_spr = input()
        try:
            w_spr = float(wsp_spr)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        if w_spr <= 0:
            print('Nalezy podac dodatni wspolczynnik sprezystosci/proporcjonalnosci wychylenia.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        else:
            w_spr = w_spr

        print('Podaj wspolczynnik proporcjonalnosci tlumienia.')
        wsp_tl = input()
        try:
            w_tl = float(wsp_tl)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        if w_tl <= 0:
            print('Nalezy podac dodatni wspolczynnik proporcjonalnosci tlumienia.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        else:
            w_tl = w_tl

        # drg_tlumione(w_pocz, p_pocz, m, w_spr, w_tl)

    elif w == 3:
        print(70 * '-')
        print('Wybrano drgania wymuszone.\n')
        print('Nastepny krok to podanie niezbednych parametrow.\n')
        print('Uwaga 1!: Rozwazany bedzie tylko ruch po wygasnieciu tlumienia (z czestoscia wymuszajaca).\n')
        print('Uwaga 2!: W celu uzyskania poprawnych rezultatow nalezy wszystkie wartosci podac w podstawowych'
              ' jednostkach ukladu SI.\n')
        print('Analiza przeprowadzana jest dla wychylenia w metrach.\n')
        print('Wartosci o nieodpowiednich jednostkach uzytkownik podaje na wlasna odpowiedzialnosc.\n')
        print('W takim wypadku reinterpretacja pozostawiana jest użytkownikowi.\n')
        print('Uwaga 3!: Wartosci "ekstremalne" uzytkownik podaje rowniez na wlasna odpowiedzialnosc.\n')
        print('Wykresy moga "dziwnie" sie zachowywac np. dla masy 1000 kg.')
        print(70 * '-')
        print('Podaj mase(w kg): \n')
        masa = input()
        try:
            m = float(masa)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        if m <= 0:
            print('Masa musi byc dodatnia.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        else:
            m = m

        print('Podaj wspolczynnik sprezystosci/proporcjonalnosci wychylenia: \n')
        wsp_spr = input()
        try:
            w_spr = float(wsp_spr)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        if w_spr <= 0:
            print('Nalezy podac dodatni wspolczynnik sprezystosci/proporcjonalnosci wychylenia.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        else:
            w_spr = w_spr


# print(w_pocz + p_pocz)








