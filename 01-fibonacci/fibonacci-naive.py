def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def main():
    num = int(input())
    print(fibonacci(num))


if __name__ == '__main__':
    main()
