arr = []
for i in range(1, 1001):
    arr.append(i)


def linear(n):
    match = False
    print("Busca Linear-")
    count = 0
    if n < arr[-1] and n > arr[0]:
        for i in arr:
            count += 1
            
            if i == n:
                match = True
                print("Valor encontrado!")
                print(f"Numero de Comparacoes: {count}.")
                break
        if match == False:
            print("Valor nao encontrado!")
    else:
        print("Valor nao encontrado!")
    print("\n")



def binaria(n):
    match = False
    print("Busca Binaria-")
    count = 0
    b = int(len(arr) / 2) - 1
    x = b
    if n < arr[-1] and n > arr[0]:
        while x >= 1:
            count += 1
            x = int(round((x / 2) + 0.1, 0))
            
            if arr[b] == n:
                match = True
                print("Valor encontrado!")
                print(f"Numero de Comparacoes: {count}.")
                break
            
            elif n > arr[b]:
                b += x
                
            elif n < arr[b]:
                b -= x
                
        if match == False:
            print("Valor nao encontrado!")
    else:
        print("Valor nao encontrado!")
    print("\n")


def tabela(n):
    print("Busca por Tabela de Frequencia-")
    count = 0
    freq = {}
    for i in arr:
        if str(i) in freq:
            freq[f'{i}'] += 1
        else:
            freq[f'{i}'] = 1

    if str(n) in freq:
        count += 1
        print("Valor encontrado!")
        print(f"Numero de Comparacoes: {count}.")
    else:
        print("Valor nao encontrado!")        

    print("\n")

    
linear(1001)
binaria(1001)
tabela(1001)
