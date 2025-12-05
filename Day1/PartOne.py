

def read_input():
    result = []

    with open('input', 'r') as file:
        for ligne in file:
            ligne = ligne.strip()

            if not ligne: continue
            lettre = ligne[0]
            nombre = int(ligne[1:])
            modulo = nombre % 100
            if lettre == 'R':
                result.append(modulo)
            elif lettre == 'L':
                result.append(-modulo)
        file.close()
    return result


def count_of_zeros():
    nombres =  read_input()
    dial = 50
    counter = 0
    for n in nombres:
        dial += n
        dial %= 100
        if dial == 0:
            counter += 1
    return counter
print(count_of_zeros())




