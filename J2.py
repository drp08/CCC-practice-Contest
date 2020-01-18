numlines = int(input())

# To find out the symbol number and create a new string
for symbol_input in range(0, numlines):
    symbol_input = int(input())

    number_input = int(input())

    symbol = symbol_input
    number = number_input
    symbols.append(symbol * number)
    

    new_symbol = symbol[0] * symbol[1]

    if new_symbol == 'number':
        pass
    elif new_symbol > 'number':
        new_symbol.pop(symbol)
    else:
        new_symbol.append(symbol)





