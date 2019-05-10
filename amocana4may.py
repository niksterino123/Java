
def counter(rand_int):
    keys = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10,
            'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    answer = ""
    exception = rand_int
    for k,v in keys.items():
        if rand_int >= v:
            answer += k
            rand_int = rand_int - v

    saboloo_pasuxi = "{}:  {}".format(exception, answer)
    print(saboloo_pasuxi)
    open("romans.txt", "a").write(saboloo_pasuxi + "\n")

counter(rd.choice(List))
