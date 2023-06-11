'''
def main():
    print_column(3)


def print_column(height):
    print("#\n" * height, end="")



main()

def main():
    print_row(4)


def print_row(width):
    print("?" * width)


main()
'''
def main():
    print_square(3)


def print_square(size):

    # For each row in square
    for i in range(size):
        # For each brink in row
        for j in range(size):
            # Print Brick
            print("#", end="")
        print()


main()