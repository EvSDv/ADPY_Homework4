from utils.decorator import decorator_maker


@decorator_maker('log.txt')
def adv_print(*args, start='', max_line=0, in_file=False):
    result = str(start)
    result_sep = ''
    for value in args:
        result += str(value)

    if max_line > 0 and len(result) > max_line:
        for symbol in range(0, len(result), max_line):
            result_sep += result[symbol:symbol + max_line] + '\n'
        result = result_sep

    if in_file:
        with open('result.txt', 'w', encoding='utf8') as file:
            file.write(result)
        return result
    else:
        return result


if __name__ == '__main__':

    adv_print(31153, '1111111111', start='*', max_line=5, in_file=True)
    adv_print('Строка для примера', start='*', max_line=5, in_file=False)