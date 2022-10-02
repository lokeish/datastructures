# example - 1 is generating binary strings.

def _print(string, index):
    if index == len(string):
        # base condition for recursion.
        print("returning")
        print(''.join(string))
        return
    print(f"before main if ---{string}")
    if string[index] == "?":
        # replace '?' by 0 and recurse
        print(f'at first if, index --{index}, list--{string}')
        string[index] = '0'
        _print(string, index + 1)

        # replace '?' by 1 and recurse
        print(f'at second if, index --{index}, list--{string}')
        string[index] = '1'
        _print(string, index)

        # Note need to backtrack as string is passed by reference to the function.
        print(f"back track step --{index}, list--{string}")
        string[index] = '?'

    else:
        print(f"at else step, index --{index}, list--{string}")
        _print(string, index + 1)


if __name__ == "__main__":
    string = "1??0?101"
    string = list(string)
    print("entering into main")
    _print(string, 0)
