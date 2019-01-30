import datetime


def decorator_maker(path):
    def my_decorator(function_to_decorate):
        def cover_function(*args, **kwargs):
            now = datetime.datetime.now()
            log_string = ''
            with open(path, 'a', encoding='utf8') as log:
                log_string += f'{now.strftime("%d-%m-%Y %H:%M:%S")} | Имя функции: {function_to_decorate.__name__} | ' \
                          f'Переданные аргументы: {args} {kwargs} | Результат: \n'
                result_string = function_to_decorate(*args, **kwargs)
                log_string += str(result_string) + '\n'
                log.write(log_string)
        return cover_function

    return my_decorator
