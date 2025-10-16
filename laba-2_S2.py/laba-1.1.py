#Напишите программу, которая решает обратную задачу по отношению к заданию 1. Из строки типа  Y4g2ke3A3BV восстанавливает исходную.

input_str = input("Напишите строку: ")


def decompress_string(compressed):
    result = []
    i = 0


    while i < len(compressed):
        char = compressed[i]

        if char.isalpha():
            current_char = char
            i += 1

            num_str = ""
            while i < len(compressed) and compressed[i].isdigit():
                num_str += compressed[i]
                i += 1

            count = int(num_str) if num_str else 1
            result.append(current_char * count)
        else:
            i += 1
    return "".join(result)


decompressed_str = decompress_string(input_str)

print(decompressed_str)