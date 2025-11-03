def permutation_naif(numbers, partials):
    if len(numbers) == len(partials):
        print(partials)
        return

    for num in numbers:
        if num not in partials:
            partials.append(num)
            permutation_naif(numbers, partials)
            partials.pop()


def permutation_swap(numbers, i):
    if i == 0:
        print(numbers)
        return

    for j in range(i):
        numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]
        permutation_swap(numbers, i - 1)
        numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]


def subsets_rec(n, current, i):
    if i > n:
        # condizione di stop: ho considerato tutti gli elementi
        print(current)
        return
        # caso 1: NON includo i
    subsets_rec(n, current, i + 1)

    # caso 2: includo i
    subsets_rec(n, current + [i], i + 1)


def subsets_naif(n, current, i):
    if i > n:
        print(current)
        return
    subsets_naif(n, current, i + 1)
    subsets_naif(n, current + [i], i + 1)


def subsets_k_of_n(n, missing, current, i):
    if missing == 0:
        print(current)
        return
    # se non ho superato n e missing è maggiore di zero e minore delle scelte ancora da fare
    elif i <= n and 0 < missing <= n - (i - 1):
        subsets_k_of_n(n, missing, current, i + 1)
        subsets_k_of_n(n, missing - 1, current + [i], i + 1)


def subsets_bitmask(n):
    for j in range(2 ** (n - 1)):
        print("{", end=" ")
        for i in range(n - 1):
            if j & 2 ** i != 0:
                print(i, ",", end=" ")
        print("}")


def ex03_0925(n, s):
    if len(s) == n:
        print(s)
    for j in (0, 1, 2):
        if len(s) < 1 or (len(s) == 1 and s[0] + j >= 2) or (len(s) >= 2 and 4 <= j + s[-1] + s[-2] <= 5):
            s.append(j)
            ex03_0925(n, s)
            s.pop()


def ex03_0724(n, i, s, pb, cb):
    if n == i:
        print(s)
        return
    for x in {0, 1}:
        if cb is None:
            cb = {"k": x, "v": 1}
            s.append(x)
            ex03_0724(n, i + 1, s, pb, cb)
            s.pop(x)
        else:
            if x == cb["k"]:
                cb["v"] += cb["v"] + 1
                s.append(x)
                ex03_0724(n, i + 1, s, pb, cb)
                s.pop(x)
            else:
                pb = cb
                cb = {"k": x, "v": 1}
                s.append(x)
                ex03_0724(n, i + 1, s, pb, cb)
                s.pop(x)
        if pb is not None and cb is not None and cb["v"] <= pb["v"]:
            s.append(x)
            ex03_0724(n, i + 1, s, pb, cb)
            s.pop(x)

'''
Data una stringa ternaria s vogliamo stampare tutte le stringhe ternarie della
stessa lunghezza di s e che differiscono da s in tutte le posizioni.

Ad esempio per s =

0 1020 vanno stampate le seguenti stringhe (non necessaria-
mente nello stesso ordine):

010, 011, 020, 021, 210, 211, 220, 221

Progettare un algoritmo che risolve il problema in tempo O(n · S(s)) dove n `e
la lunghezza della stringa s ed S(s) `e il numero di stringhe da stampare.
Motivare BENE la correttezza e la complessità dell’algoritmo proposto.
'''
def ex03_1024(s, i, result):
    if i >= len(s):
        print(result)
        return
    for item in {0,1,2}:
        if item != s[i]:
            result.append(item)
            ex03_1024(s, i+1, result)
            result.pop()

'''
ESERCIZIO 3 stampa risalite: data una scala con n

2 gradini vogliamo
sapere i diversi modi che abbiamo di risalita dal primo all’ultimo gradino della
scala sapendo che ad ogni passo possiamo risalire di 1, 2 o 3 gradini. Ogni modo
di risalire `e rappresentato dalla sequenza di passi che vengono di volta in volta
effettuati.

Ad esempio per una scala con n = 4 gradini la risposta sar`a data dalle 4 sequenze:

[1, 1, 1], [1, 2], [2, 1], [3]

Progettare un algoritmo basato sulla tecnica del backtracking che dato n stampa
i diversi modi di risalire la scala.
L’algoritmo deve avere complessità O(nS(n)) dove S(n) `e il numero di diversi
modi di risalire la scala.

Motivare BENE la correttezza e la complessit`a dell’algoritmo pro-
posto.
'''

def ex03_1023(n, s, r):
    if s == n:
        print(r)
        return
    for el in {1,2,3}:
        if s <= n:
            r.append(el)
            ex03_1023(n, s+el, r)
            r.pop()
        else:
            return


'''
Progettare un algoritmo che, dato l'intero , stampi tutte le matrici
binarie di dimensione tali che nella diagonale principale e in
ciascuna delle diagonali parallele a quella principale compaiano
elementi uguali.
L'algoritmo deve avere complessità dove è il numero di matrici
da stampare.
'''
def ex03_0325(n, i, M):
    if i == n*n:
        print(M)
        return
    for el in {0,1}:
        if i//n == 0 or i%n == 0 or M[(i//n)-1][(i%n)-1] == el:
            M[i//n][i%n] = el
            ex03_0325(n, i + 1, M)


'''
Dato un intero n vogliamo stampare tutte le stringhe binarie di lunghezza n in
cui non compare la sottostringa ’101’ n ́e la sottostringa ’010’.
Ad esempio per n = 40 delle 16 stringhe binarie lunghe 4 vanno stampate le
seguenti 10 (non necessariamente nello stesso ordine):

0000 0001 0011 0110 0111 1000 1001 1100 1110 1111

Progettare un algoritmo, basato sulla tecnica del backtracking, che risolva il
problema in tempo O(n · S(n)) dove S(n) `e il numero di stringhe da stampare.
Motivare BENE la correttezza e la complessit`a dell’algoritmo proposto
'''
def ex03_0225(n, i, result):
    if i > n:
        print(result)
        return
    for el in {0,1}:
        if i <= 1 or (el == 1 and result[-2:-1] != ['0','1']) or (el == 0 and result[-2:-1] != ['1','0']):
            result.append(el)
            ex03_0225(n, i+1, result)
            result.pop()



if __name__ == '__main__':
    # permutation_naif([1,2,3],[])
    # permutation_swap(['A', 'B', 'C'], 3)
    # subsets_rec(3, [], 1)
    # subsets_k_of_n(6, 3,[], 1)
    # subsets_naif(3,[], 1)
    # subsets_bitmask(4)
    # c = ex03_0925(5, [])
    # ex03_0724(4, 0, [], None, None)
    # ex03_1024([1,0,2], 0, [])
    # ex03_1023(3, 0, [])
    # n = 3
    # M = [[None for _ in range(n)] for _ in range(n)]
    # ex03_0325(n, 0, M)
    ex03_0225(3, 0,[])