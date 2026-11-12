"""Compute and print the Collatz sequence starting from 27."""


def collatz_sequence(start):
    """Return the Collatz sequence from start through the first 1, inclusive."""
    if start < 1:
        raise ValueError("start must be a positive integer")
    n = start
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz_sequence(27)
    for value in sequence:
        print(value)
    total_steps = len(sequence) - 1
    print(f"Total transformations to reach 1: {total_steps}")


if __name__ == "__main__":
    main()
