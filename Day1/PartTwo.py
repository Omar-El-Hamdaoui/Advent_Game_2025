
def read_input_with_no_mod():
    result = []
    with open('input', 'r') as file:
        for ligne in file:
            ligne = ligne.strip()
            if not ligne: continue
            lettre = ligne[0]
            value = int(ligne[1:])
            if lettre == 'R':
                result.append(value)
            elif lettre == 'L':
                result.append(value)
        file.close()
    return result

def count_of_zeros_method_0x434C49434B():
    nombres =  read_input_with_no_mod()
    dial = 50
    counter = 0
    for n in nombres:
        # if for numbers greater than 100
        if abs(n) >= 100 :
            counter += abs(n)//100
        n %= 100
        if (n + dial >= 100):
            counter += 1
            dial += n
            dial %= 100
        else:
            dial += n
    return counter


print(count_of_zeros_method_0x434C49434B())

