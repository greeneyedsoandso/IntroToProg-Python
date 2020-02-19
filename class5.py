print('using a list object')
lstRow = []
objFile = open("HomeInventory.txt", 'r')
for row in objFile:
    lstRow = row.split(',')
    print(lstRow)
    print(lstRow[0] + '|' + lstRow[1].strip())
objFile.close()

print('using Dictionary objects')
dicRow = {}
objFile = open("HomeInventory.txt", 'r')
for row in objFile:
    i, v = row.split(',')
    dicRow = {'item': i, 'value': v}
    print(dicRow)
    print(dicRow['item'] + '|' + dicRow['value'].strip())
objFile.close()