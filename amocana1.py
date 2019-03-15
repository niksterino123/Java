
def magaziebi (x,c):
    count = 0
    while int(x) != count:
        c[input('sheiyvanet magaziis saxeli :')] = input('sheiyvanet productis saxeli :')
        count += 1


def shemowmeba (z):
    print(z[input('sheiyvanet shesamowmebeli magaziis sia :')])


def damateba (d):
    carieli = open ('sia.txt','w')
    for key,value in d.items():
        carieli.write("{}: {}\n".format(key,value))


def main ():
    sia = {}
    raodenoba = input('daweret ramdeni magazia gsurt :')
    magaziebi (raodenoba , sia)
    shemowmeba(sia)
    damateba(sia)


if __name__ == '__main__':
    main()

