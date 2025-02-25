def debug(func):
    def wrapper(*args, **kwargs):
       arg_str = ",".join(str(value) for value in args)
       kwargs_str = ",".join(f"{key}={value}" for key, value in kwargs.item())
       all_args_str = ",".join(filter(None, [args_str, kwargs_str]))

        print(f"funkcja {func.__name__}(3, b=2, c=4):")
        print(f"arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        return result

    return wrapper



@debug
def func(a, b, c):
    return a+b *c

if __name__ == "__main__":
    func(3, b=2, c=4)

#funkcja func(3, b=2, c=4) zwróciła 11
#11
