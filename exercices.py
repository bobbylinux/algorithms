from merge_sort import merge_sort


def ex03(lista):
    #primo passaggio è far diventare un set la lista
    insieme = []
    for x in lista:
        found = False
        for el in insieme:
            if el == x:
                found = True
        if not found:
            insieme.append(x)
    #devo ordinare l'insieme
    insieme = merge_sort(insieme)
    #ora che ho ordinato lavoro sul backtracking
    backset(insieme, [], 0)


def backset(insieme, current, i):
    if i > len(insieme)-1:
        print(current)
    else:
        backset(insieme, current, i+1)
        backset(insieme, current+[insieme[i]], i+1)


if __name__ == '__main__':
    ex03([5,1,2])
    ex03([1,3,3,2,2,3,2,1,1,1,1])
