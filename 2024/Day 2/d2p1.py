def main():
    with open('input.txt') as file:
        lines = file.readlines()

    num_safe = 0

    for line in lines:
        first = True
        previous = None
        up = False
        down = False
        is_safe = True

        for val in line.split():
            val = int(val)
            
            if first:
                first = False
                previous = val
                continue

            diff = abs(val - previous)

            if not up and not down:
                if val > previous:
                    up = True
                elif val < previous:
                    down = True

            if not (0 < diff < 4):
                is_safe = False
                break

            if (up and val < previous) or (down and val > previous):
                is_safe = False
                break

            previous = val

        if is_safe:
            num_safe += 1

    print(num_safe)

if __name__ == '__main__':
    main()
