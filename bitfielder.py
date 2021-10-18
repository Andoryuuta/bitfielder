import sys

ANSI_ESCAPE_COLOR_GREEN = '\u001B[32m'
ANSI_ESCAPE_COLOR_RED = '\u001b[31m'
ANSI_ESCAPE_RESET = '\u001b[0m'

def is_hex(v):
    try:
        int(v, 16)
        return True
    except ValueError:
        return False

def format_binary_number(val, padding):
    padded_str = ('{:0' + str(padding) + 'b}').format(val)
    output = ''
    for k, v in enumerate(padded_str[::-1]):
        if k % 8 == 0:
            output += ' '
        output += v

    return output[::-1]

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: bitfielder.py [integer] [integer]")
        print("Example: bitfielder.py 0x00000000 0x00000020")
        sys.exit(1)

    before = sys.argv[1]
    after = sys.argv[2]
    max_bits = 0

    if is_hex(before) or is_hex(after):
        before_bits = len(before.split('0x')[-1]) * 4
        after_bits = len(after.split('0x')[-1]) * 4
        max_bits = max(before_bits, after_bits)
    else:
        before_bits = int(before, 0).bit_length()
        after_bits = int(after, 0).bit_length()
        max_bits = max(before_bits, after_bits)

    before = int(before, 0)
    after = int(after, 0)

    print('0b' + format_binary_number(before, max_bits) + ' - INPUT 1')
    print('0b' + format_binary_number(after, max_bits) + ' - INPUT 2')
    print('-' * len(format_binary_number(after, max_bits)))

    for i in range(max_bits):
        bit = 1 << i
        bit_match = (before & bit) == (after & bit)
        line_color = ANSI_ESCAPE_COLOR_GREEN if bit_match else ANSI_ESCAPE_COLOR_RED
        bit_as_padded_hex = ('{:0' + str(round(max_bits/4)) + 'X}').format(bit)

        print(f"{line_color}0b{format_binary_number(bit, max_bits)} = {'MATCHED' if bit_match else 'CHANGED'} 0x{bit_as_padded_hex}" + ANSI_ESCAPE_RESET)