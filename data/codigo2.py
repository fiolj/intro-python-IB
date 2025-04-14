from enum import Enum

class State(Enum):
    VALIDO = 1
    TOLERABLE = 2
    INVALIDO = 3

# Niveles de prueba para el problema
niveles = """
7 6 4 2 1
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
1 2 7 8 9
"""

def ascending(nivel):
    for i in range(len(nivel)-1):
        if nivel[i] > nivel[i+1]:
            return False
    return True

def descending(nivel):
    for i in range(len(nivel)-1):
        if nivel[i] < nivel[i+1]:
            return False
    return True


def testea_nivel(nivel):

    if ascending(nivel):
        return "Ascendente"
    elif descending(nivel):
        return "Descendente"
    else:
        return "ZigZag"
    
def testea_niveles(niveles):
    return [testea_nivel(nivel) for nivel in niveles]

def remove_one(nivel):
    return [nivel[1:n] + nivel[n+1:len(nivel)] for n in range(0, len(nivel))]
    
def testea_niveles_menos_uno(niveles2d):

    all_status = []
    for nivel in niveles2d:
        print(nivel, testea_nivel(nivel))
        nivel_status = testea_nivel(nivel)

        if nivel_status == State.INVALIDO:
            nivel_menos_uno = remove_one(nivel)
            nivel_status = testea_niveles(nivel_menos_uno)
            status = State.TOLERABLE if State.VALIDO in nivel_status else State.INVALIDO
        else:
            status = State.VALIDO

        all_status.append(status)
    return all_status 


if __name__ == "__main__":
    #
    #   Prueba 
    #

    niveles2d = [n.split() for n in niveles.splitlines()[1:-1]]
    niveles2d = [[int(n) for n in nivel] for nivel in niveles2d]
    print(niveles2d)

    niveles_menos_uno = remove_one(niveles2d[0])
    testea_niveles_menos_uno(niveles2d)

    #
    #   Niveles de archivo
    #
    # Leer archivo niveles.txt
    niveles_from_file = []
    with open("niveles.txt") as f:
        for line in f:
            niveles_from_file.append([int(n) for n in line.split()])

    print(niveles_from_file)

    status_of_niveles_from_file = testea_niveles_menos_uno(niveles_from_file)

    for s in [v.name for v in  status_of_niveles_from_file]:
        print(s)

    # Leer los status correctos de status_niveles.txt
    status_correctos = []
    with open("status_niveles.txt") as f:
        for line in f:
            status_correctos.append(line.strip())

    # Comparación 
    for sf,sc in zip(status_of_niveles_from_file, status_correctos):
        print(sf.name, sc)
        assert sf == State[sc]

