class MyError(Exception):
    pass


def curry(func, arity):
    # для ф inner этот список будет глобальным
    if arity <= 0:
        raise MyError("Арность не может быть меньше или равна 0.")
    if arity > func.__code__.co_argcount:
        raise MyError("Переданная арность больше действительной.")
    if not isinstance(arity, int):
        raise MyError("Переданная арность функции обязана быть целым числом.")
    lst = []

    def inner(arg):
        nonlocal lst
        lst.append(arg)
        if len(lst) == arity:
            tmp = func(*lst)
            # освобождаем список, чтобы функцию можно было использовать повторно
            lst = []
            return tmp
        return inner

    return inner


def uncurry(curried_func, arity):
    """
    Этой функции передается внутренняя функция inner функции curry, принимающая один аргумент.
    Сначала возвращается функция, способная принимать любое кол-во аргументов.
    Все последующее обращение будет к внутренней функции.
    """

    def uncarried_func(*args):
        tmp_func = curried_func
        if len(args) != arity:
            raise MyError("Передано неверное кол-во аргументов.")
        if len(args) == arity:
            for el in args:
                tmp_func = tmp_func(el)
        return tmp_func

    return uncarried_func
