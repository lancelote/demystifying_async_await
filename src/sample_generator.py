def fibonacci():
    current, sequent = 0, 1
    while True:
        current, sequent = sequent, current + sequent
        yield current


def main():
    result = fibonacci()

    for number in result:
        print(number, end=', ')
        if number > 1000:
            break


if __name__ == '__main__':
    main()
