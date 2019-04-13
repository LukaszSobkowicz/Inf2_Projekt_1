# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:15:06 2019

@author: S291432@Lab400
"""
#dodaj label pod komentarz
def PktPrzec(XA, YA, XB, YB, XC, YC, XD, YD):
    """
    Obliczenie współrzędnych punktu przecięcia dwóch linii
    :param XA: float | współrzędne końców linii
    :param YA: float
    :param XB: float
    :param YB: float
    :param XC: float
    :param YC: float
    :param XD: float
    :param YD: float
    :return: 
    komentarz: str | Położenie punktu względem linii
    XP: float | Współrzędne punktu przecięcia
    YP: float
    """

    dXAB = XB - XA
    dYAB = YB - YA
    dXCD = XD - XC
    dYCD = YD - YC
    dXAC = XC - XA
    dYAC = YC - YA
    
    M = dXAB*dYCD - dYAB*dXCD
    
    x1 = [XA, XB]
    y1 = [YA, YB]
    
    x2 = [XC, XD]
    y2 = [YC, YD]

    if int(M) == 0:
        komentarz = " proste są równoległe "
        XP = " brak "
        YP = " brak "
        return komentarz, XP, YP
    else:
        t1 = (dXAC*dYCD - dYAC*dXCD)/M
        t2 = (dXAC*dYAB - dYAC*dXAB)/M
    
        XP = "{:.3f}".format(XA + t1*dXAB)
        YP = "{:.3f}".format(YA + t1*dYAB)

        if 0 <= t1 <= 1 and 0 <= t2 <= 1:
            komentarz = " na przecięciu odcinków "
            return komentarz, XP, YP,
        elif (t1 > 1 or t1 < 0) and (t2 > 1 or t2 < 0):
            komentarz = " na przecięciu przedłużeń odcinków "
            return komentarz, XP, YP
        else:
            komentarz = " na przecięciu odcinka i przedłużenia "
            return komentarz, XP, YP


def dms(alpha):
    """
    Zamiana kątów w radianach na stopnie minuty sekundy
    :param alpha: float | kąt w radianach
    :return:
    beta: str | kąt w stopniach minutach sekundach
    """
    from math import pi

    i = 1
    z = ' '

    if alpha < 0:
        i = -1
        z = '-'

    f = abs(alpha)

    f = f * 180 / pi

    d = int(f)

    m = int(60 * (f - d))

    s = (f - d - m / 60) * 3600

    beta = '{:5} {:5} {:5.3f}'.format(d, m, s)
    return beta

def Azymut(XA, YA, XB, YB):
    """
    Obliczenie azymutu odcinka
    :param XA: float | współrzędne punktów początkowego i końcowego
    :param YA: float
    :param XB: float
    :param YB: float
    :return:
    azymut: str | azymut w kierunku głównym w stopniach minutach sekundach
    * Do poprawnego działania potrzebuje funkcji dms()
    """
    from math import atan, pi
    dx = (float(XB) - float(XA))
    dy = (float(YB) - float(YA))
    if (dx < 0 and dy < 0) or (dx < 0 and dy > 0):
        A = atan(dy / dx)
        Az = A + pi
        azymut = dms(Az)
    elif dx > 0 and dy < 0:
        A = atan(dy / dx)
        Az = A + 2 * pi
        azymut = dms(Az)
    elif dy == 0.0 and dx < 0.0:
        Az = pi
        azymut = dms(Az)
    elif dy == 0.0 and dx > 0.0:
        Az = 0.0
        azymut = dms(Az)
    elif dx == 0.0 and dy < 0.0:
        Az = 3/2*pi
        azymut = dms(Az)
    elif dx == 0.0 and dy > 0.0:
        Az = pi/2
        azymut = dms(Az)
    else:
        A = atan(dy / dx)
        Az = A
        azymut = dms(Az)
    return azymut


