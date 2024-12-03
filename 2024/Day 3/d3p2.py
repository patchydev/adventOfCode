import re

def main():
    mul_re = re.compile(r"mul\(\d+,\d+\)")
    tok_re = re.compile(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))")

    res = 0
    do = True

    with open('input.txt') as file:
        for _, line in enumerate(file):
            tokens = re.split(tok_re, line)

            for token in tokens:
                if token == "do()":
                    do = True
                elif token == "don't()":
                    do = False
                elif re.match(mul_re, token) and do:
                    matches = mul_re.findall(token)

                    for match in matches:
                        nums = [int(num) for num in re.findall(r'\d+', match)]

                        mul_res = nums[0] * nums[1]
                        res += mul_res

    print(res)

if __name__ == '__main__':
    main()