# Напишите программу, которая принимает на вход строку символов (заглавные и прописные буквы латинского алфавита),
# которые могут повторятся, например: YYYYggkeeeAAABV . Заглавные и строчные буквы различаются.
# Программа должна преобразовать (закодировать) строку в сжатый формат: Y4g2ke3A3BV .
# Число после символа – количество повторений, если символ однократный – едениwe выводить не надо.



input_string = input("Напишите строку: ")


def compress_string(s):
    compressed = []
    count = 1
    length = len(s)


    for i in range(length - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            compressed.append(s[i])
            if count > 1:
                compressed.append(str(count))
            count = 1

    compressed.append(s[-1])
    if count > 1:
        compressed.append(str(count))

    return ''.join(compressed)

compressed_string = compress_string(input_string)

print(compressed_string)









