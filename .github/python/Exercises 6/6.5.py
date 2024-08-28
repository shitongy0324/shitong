def even_number(list):
    for a in  list:
        if a % 2 == 0:
            list.remove(a)
    return list



list=[1,2,3,4,5,6]
print(f"{list}\n{even_number(list)}")