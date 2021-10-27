def citireLista():
    l = []
    givenString = input("dati lista de nr. intregi, despartite prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def citireLista3():
    l = []
    givenString = input("dati lista de nr. float, despartite prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(float(x))
    return l

def allAreDivByK(a: list[int], k: int):
    '''
    verifiva daca toate elementele dintr-o lista sunt divizibile cu k
    :param a: lista de nr. intregi
    :param k: un nr. intreg
    :return: True daca toate elementele din a sunt divizibile cu k,sau False in caz contrar
    '''
    if all([x % k == 0 for x in a]):
        return True
    else:
        return False

def testAllAreDiv():
    assert allAreDivByK([1, -3, 7, 2, -4], 2) is False
    assert allAreDivByK([3, -6, 27, -18, 9,], 3) is True

def get_longest_div_k(l: list[int], k: int):
    '''
    detrmina cea mai lunga subsecventa de numere care sunt divizibile cu k
    :param l: o lista de numere intregi
    :param k: un numar intreg
    :return: cea mai lunga subsecventa de numere care sunt divizibile cu k
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if allAreDivByK(l[i:j + 1], k) and len(l[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax

def test_get_longest_div_k():
    assert get_longest_div_k([-5, 5, 15, 25, 7, 8, -9, -15, 5, 35, 2, -46], 5) == [-5, 5, 15, 25]
    assert get_longest_div_k([1, 3, -2, 2, 2, 6, 9, -4, 6, 4, 7, -5], 2) == [-2, 2, 2, 6]

def numarDeDiv(x: int):
    '''
    calculeaza numarul de divizori ai unui numar
    :param x: numar intreg
    :return: numarul de divizori ai unui numar
    '''
    nrdiv = 0
    for d in range(1, x):
        if x % d == 0:
            nrdiv += 1
    return nrdiv

def allHaveTheSameDivCount(l: list[int]):
    '''
    verifica daca toate elementele dintr-o lista au acelasi nr. de divizori
    :param l: lista de numere intregi
    :return: True daca toate elementele din l au acelasi nr. de divizori,sau False in caz contrar
    '''
    i = 0
    while i < len(l)-1:
        if numarDeDiv(l[i]) != numarDeDiv(l[i + 1]):
            return False
        i += 1
    return True

def testAllHaveTheSameDivCount():
    assert allHaveTheSameDivCount([14, 10, 8, 15]) is True
    assert allHaveTheSameDivCount([2, 78, 12, 35]) is False

def get_longest_same_div_count(l: list[int]):
    '''
    detrmina cea mai lunga subsecventa de numere care au acelasi numar de divizori
    :param l: lista de numere intregi
    :return: cea mai lunga subsecventa de numere care au acelasi numar de divizori
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if allHaveTheSameDivCount(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax

def test_get_longest_same_div_count():
    assert get_longest_same_div_count([3, 14, 10, 15, 8, 9, 12, 18, 20]) == [14, 10, 15, 8]
    assert get_longest_same_div_count([8, 5, 17, 14, 20, 12, 18, 11, 16, 78]) == [20, 12, 18]


def allHavePfEqualToPi(l: list[float]):
    '''
    verifica daca toate elementele dintr-o lista au partea intreaga egala cu partea fractionara
    :param l: lista de numere float
    :return: True daca toate elementele din l au partea intreaga egala cu partea fractionara,sau False in caz contrar
    '''
    for x in l:
        lStr = str(x)
        pi = lStr.split(".")[0]
        pf = lStr.split(".")[1]
        if pi != pf:
            return False
    return True


def testAllHavePfEqualToPi():
    assert allHavePfEqualToPi([17.23, 7.0, 34.98, 2.0]) is False
    assert allHavePfEqualToPi([12.12, 6.6, 18.18, 27.27]) is True

def get_longest_equal_int_real(l: list[float]):
    '''
    detrmina cea mai lunga subsecventa de numere care au partea intreaga egala cu partea fractionara
    :param l: lista de numere float
    :return: cea mai lunga subsecventa de numere care au partea intreaga egala cu partea fractionara
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if allHavePfEqualToPi(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax

def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([2.0, 13.13, 9.9, 77.77, 12.12, 8.5, 4.2, 7.2]) == [13.13, 9.9, 77.77, 12.12]
    assert get_longest_equal_int_real([3.14, 8.7, 9.62, 4.66, 8.0, 9.77]) == []


if __name__ == "__main__":
    testAllAreDiv()
    test_get_longest_div_k()
    testAllHaveTheSameDivCount()
    test_get_longest_same_div_count()
    testAllHavePfEqualToPi()
    test_get_longest_equal_int_real()
    l1 = []
    l2 = []
    l3 = []
    while True:
        optiune = input("Pentru tasta 1 citim prima lista\n"
                        "Pentru tasta 2 afisam cea mai lunga subsecventa de numere care sunt divizibile cu k\n"
                        "Pentru tasta 3 citim a doua lista de numere\n"
                        "Pentru tasta 4 afisam cea mai lunga subsecventa de numere care au acelasi numar de divizori\n"
                        "Pentru tasta 5 citim a treia lista de numere\n"
                        "Pentru tasta 6 afisam cea mai lunga subsecventa de numere care au partea intreaga egala cu partea fractionara\n"
                        "Pentru tasta x programul se va incheia:")
        if optiune == "1":
            l1 = citireLista()
        if optiune == "2":
            k = int(input("dati un numar intreg: "))
            print(allAreDivByK(l1, k))
        if optiune == "3":
            l2 = citireLista()
        if optiune == "4":
            print(allHaveTheSameDivCount(l2))
        if optiune == "5":
            l3 = citireLista3()
        if optiune == "6":
            print(get_longest_equal_int_real(l3))
        if optiune == "x":
            break
