import Magic_Square
table=Magic_Square.fill_it([],int(input('Enter the Number: ')))
print('Additive Magic Square: ')
Magic_Square.print_matrix(table)
for i in range(len(table)):
    for j in range(len(table[i])):
        table[i][j]=2**table[i][j]
print('Multiplicative Magic Square: ')
Magic_Square.print_matrix(table)