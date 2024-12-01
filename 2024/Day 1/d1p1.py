def main():
    with open('input.txt') as file:
        lines = file.readlines()

    lowest_left_numbers = sorted(int(line.split(' ')[0]) for line in lines)
    lowest_right_numbers = sorted(int(line.split(' ')[3]) for line in lines)

    total_distance = sum(abs(left - right) for left, right in zip(lowest_left_numbers, lowest_right_numbers))

    print(total_distance)

if __name__ == '__main__':
    main()
