def readcsv(filepath):
    f = open(filepath, 'r')
    content = f.read()
    print(content)
    f.close()

readcsv('aluguelbr.csv')

def print_markdown(filepath):
    f = open(filepath, 'r')
    lines = f.readlines()

    first_line = lines[0]
    to_print = '|'+line.replace(',','|').strip()+'|'
    print(to_print)
    #print('-------------------------------------------')


    num_colunas = first_line.split(',')
    for i in range(num_colunas):
        print('|-',end=' ')
    print('|')


    for line in lines[1:]:
        to_print = '|'+line.replace(',','|').strip()+'|'
        print(to_print)

print_markdown('aluguelbr.csv')