# To jest modul z funkcjami

import numpy as np
import matplotlib.pyplot as plt
import sys


def drg_swobodne(x_0, v_0, m, k):
    """
    Funkcja po przyjeciu wymaganych parametrow i warunkow poczatkowych
    generuje wykres polozenia od czasu dla drgan swobodnych.

    :param x_0:
    :param v_0:
    :param m:
    :param k:
    :return:
    """
    # Obliczenia podstawowych wielkosci:
    omega_0 = np.sqrt(k/m)
    period = 2 * np.pi / omega_0
    freq = 1 / period

    if x_0 != 0 and v_0 != 0:
        # Obliczenia:
        amplitude = np.sqrt(pow(x_0, 2) + pow((v_0/x_0), 2))
        fase_shift = (-1) * v_0 / (x_0 * omega_0)

        # Wyswietlanie:
        print('Amplituda drgan wynosi: %f m.\n' % np.abs(amplitude))
        print('Przesuniecie fazowe wynosi: %f rad.\n' % fase_shift)
        print('Okres drgan wynosi: %f s.\n' % period)
        print('Czestotliowsc drgan wynosi: %f Hz.\n' % freq)

        # Zapis do pliku:
        """
        plik = open('dane_drg_swb.doc', 'w')
        plik.write('Amplituda drgan wynosi: %f m\n' % np.abs(amplitude))
        plik.write('Przesuniecie fazowe wynosi: %f rad\n' % fase_shift)
        plik.write('Okres drgan wynosi: %f s\n' % period)
        plik.write('Czestotliowsc drgan wynosi: %f Hz\n' % freq)
        plik.close()
        """

        # Generowanie wykresu:
        t = np.linspace(0, 50, 500)
        x = amplitude * np.cos(omega_0 * t + fase_shift)
        plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = Acos(wt+q)')
        plt.legend(loc='upper right')
        plt.xlabel('t', fontsize=8)
        plt.xticks(np.arange(0, 51, step=2))
        plt.ylabel('f(t)', fontsize=8)
        plt.grid(True)
        plt.title('Wykres funkcji drgań swobodnych postaci: Acos(wt+q)')
        # plt.savefig('drg_swob.png', dpi=72)
        plt.show()

    elif x_0 == 0 and v_0 != 0:
        # Obliczenia:
        amplitude = (-1) * v_0 / omega_0
        fase_shift = np.pi / 2

        # Wyswietlanie:
        print('Amplituda drgan wynosi: %f m\n' % np.abs(amplitude))
        print('Przesuniecie fazowe wynosi: %f rad\n' % fase_shift)
        print('Okres drgan wynosi: %f s\n' % period)
        print('Czestotliowsc drgan wynosi: %f Hz\n' % freq)

        # Zapis do pliku:
        """
        plik = open('dane_drg_swb.doc', 'w')
        plik.write('Amplituda drgan wynosi: %f m\n' % np.abs(amplitude))
        plik.write('Przesuniecie fazowe wynosi: %f rad\n' % fase_shift)
        plik.write('Okres drgan wynosi: %f s\n' % period)
        plik.write('Czestotliowsc drgan wynosi: %f Hz\n' % freq)
        plik.close()
        """

        # Generowanie wykresu:
        t = np.linspace(0, 50, 500)
        x = amplitude * np.cos(omega_0 * t + fase_shift)
        plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = Asin(wt)')
        plt.legend(loc='upper right')
        plt.xlabel('t', fontsize=8)
        plt.xticks(np.arange(0, 51, step=2))
        plt.ylabel('f(t)', fontsize=8)
        plt.grid(True)
        plt.title('Wykres funkcji drgań swobodnych postaci: Acos(wt+q)')
        # plt.savefig('drg_swob.png', dpi=72)
        plt.show()

    elif x_0 != 0 and v_0 == 0:
        # Obliczenia:
        amplitude = x_0
        fase_shift = 0

        # Wyswietlanie:
        print('Amplituda drgan wynosi: %f m\n' % np.abs(amplitude))
        print('Przesuniecie fazowe wynosi: %f rad\n' % fase_shift)
        print('Okres drgan wynosi: %f s\n' % period)
        print('Czestotliowsc drgan wynosi: %f Hz\n' % freq)

        # Zapis do pliku:
        """
        plik = open('dane_drg_swb.doc', 'w')
        plik.write('Amplituda drgan wynosi: %f m\n' % np.abs(amplitude))
        plik.write('Przesuniecie fazowe wynosi: %f rad\n' % fase_shift)
        plik.write('Okres drgan wynosi: %f s\n' % period)
        plik.write('Czestotliowsc drgan wynosi: %f Hz\n' % freq)
        plik.close()
        """

        # Generowanie wykresu:
        t = np.linspace(0, 50, 500)
        x = amplitude * np.cos(omega_0 * t + fase_shift)
        plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = Acos(wt)')
        plt.legend(loc='upper right')
        plt.xlabel('t', fontsize=8)
        plt.xticks(np.arange(0, 51, step=2))
        plt.ylabel('f(t)', fontsize=8)
        plt.grid(True)
        plt.title('Wykres funkcji drgań swobodnych postaci: Acos(wt+q)')
        # plt.savefig('drg_swob.png', dpi=72)
        plt.show()

    elif x_0 == 0 and v_0 == 0:
        # Obliczenia:
        amplitude = 0
        fase_shift = 0

        # Wyswietlanie:
        print('Amplituda drgan wynosi: %f m\n' % np.abs(amplitude))
        print('Przesuniecie fazowe wynosi: %f rad\n' % fase_shift)
        print('Okres drgan wynosi: %f s\n' % period)
        print('Czestotliowsc drgan wynosi: %f Hz\n' % freq)
        print('Nalezy miec na uwadze, ze przy zerowej amplitudzie okres czy czestotliwosc nie maja sensu fizycznego.\n')

        # Zapis do pliku:
        """
        plik = open('dane_drg_swb.doc', 'w')
        plik.write('Amplituda drgan wynosi: %f m\n' % np.abs(amplitude))
        plik.write('Przesuniecie fazowe wynosi: %f rad\n' % fase_shift)
        plik.write('Okres drgan wynosi: %f s\n' % period)
        plik.write('Czestotliowsc drgan wynosi: %f Hz\n' % freq)
        print('Nalezy miec na uwadze, ze przy zerowej amplitudzie okres czy czestotliwosc nie maja sensu fizycznego.\n')
        plik.close()
        """

        # Generowanie wykresu:
        t = np.linspace(0, 50, 500)
        x = amplitude * np.cos(omega_0 * t + fase_shift)
        plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = 0')
        plt.legend(loc='upper right')
        plt.xlabel('t', fontsize=8)
        plt.xticks(np.arange(0, 51, step=2))
        plt.ylabel('f(t)', fontsize=8)
        plt.grid(True)
        plt.title('Wykres funkcji drgań swobodnych postaci: Acos(wt+q)')
        # plt.savefig('drg_swob.png', dpi=72)
        plt.show()


def drg_tlumione(x_0, v_0, m, k, f):
    """
    Funkcja po przyjeciu wymaganych parametrow i warunkow poczatkowych
    generuje wykres polozenia od czasu dla drgan tlumionych.

    :param x_0:
    :param v_0:
    :param m:
    :param k:
    :param f:
    :return:
    """
    # Obliczenia podstawowych wielkosci:
    omega_0 = np.sqrt(k / m)
    period_0 = 2 * np.pi / omega_0
    freq_0 = 1 / period_0
    beta = f / (2 * m)
    tau = 1 / beta

    if np.power(omega_0, 2) > np.power(beta, 2):
        # Obliczenia:
        omega = np.sqrt(np.power(omega_0, 2) - np.power(beta, 2))
        period = 2 * np.pi / omega
        freq = 1 / period
        log_dec = beta * period

        if x_0 != 0 and v_0 != 0:
            # Obliczenia:
            fase_shift = np.arctan(((-1) * beta * x_0 - v_0) / (x_0 * omega))
            amplitude = x_0 / np.cos(fase_shift)

            # Wyswietlanie najwazniejszych danych:
            print('Okres drgań swobodnych wynosi: %f s.\n' % period_0)
            print('Czestotliwosc drgan swobodnych wynosi: %f Hz.\n' % freq_0)
            print('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
            print('Czas relaksacji wynosi: %f s.\n' % tau)
            print('Okres drgan wynosi: %f s.\n' % period)
            print('Czestotliwosc drgan wynosi: %f Hz.\n' % freq)
            print('Przesuniecie fazowe wynosi: %f rad.\n' % fase_shift)
            print('Maksymalna amplituda wynosi: %f m.\n' % np.abs(amplitude))
            print('Logarytmiczny dekrement tlumienia wynosi: %f.\n' % log_dec)

            # Zapis do pliku:
            """
            plik = open('dane_drg_tl.doc', 'w')
            plik.write('Okres drgan swobodnych wynosi: %f s.\n' % period_0)
            plik.write('Czestotliwosc drgan swobodnych wynosi: %f Hz.\n' % freq_0)
            plik.write('\n')
            plik.write('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
            plik.write('Czas relaksacji wynosi: %f s.\n' % tau)
            plik.write('Okres drgan wynosi: %f s.\n' % period)
            plik.write('Czestotliwosc drgan wynosi: %f Hz.\n' % freq)
            plik.write('Przesuniecie fazowe wynosi: %f rad.\n' % fase_shift)
            plik.write('Maksymalna amplituda wynosi: %f m.\n' % np.abs(amplitude))
            plik.write('Logarytmiczny dekrement tlumienia wynosi: %f.\n' % log_dec)
            plik.close()
            """

            # Generowanie wykresu:
            t = np.linspace(0, 50, 500)
            x = amplitude * np.exp((-1) * beta * t) * np.cos(omega * t + fase_shift)
            plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = Aexp(-bt)cos(wt+q)')
            plt.legend(loc='upper right')
            plt.xlabel('t', fontsize=8)
            plt.xticks(np.arange(0, 51, step=2))
            plt.ylabel('f(t)', fontsize=8)
            plt.grid(True)
            plt.title('Wykres funkcji drgań tlumionych postaci: Aexp(-bt)cos(wt+q)')
            # plt.savefig('drg_tl.png', dpi=72)
            plt.show()

        elif x_0 == 0 and v_0 != 0:
            # Obliczenia:
            fase_shift = np.pi / 2
            amplitude = (-1) * v_0 / omega

            # Wyswietlanie najwazniejszych danych:
            print('Okres drgań swobodnych wynosi: %f s.\n' % period_0)
            print('Czestotliwosc drgan swobodnych wynosi: %f Hz.\n' % freq_0)
            print('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
            print('Czas relaksacji wynosi: %f s.\n' % tau)
            print('Okres drgan wynosi: %f s.\n' % period)
            print('Czestotliwosc drgan wynosi: %f Hz.\n' % freq)
            print('Przesuniecie fazowe wynosi: %f rad.\n' % fase_shift)
            print('Maksymalna amplituda wynosi: %f m.\n' % np.abs(amplitude))
            print('Logarytmiczny dekrement tlumienia wynosi: %f.\n' % log_dec)

            # Zapis do pliku:
            """
            plik = open('dane_drg_tl.doc', 'w')
            plik.write('Okres drgan swobodnych wynosi: %f s.\n' % period_0)
            plik.write('Czestotliwosc drgan swobodnych wynosi: %f Hz.\n' % freq_0)
            plik.write('\n')
            plik.write('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
            plik.write('Czas relaksacji wynosi: %f s.\n' % tau)
            plik.write('Okres drgan wynosi: %f s.\n' % period)
            plik.write('Czestotliwosc drgan wynosi: %f Hz.\n' % freq)
            plik.write('Przesuniecie fazowe wynosi: %f rad.\n' % fase_shift)
            plik.write('Maksymalna amplituda wynosi: %f m.\n' % np.abs(amplitude))
            plik.write('Logarytmiczny dekrement tlumienia wynosi: %f.\n' % log_dec)
            plik.close()
            """
            # Generowanie wykresu:
            t = np.linspace(0, 50, 500)
            x = amplitude * np.exp((-1) * beta * t) * np.cos(omega * t + fase_shift)
            plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = Aexp(-bt)sin(wt)')
            plt.legend(loc='upper right')
            plt.xlabel('t', fontsize=8)
            plt.xticks(np.arange(0, 51, step=2))
            plt.ylabel('f(t)', fontsize=8)
            plt.grid(True)
            plt.title('Wykres funkcji drgań tlumionych postaci: Aexp(-bt)cos(wt+q)')
            # plt.savefig('drg_tl.png', dpi=72)
            plt.show()

        elif x_0 != 0 and v_0 == 0:
            # Obliczenia:
            fase_shift = np.arctan((-1) * beta / omega)
            amplitude = x_0 / np.cos(fase_shift)

            # Wyswietlanie najwazniejszych danych:
            print('Okres drgań swobodnych wynosi: %f s.\n' % period_0)
            print('Czestotliwosc drgan swobodnych wynosi: %f Hz.\n' % freq_0)
            print('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
            print('Czas relaksacji wynosi: %f s.\n' % tau)
            print('Okres drgan wynosi: %f s.\n' % period)
            print('Czestotliwosc drgan wynosi: %f Hz.\n' % freq)
            print('Przesuniecie fazowe wynosi: %f rad.\n' % fase_shift)
            print('Maksymalna amplituda wynosi: %f m.\n' % np.abs(amplitude))
            print('Logarytmiczny dekrement tlumienia wynosi: %f.\n' % log_dec)

            # Zapis do pliku:
            """
            plik = open('dane_drg_tl.doc', 'w')
            plik.write('Okres drgan swobodnych wynosi: %f s.\n' % period_0)
            plik.write('Czestotliwosc drgan swobodnych wynosi: %f Hz.\n' % freq_0)
            plik.write('\n')
            plik.write('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
            plik.write('Czas relaksacji wynosi: %f s.\n' % tau)
            plik.write('Okres drgan wynosi: %f s.\n' % period)
            plik.write('Czestotliwosc drgan wynosi: %f Hz.\n' % freq)
            plik.write('Przesuniecie fazowe wynosi: %f rad.\n' % fase_shift)
            plik.write('Maksymalna amplituda wynosi: %f m.\n' % np.abs(amplitude))
            plik.write('Logarytmiczny dekrement tlumienia wynosi: %f.\n' % log_dec)
            plik.close()
            """
            # Generowanie wykresu:
            t = np.linspace(0, 50, 500)
            x = amplitude * np.exp((-1) * beta * t) * np.cos(omega * t + fase_shift)
            plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = Aexp(-bt)cos(wt+q)')
            plt.legend(loc='upper right')
            plt.xlabel('t', fontsize=8)
            plt.xticks(np.arange(0, 51, step=2))
            plt.ylabel('f(t)', fontsize=8)
            plt.grid(True)
            plt.title('Wykres funkcji drgań tlumionych postaci: Aexp(-bt)cos(wt+q)')
            # plt.savefig('drg_tl.png', dpi=72)
            plt.show()

        elif x_0 == 0 and v_0 == 0:
            # Obliczenia:
            fase_shift = np.arctan((-1) * beta / omega)
            amplitude = 0

            # Wyswietlanie najwazniejszych danych:
            print('Okres drgań swobodnych wynosi: %f s.\n' % period_0)
            print('Czestotliwosc drgan swobodnych wynosi: %f Hz.\n' % freq_0)
            print('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
            print('Czas relaksacji wynosi: %f s.\n' % tau)
            print('Okres drgan wynosi: %f s.\n' % period)
            print('Czestotliwosc drgan wynosi: %f Hz.\n' % freq)
            print('Przesuniecie fazowe wynosi: %f rad.\n' % fase_shift)
            print('Maksymalna amplituda wynosi: %f m.\n' % np.abs(amplitude))
            print('Logarytmiczny dekrement tlumienia wynosi: %f.\n' % log_dec)
            print('Nalezy miec na uwadze, ze przy zerowej amplitudzie okres czy czestotliwosc nie maja sensu fizycznego.\n')

            # Zapis do pliku:
            """
            plik = open('dane_drg_tl.doc', 'w')
            plik.write('Okres drgan swobodnych wynosi: %f s.\n' % period_0)
            plik.write('Czestotliwosc drgan swobodnych wynosi: %f Hz.\n' % freq_0)
            plik.write('\n')
            plik.write('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
            plik.write('Czas relaksacji wynosi: %f s.\n' % tau)
            plik.write('Okres drgan wynosi: %f s.\n' % period)
            plik.write('Czestotliwosc drgan wynosi: %f Hz.\n' % freq)
            plik.write('Przesuniecie fazowe wynosi: %f rad.\n' % fase_shift)
            plik.write('Maksymalna amplituda wynosi: %f m.\n' % np.abs(amplitude))
            plik.write('Logarytmiczny dekrement tlumienia wynosi: %f.\n' % log_dec)
            plik,write('Nalezy miec na uwadze, ze przy zerowej amplitudzie okres czy czestotliwosc nie maja sensu fizycznego.\n')
            plik.close()
            """
            # Generowanie wykresu:
            t = np.linspace(0, 50, 500)
            x = amplitude * np.exp((-1) * beta * t) * np.cos(omega * t + fase_shift)
            plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = 0')
            plt.legend(loc='upper right')
            plt.xlabel('t', fontsize=8)
            plt.xticks(np.arange(0, 51, step=2))
            plt.ylabel('f(t)', fontsize=8)
            plt.grid(True)
            plt.title('Wykres funkcji drgań tlumionych postaci: Aexp(-bt)cos(wt+q)')
            # plt.savefig('drg_tl.png', dpi=72)
            plt.show()

    elif np.power(omega_0, 2) == np.power(beta, 2):
        # Ruch aperiodyczny. Tlumienie krytyczne.
        # Obliczenia:
        A = x_0
        B = v_0 + beta * A

        # Wyswietlanie najwazniejszych danych:
        print('Przypadek tlumienia krytycznego.\n')
        print('Zaleznosc x(t) ma postac: x(t) = (A + Bt)exp(-bt).\n')
        print('Stala A wynosi: %f m.\n' % A)
        print('Stala B wynosi %f m/s.\n' % B)
        print('Wspolczynnik tlumienia (jednoczesnie wartosc czestosci drgan wlasnych) wynosi: %f 1/s.\n' % beta)

        # Zapis do pliku:
        """
        plik = open('dane_drg_tl.doc', 'w')
        plik.write('Przypadek tlumienia krytycznego.\n')
        plik.write('Zaleznosc x(t) ma postac: x(t) = (A + Bt)exp(-bt).\n')
        plik.write('Stala A wynosi: %f m.\n' % A)
        plik.write('Stala B wynosi %f m/s.\n' % B)
        plik.write('Wspolczynnik tlumienia (jednoczesnie wartosc czestosci drgan wlasnych) wynosi: %f 1/s.\n' % beta)
        plik.close()
        """

        # Generowanie wykresu:
        t = np.linspace(0, 50, 500)
        x = (A + B * t) * np.exp((-1) * beta * t)

        if A != 0 and B != 0:
            plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = (A + Bt)exp(-bt)')

        elif A == 0 and B != 0:
            plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = Btexp(-bt)')

        elif A != 0 and B == 0:
            plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = Aexp(-bt)')

        elif A == 0 and B == 0:
            plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = 0')

        plt.legend(loc='upper right')
        plt.xlabel('t', fontsize=8)
        plt.xticks(np.arange(0, 51, step=2))
        plt.ylabel('f(t)', fontsize=8)
        plt.grid(True)
        plt.title('Wykres funkcji drgań tlumionych postaci: (A + Bt)exp(-bt)')
        # plt.savefig('drg_tl.png', dpi=72)
        plt.show()

    elif np.power(omega_0, 2) < np.power(beta, 2):
        # Ruch aperiodyczny. Drgania przetlumione.
        # Obliczenia:
        pseudo_omega = np.sqrt(np.power(beta, 2) - np.power(omega_0, 2))
        A = (v_0 + x_0 * (beta + pseudo_omega)) / (2 * pseudo_omega)
        B = x_0 - A

        # Wyswietlanie najwazniejszych danych:
        print('Przypadek drgan przetlumionych.\n')
        print('Zaleznosc x(t) ma postac: x(t) = exp(-bt)(Aexp(wt) + Bexp(-wt)).\n')
        print('w = (b^2 - w_0^2) ^ (1/2).\n')
        print('Stala A wynosi: %f m.\n' % A)
        print('Stala B wynosi %f m.\n' % B)
        print('Czestosc wlasna ukladu wynosi: %f 1/s.\n' % omega_0)
        print('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
        print('Pseudo-czestosc drgan (taka czestosc mialyby drgania gdyby mogly zajsc) wynosi: %f 1/s.\n' % pseudo_omega)

        # Zapis do pliku:
        """
        plik = open('dane_drg_tl.doc', 'w')
        plik.write('Przypadek drgan przetlumionych.\n')
        plik.write('Zaleznosc x(t) ma postac: x(t) = exp(-bt)(Aexp(wt) + Bexp(-wt)).\n')
        plik.write('w = (b^2 - w_0^2) ^ (1/2).\n')
        plik.write('Stala A wynosi: %f m.\n' % A)
        plik.write('Stala B wynosi %f m.\n' % B)
        plik.write('Czestosc wlasna ukladu wynosi: %f 1/s.\n' % omega_0)
        plik.write('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
        plik.write('Pseudo-czestosc drgan (taka czestosc mialyby drgania gdyby mogly zajsc) wynosi: %f 1/s.\n' % pseudo_omega)
        plik.close()
        """

        # Generowanie wykresu:
        t = np.linspace(0, 50, 500)
        x_1 = np.exp((-1) * beta * t)
        x_2 = (A * np.exp(pseudo_omega * t))
        x_3 = (B * np.exp((-1) * pseudo_omega * t))
        x = x_1 * (x_2 + x_3)

        if A != 0 and B != 0:
            plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = exp(-bt)[Aexp(wt) + Bexp(wt)]')

        elif A == 0 and B != 0:
            plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = Bexp(-bt)exp(wt)')

        elif A != 0 and B == 0:
            plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = Aexp(-bt)exp(wt)')

        elif A == 0 and B == 0:
            plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = 0')

        plt.legend(loc='upper right')
        plt.xlabel('t', fontsize=8)
        plt.xticks(np.arange(0, 51, step=2))
        plt.ylabel('f(t)', fontsize=8)
        plt.grid(True)
        plt.title('Wykres funkcji drgań tlumionych postaci: exp(-bt)[Aexp(wt) + Bexp(wt)]')
        # plt.savefig('drg_tl.png', dpi=72)
        plt.show()


def drg_wymuszone(m, k, f, force_0, omega):
    """
    Funkcja po przyjeciu wymaganych parametrow generuje wykres
    polozenia od czasu dla drgan wymuszonych.

    :param m:
    :param k:
    :param f:
    :param force_0:
    :param omega:
    :return:
    """
    # Obliczenia podstawowych wielkosci:
    omega_0 = np.sqrt(k / m)
    period_0 = 2 * np.pi / omega_0
    freq_0 = 1 / period_0
    beta = f / (2 * m)
    pseudo_omega = np.power(omega_0, 2) - np.power(omega, 2)
    z = np.sqrt(np.power(pseudo_omega, 2) + 4 * np.power(beta, 2) * np.power(omega, 2))
    pre_omega_r = np.power(omega_0, 2) - 2 * np.power(beta, 2)
    if pre_omega_r < 0:
        omega_r = 0
        period_r = 0
        freq_r = 0

    else:
        omega_r = np.sqrt(pre_omega_r)
        period_r = 2 * np.pi / omega_r
        freq_r = 1 / period_r

    if beta != 0 or (beta == 0 and np.power(omega_0, 2) != np.power(omega, 2)):
        # Obliczenia:
        amplitude = force_0 / (omega * z)
        imped = np.sqrt(np.power(f, 2) + np.power((m * omega - k / omega), 2))
        a_ab = 2 * force_0 * beta * m / (omega * np.power(imped, 2))
        a_el = force_0 * m * (np.power(omega_0, 2) - np.power(omega, 2)) / (np.power(imped, 2) * np.power(omega, 2))

        # Wyswietlanie najwazniejszych danych:
        print('Amplituda drgan wynosi: %f m.\n' % np.abs(amplitude))
        print('Okres drgan wlasnych wynosi: %f s.\n' % period_0)
        print('Czestotliwosc drgan wlasnych wynosi: %f 1/s.\n' % freq_0)
        print('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
        if pre_omega_r < 0:
            print('Czestosc rezonansowa nieokreslona.\n')
            print('Czestotliwosc rezonansowa nieokreslona.\n')

        else:
            print('Czestosc rezonansowa wynosi: %f 1/s.\n' % omega_r)
            print('Czestotliwosc rezonansowa wynosi: %f Hz.\n' % freq_r)

        print('Impedancja mechaniczna wynosi: %f kg/s.\n' % imped)
        print('Amplituda absorpcyjna wynosi: %f m.\n' % np.abs(a_ab))
        print('Amplituda elastyczna wynosi: %f m.\n' % np.abs(a_el))

        # Zapis do pliku:
        """
        plik = open('dane_drg_wym.doc', 'w')
        plik.write('Amplituda drgan wynosi: %f m.\n' % np.abs(amplitude))
        plik.write('Okres drgan wlasnych wynosi: %f s.\n' % period_0)
        plik.write('Czestotliwosc drgan wlasnych wynosi: %f 1/s.\n' % freq_0)
        plik.write('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
        if pre_omega_r < 0:
            plik.write('Czestosc rezonansowa nieokreslona.\n')
            plik.write('Czestotliwosc rezonansowa nieokreslona.\n')
            
        else:
            plik.write('Czestosc rezonansowa wynosi: %f 1/s.\n' % omega_r)
            plik.write('Czestotliwosc rezonansowa wynosi: %f Hz.\n' % freq_r)
        
        plik.write('Czestosc rezonansowa wynosi: %f 1/s.\n' % omega_r)
        plik.write('Czestotliwosc rezonansowa wynosi: %f Hz.\n' % freq_r)
        plik.write('Impedancja mechaniczna wynosi: %f kg/s.\n' % imped)
        plik.write('Amplituda absorpcyjna wynosi: %f m.\n' % np.abs(a_ab))
        plik.write('Amplituda elastyczna wynosi: %f m.\n' % np.abs(a_el))
        plik.close()
        """

        # Generowanie wykresow. Wykresy postaci drgan i zaleznosci amplitud od czestotliwosci:
        t = np.linspace(0, 50, 500)
        x = amplitude * np.cos(omega * t)
        om_space = np.linspace(0.2, 50, 500)
        im_space = np.sqrt(np.power(f, 2) + np.power((m * om_space - k / om_space), 2))
        a_ab_space = 2 * force_0 * beta * m / (om_space * np.power(im_space, 2))
        a_el_space = force_0 * m * (np.power(omega_0, 2) - np.power(om_space, 2)) / (np.power(im_space, 2) * np.power(om_space, 2))
        pseudo_omega_space = np.power(omega_0, 2) - np.power(om_space, 2)
        z_space = np.sqrt(np.power(pseudo_omega_space, 2) + 4 * np.power(beta, 2) * np.power(om_space, 2))
        amplitude_space = force_0 / (om_space * z_space)

        plt.subplot(211)
        plt.plot(t, x, color='r', lw=1, ls='-', label='f(x) = Acos(wt)')
        plt.legend(loc='upper right')
        plt.xlabel('t', fontsize=8)
        plt.xticks(np.arange(0, 51, step=2))
        plt.ylabel('f(t)', fontsize=8)
        plt.grid(True)
        plt.title('Wykres funkcji drgań wymuszonych postaci: Acos(wt)')
        plt.subplot(212)
        plt.plot(om_space, a_ab_space, color='r', lw=1, ls='-', label='Aab = 2Fbm/wZ^2')
        plt.plot(om_space, a_el_space, color='b', lw=1, ls='-.', label='Ael = Fm(w0^2-w^2)/(Zw)^2')
        plt.plot(om_space, amplitude_space, color='g', lw=2, ls='--', label='A = F/Zw')
        plt.legend(loc='upper right')
        plt.xlabel('omega(czestosc sily wymuszajacej)', fontsize=8)
        plt.xticks(np.arange(0, 51, step=2))
        plt.ylabel('A (wartosc wychylenia z polozenia rownowagi)', fontsize=8)
        plt.grid(True)
        plt.title('Wykresy zaleznosci amplitudy absorbcyjnej, elastycznej i "glownej" od czestosci sily wymuszajacej.')
        # plt.savefig('drg_tl.png', dpi=72)
        plt.show()

    elif beta == 0 and np.power(omega_0, 2) == np.power(omega, 2):
        # Obliczenia:
        imped = np.sqrt(np.power(f, 2) + np.power((m * omega - k / omega), 2))

        # Wyswietlanie najwazniejszych danych:
        print('Okres drgan wlasnych wynosi: %f s.\n' % period_0)
        print('Czestotliwosc drgan wlasnych wynosi: %f 1/s.\n' % freq_0)
        print('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
        if pre_omega_r < 0:
            print('Czestosc rezonansowa nieokreslona.\n')
            print('Czestotliwosc rezonansowa nieokreslona.\n')

        else:
            print('Czestosc rezonansowa wynosi: %f 1/s.\n' % omega_r)
            print('Czestotliwosc rezonansowa wynosi: %f Hz.\n' % freq_r)

        print('Impedancja mechaniczna wynosi: %f kg/s.\n' % imped)
        print('Amplituda dąży do nieskończoności.\n')
        print('Amplitudy absorbcyjna i elastyczna również.\n')

        # Zapis do pliku:
        """
        plik = open('dane_drg_wym.doc', 'w')
        plik.write('Okres drgan wlasnych wynosi: %f s.\n' % period_0)
        plik.write('Czestotliwosc drgan wlasnych wynosi: %f 1/s.\n' % freq_0)
        plik.write('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)
        if pre_omega_r < 0:
            plik.write('Czestosc rezonansowa nieokreslona.\n')
            plik.write('Czestotliwosc rezonansowa nieokreslona.\n')
            
        else:
            plik.write('Czestosc rezonansowa wynosi: %f 1/s.\n' % omega_r)
            plik.write('Czestotliwosc rezonansowa wynosi: %f Hz.\n' % freq_r) 
        
        plik.write('Czestosc rezonansowa wynosi: %f 1/s.\n' % omega_r)
        plik.write('Czestotliwosc rezonansowa wynosi: %f Hz.\n' % freq_r)
        plik.write('Impedancja mechaniczna wynosi: %f kg/s.\n' % imped)
        plik.write('Amplituda dąży do nieskończoności.\n')
        plik.write('Amplitudy absorbcyjna i elastyczna również.\n')
        plik.close()
        """
        # Generowanie wykresow. Wykresy zaleznosci amplitud od czestotliwosci:
        om_space = np.linspace(0.2, 50, 500)
        im_space = np.sqrt(np.power(f, 2) + np.power((m * om_space - k / om_space), 2))
        a_ab_space = 2 * force_0 * beta * m / (om_space * np.power(im_space, 2))
        a_el_space = force_0 * m * (np.power(omega_0, 2) - np.power(om_space, 2)) / (np.power(im_space, 2) * np.power(om_space, 2))
        pseudo_omega_space = np.power(omega_0, 2) - np.power(om_space, 2)
        z_space = np.sqrt(np.power(pseudo_omega_space, 2) + 4 * np.power(beta, 2) * np.power(om_space, 2))
        amplitude_space = force_0 / (om_space * z_space)

        plt.plot(om_space, a_ab_space, color='r', lw=1, ls='-', label='Aab = 2Fbm/wZ^2')
        plt.plot(om_space, a_el_space, color='b', lw=1, ls='-.', label='Ael = Fm(w0^2-w^2)/(Zw)^2')
        plt.plot(om_space, amplitude_space, color='g', lw=2, ls='--', label='A = F/Zw')
        plt.legend(loc='upper right')
        plt.xlabel('omega(czestosc sily wymuszajacej)', fontsize=8)
        plt.xticks(np.arange(0, 51, step=2))
        plt.ylabel('A (wartosc wychylenia z polozenia rownowagi)', fontsize=8)
        plt.grid(True)
        plt.title('Wykresy zaleznosci amplitudy absorbcyjnej, elastycznej i glownej od czestosci sily wymuszajacej.')
        # plt.savefig('drg_tl.png', dpi=72)
        plt.show()


def dod_drgan():
    """
    Ta funkcja pobiera od uzytkownika dlugosc struny oraz parametry wybranej
    liczby fal stacjonarnych po czym sumuje je modelujac ksztalt powstalego
    zaburzenia na strunie.

    :return:
    """
    print(70 * '-')
    print('Ta funkcja dodaje do siebie fale stacjonarne na strunie o wybranej dlugosci.\n')
    print('Na poczatku nalezy podac niezbedne dane.\n')
    print(70 * '-')

    # Zbieranie wymaganych parametrow
    print('Podaj dlugosc struny(w m):\n')
    print('Uwaga! Struna moze miec maksymalnie 3m.\n')
    dlugosc = input()
    try:
        dl = float(dlugosc)

    except ValueError:
        print('Niewlasciwy typ danych.\n')
        print('Dzialanie programu zostalo przerwane.\n')
        sys.exit(0)

    if dl <= 0:
        print('Dlugosc musi byc dodatnia.\n')
        print('Dzialanie programu zostalo przerwane.\n')
        sys.exit(0)

    elif dl > 3:
        print('Niepoprawna dlugosc struny.\n')
        print('Struna nie powinna byc dluzsza niz 3 metry.\n')
        print('Dzialanie programu zostalo przerwane.\n')
        sys.exit(0)

    else:
        dl = dl

    print('Nastepnie nalezy wybrac ilosc skladanych fal.\n')
    print('Ile fal chcesz zlozyc?:\n')
    print('uwaga! Maksymalnie mozesz zlozyc 20 fal.\n')
    liczba = input()
    try:
        li = int(liczba)

    except ValueError:
        print('Niewlasciwy typ danych.\n')
        print('Dzialanie programu zostalo przerwane.\n')
        sys.exit(0)

    if li <= 0:
        print('Wybrana ilosc musi byc liczba dodatnia.\n')
        print('Dzialanie programu zostalo przerwane.\n')
        sys.exit(0)

    elif li > 20:
        print('Niepoprawna ilosc fal.\n')
        print('Program sklada maksymalnie 20 fal.\n')
        print('Dzialanie programu zostalo przerwane.\n')
        sys.exit(0)

    else:
        li = li

    am_lim = 0.2 * dl
    amplitudy = []
    l_falowe = []
    prz_fazowe = []
    for i in range(li):
        print('Podaj parametry %i fali:\n' % (i + 1))
        print('Podaj amplitude(w m):\n')
        print('Uwaga! Amplituda moze miec maksymalnie %f m.\n' % am_lim)
        amplituda = input()
        try:
            am = float(amplituda)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        if am <= 0:
            print('Amplituda musi byc liczba dodatnia.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        elif am > am_lim:
            print('Niepoprawna wartosc amplitudy.\n')
            print('Maksymalna amplituda musi miec maksymalnie %f metra.\n' % am_lim)
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        else:
            amplitudy.append(am)

        print('Podaj liczbe falowa(w 1/m):\n')
        print('Uwaga! Liczba falowa moze wynosic maksymalnie 15 1/m.\n')
        l_fal = input()
        try:
            l_f = float(l_fal)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        if l_f <= 0:
            print('Liczba falowa musi byc liczba dodatnia.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        elif l_f > 15:
            print('Niepoprawna wartosc liczby falowej.\n')
            print('Wartosc liczby falowej musi miec maksymalnie 15 1/m.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        else:
            l_falowe.append(l_f)

        print('Podaj przesuniecie fazowe(w rad):\n')
        p_fazowe = input()
        try:
            p_f = float(p_fazowe)

        except ValueError:
            print('Niewlasciwy typ danych.\n')
            print('Dzialanie programu zostalo przerwane.\n')
            sys.exit(0)

        p_f = p_f
        prz_fazowe.append(p_f)

    # Generowanie wykresu
    x = np.linspace(0, dl, 500)
    # print(x)
    y = 0
    for i in range(li):
        y += amplitudy[i] * np.cos(l_falowe[i] * x + prz_fazowe[i])

    plt.plot(x, y, color='r', lw=1, ls='-', label='f(x) = A1*cos(k1*t+q1) + ... + An*cos(kn*t+qn)')
    plt.legend(loc='upper right')
    plt.xlabel('x', fontsize=8)
    plt.ylabel('f(x)', fontsize=8)
    plt.grid(True)
    plt.title('Suma danych fal na strunie o dlugości %f m.' % dl)
    # plt.savefig('skl_drgan.png', dpi=72)
    plt.show()


