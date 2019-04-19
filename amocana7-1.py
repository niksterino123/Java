import re




xmovnebi = ''.join(list(filter(lambda x: (re.match("[aeiouy]", x)), open('samples.txt','r').read())))

tanxmovnebi = ''.join(list(filter(lambda x: (re.match("[^aeiouy!-=]", x)), open('samples.txt','r').read()))).replace(" ", "")

kentebi = ''.join(list(filter(lambda y: (int(y) % 2 != 0), [i for i in open('samples.txt','r').read() if i.isdigit()])))

luwebi = ''.join(list(filter(lambda y: (int(y) % 2 == 0), [i for i in open('samples.txt', 'r').read() if i.isdigit()])))

open('xmovnebi.txt', 'w').write(xmovnebi)
open('tanxmovnebi.txt', 'w').write(tanxmovnebi)
open('kentebi.txt', 'w').write(kentebi)
open('luwebi.txt', 'w').write(luwebi)

open('samples.txt', 'r').close()
