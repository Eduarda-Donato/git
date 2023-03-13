def readcsv(filepath):
    f = open(filepath, 'r')
    content = f.read()
    print(content)
    f.close()

readcsv('aluguelbr.csv')