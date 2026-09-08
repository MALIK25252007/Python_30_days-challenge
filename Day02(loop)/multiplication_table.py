# WAP to print multiplication table from 2 to 10

for row in range(1,11):
    for col in range(1,11):
        product=row*col
        if product <10:
            print('',product,'',end=' ')
        else:
            print(product,'',end=' ')
    print()