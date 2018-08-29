# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32
# и заканчивая 127-м включительно. Вывод выполнить в табличной форме:
# по десять пар «код-символ» в каждой строке.


def generate_line(start_index, step):
    line = ''
    for i in range(step):
        if start_index + i <= 127:
            line += f' {start_index + i} - {chr(start_index + i)} '

    return line


END = 127
STEP = 10

start_index = 32

while start_index <= 127:
    print(generate_line(start_index, STEP))
    start_index += STEP





