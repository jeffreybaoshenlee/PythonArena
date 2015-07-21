__author__ = "jeffrey"
__date__ = "$2015/5/18 下午 04:47:18$"

import random

def gen_random_bits(bit_count):
    if bit_count <= 0:
        raise RuntimeError("The bit count must greater than 0.");
    
    result = 0
    
    for digit in range(bit_count):
        if random.randint(0, 1):
            result |= 1 << digit
    
    return result
                        
def gen_random_numbers(max_value, count=None):
    if count == None:
        count = max_value
    data = [random.randint(0, max_value) for _ in range(count)]
    return data

if __name__ == "__main__":
    bit_count = 64
    
    while bit_count >= 0:
        print("{:#0{}b}".format(gen_random_bits(bit_count), bit_count + 2))
        bit_count //= 2
