from importlib.resources import files

def sum_numbers():
    data_file = files("testpkg.data").joinpath("numbers.txt")
    print(data_file)
    numbers = [int(x) for x in data_file.read_text().splitlines()]
    return sum(numbers)

