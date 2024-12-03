import re

def main():
    regex = re.compile(r"mul\(\d+,\d+\)")

    res = 0

    with open('input.txt') as file:
        for _, line in enumerate(file):
            matches = regex.findall(line)

            for match in matches:
                nums = [int(num) for num in re.findall(r'\d+', match)]

                mul_res = nums[0] * nums[1]
                res += mul_res

    print(res)

if __name__ == '__main__':
    main()