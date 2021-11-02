def citireLista():
    l = []
    givenString = input("dati lista de nr. intregi, despartite prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

#Proprietatea 6
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

#Prorietatea 12
def numarDeDiv(x: int):
    '''
    calculeaza numarul de divizori ai unui numar
    :param x: numar intreg
    :return: numarul de divizori ai unui numar
    '''
    nrdiv = 0
    for d in range(1, x + 1):
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

#Proprietatea 7
def isNotPrime(x: int):
    '''
    determina daca un nr. este prim
    :param x: un numar intreg
    :return: True, daca x nu este prim sau False in caz contrar
    '''
    nrd = 0
    for d in range(1, x + 1):
        if x % d == 0:
            nrd += 1
    if nrd != 2:
        return True
    return False

def testIsNotPrime():
    assert isNotPrime(31) is False
    assert isNotPrime(121) is True

def verifListaNotPrime(l: list[int]):
    '''
    verifica daca o lista contine doar numere neprime
    :param l: o lista de numere intregi
    :return: True daca lista l contine doar numere neprime, sau false in caz contrar
    '''
    for i in l:
        if isNotPrime(i) is False:
            return False
    return True

def testVerifListaNotPrime():
    assert verifListaNotPrime([31, 17, 16, 23, 64]) is False
    assert verifListaNotPrime([9, 15, 36, 72, 10]) is True

def get_longest_all_not_prime(l: list[int]):
    '''
    detrmina cea mai lunga subsecventa de numere care sunt neprime
    :param l: lista de numere intregi
    :return: cea mai lunga subsecventa de numere care sunt neprime
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if verifListaNotPrime(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax

def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([29, 16, 8, 6, 7, 31, 15, 9, 11]) == [16, 8, 6]
    assert get_longest_all_not_prime([29, 16, 8, 6, 7, 31, 15, 9, 12, 48, 27, 17]) == [15, 9, 12, 48, 27]

if __name__ == "__main__":
    testAllAreDiv()
    test_get_longest_div_k()
    testAllHaveTheSameDivCount()
    test_get_longest_same_div_count()
    testIsNotPrime()
    testVerifListaNotPrime()
    test_get_longest_all_not_prime()
    l = []
    while True:
        optiune = input("Pentru tasta 1 citim o lista de numere\n"
                        "Pentru tasta 2 afisam cea mai lunga subsecventa de numere care sunt divizibile cu k\n"
                        "Pentru tasta 3 afisam cea mai lunga subsecventa de numere care au acelasi numar de divizori\n"
                        "Pentru tasta 4 afisam cea mai lunga subsecventa de numere care sunt neprime\n"
                        "Pentru tasta x programul se va incheia:")
        if optiune == "1":
            l = citireLista()
        if optiune == "2":
            k = int(input("dati un numar intreg: "))
            print(get_longest_div_k(l, k))
        if optiune == "3":
            print(get_longest_same_div_count(l))
        if optiune == "4":
            print(get_longest_all_not_prime(l))
        if optiune == "x":
            break
