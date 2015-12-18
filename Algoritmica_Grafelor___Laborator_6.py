def readFromFile(fileName, ExInit, ExTerm, Capacitate):
    f = open(fileName, 'r')
    ok = 0
    for i in f:
        line = i.split(" ")
        if ok == 0:
            n = int(line[0])
            m = int(line[1])
        else:
            ExInit.append(int(line[0]))
            ExTerm.append(int(line[1]))
            Capacitate.append(int(line[2]))
        ok += 1
    return n, m, ExInit, ExTerm, Capacitate
def readParcurgereFromFile(fileName, parcurgere):
    f = open(fileName, 'r')
    ok = 0
    for i in f:
        line = i.split(",")
        if ok == 0:
            n = int(line[0])
        else:
            line = [i.split('\n')[0] for i in line] 
            parcurgere.append(line)
        ok += 1
    for i in parcurgere:
        for x in range(len(i)):
            i[x] = int(i[x])
    return n, parcurgere
def Initializari(Fi, m):
    for i in range(m):
        Fi.append(0)
    return 0, Fi
def VarfSursa(term, n):
    for varf in range(n):
        if varf+1 not in term:
            return varf+1
def VarfDestinatie(init, n):
    for varf in range(n):
        if varf+1 not in init:
            return varf+1
def ResetVectorEtichete(VectorEtichete, n):
    Pi = [0, "*", 10000000]
    VectorEtichete.append(Pi)    
    Pi = [0, "0", 0]
    for i in range(n-1):
        VectorEtichete.append(Pi)
    return VectorEtichete   
def EticheteazaVarful(VectorEtichete, e1, e2, e3, varf):
    vector = []
    vector.append(e1)
    vector.append(e2)
    vector.append(e3)
    VectorEtichete[varf-1] = vector
    return VectorEtichete
def ifIsMarked(vectorEtichete, varf):
    if vectorEtichete[varf-1][1] == "0":
        return False
    return True
def minim(a, b):
    if a < b:
        return a
    return b
def ifExistaMuchieDela_i_la_j(i, j, ExInit, ExTerm, m):
    for pi in range(m):
        if ExInit[pi] == i and ExTerm[pi] == j:
            return True, pi
    return False, pi

def FordFulkerson():
    ExInit = []
    ExTerm = []
    Capacitate = []
    vect = 54
    n, m, ExInit, ExTerm, Capacitate = readFromFile("sursa.txt", ExInit, ExTerm, Capacitate)
    Fi = []
    vectorEtichete = []
    k, Fi= Initializari(Fi, m)
    vectorEtichete = ResetVectorEtichete(vectorEtichete, n)
    s = VarfSursa(ExTerm, n)
    t = VarfDestinatie(ExInit, n)
    parcurgere = []
    terminat, parcurgere = readParcurgereFromFile("ordine.txt", parcurgere)
    numarIteratii = 0
    flux = 0
    while numarIteratii < terminat :
        vector = parcurgere[numarIteratii]
        numarIteratii += 1
        vectorEtichete = ResetVectorEtichete(vectorEtichete, n)
        k = 0
        while k < len(vector)-1:
            i = vector[k]
            j = vector[k+1]
            bool, u = ifExistaMuchieDela_i_la_j(i, j, ExInit, ExTerm, m)
            if  bool == True:
                vectorEtichete = EticheteazaVarful(vectorEtichete, i, '+', minim(vectorEtichete[i-1][2], Capacitate[u] - Fi[u]), j)
            else:
                vectorEtichete = EticheteazaVarful(vectorEtichete, i, '-', minim(vectorEtichete[i-1][2], Fi[u]), j)
            k += 1
        j = 3
        ebsilon = vect
        while j != VarfSursa(ExTerm, n):
            i = vectorEtichete[j-1][0]
            bool, u = ifExistaMuchieDela_i_la_j(i, j, ExInit, ExTerm, m)
            if vectorEtichete[j-1][1] == '+':
                Fi[u] = Fi[u] + ebsilon
            else:
                Fi[u] = Fi[u] - ebsilon
            j = i
    flux = flux + vect
    print "Fluxul maxim prin reteaua data este", flux

FordFulkerson()