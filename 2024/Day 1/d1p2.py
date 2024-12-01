def main():
    with open('input.txt') as file:
        lines = file.readlines()

    lowest_left_numbers = list(int(line.split(' ')[0]) for line in lines)
    lowest_right_numbers = list(int(line.split(' ')[3]) for line in lines)
    similarity_score = 0

    for i in range(len(lowest_left_numbers)):
        num_times_appeared = 0
        for j in range(len(lowest_right_numbers)):
            if lowest_left_numbers[i] == lowest_right_numbers[j]:
                num_times_appeared += 1
        similarity_score += (lowest_left_numbers[i] * num_times_appeared)

    print(similarity_score)

if __name__ == '__main__':
    main()
