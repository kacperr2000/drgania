# To jest modul z funkcjami

import numpy as np
import matplotlib.pyplot as plt

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
            plt.legend(loc='upper left')
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
            plt.legend(loc='upper left')
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
            plt.legend(loc='upper left')
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
            plt.legend(loc='upper left')
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
        A = (v_0 + x_0 * (beta + pseudo_omega)) / pseudo_omega
        B = x_0 - A

        # Wyswietlanie najwazniejszych danych:
        print('Przypadek drgan przetlumionych.\n')
        print('Zaleznosc x(t) ma postac: x(t) = exp(-bt)(Aexp(ht) + Bexp(-ht)).\n')
        print('h = (b^2 - w_0^2) ^ (1/2).')
        print('Stala A wynosi: %f m.\n' % A)
        print('Stala B wynosi %f m.\n' % B)
        print('Wspolczynnik tlumienia wynosi: %f 1/s.\n' % beta)


# drg_swobodne(0.02, 0.01425, 0.5, 0.5)
# drg_tlumione(0.78, 0.9, 1, 1, 3)




