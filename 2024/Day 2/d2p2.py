def is_safe_line(values):
    previous = values[0]
    up = False
    down = False

    for val in values[1:]:
        diff = abs(val - previous)

        if not up and not down:
            if val > previous:
                up = True
            elif val < previous:
                down = True

        if not (0 < diff < 4) or (up and val < previous) or (down and val > previous):
            return False

        previous = val

    return True


def main():
    with open('input.txt') as file:
        lines = file.readlines()

    num_safe = 0

    for line in lines:
        values = list(map(int, line.split()))

        if is_safe_line(values):
            num_safe += 1
            continue

        for i in range(len(values)):
            modified_values = values[:i] + values[i + 1:]
            if is_safe_line(modified_values):
                num_safe += 1
                break

    print(num_safe)


if __name__ == '__main__':
    main()
