def shemowmeba(x, y):
   for i in x:
        if type(i) == int:
            y.append(i)
        else:
            shemowmeba(i, y)


def main():
    multi_dimensional_array = [1, [9, [[[[[2]]]]]], [[[2], [12, [2]], [10]]]]
    new_list = []
    shemowmeba(multi_dimensional_array, new_list)
    print(new_list)


if __name__ == "__main__":
    main()