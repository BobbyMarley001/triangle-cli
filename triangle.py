import sys

def can_form_triangle(n):
    row = 1
    total = 0
    rows = []

    while True:
        count = 2 * row - 1  # 1, 3, 5, 7...
        if total + count > n:
            break
        rows.append(count)
        total += count
        row += 1

    if total != n:
        print("Impossible to build a triangle")
        return

    number = 1
    max_width = rows[-1] * 2
    for count in rows:
        line = ' '.join(str(number + i) for i in range(count))
        print(line.center(max_width))
        number += count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter a number as the first argument.")
    else:
        try:
            n = int(sys.argv[1])
            can_form_triangle(n)
        except ValueError:
            print("Please provide a valid integer.")
