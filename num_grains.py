
def square(starting_square):
    if not 1 <= int(starting_square) <= 64:
        raise ValueError('square must be between 1 and 64')
    return 1 << (int(starting_square) - 1)

rice_on_starting_square = square(input("Pick a starting square: "))
print(rice_on_starting_square)

def total():
    return (1 << 64) - 1

print(total())
