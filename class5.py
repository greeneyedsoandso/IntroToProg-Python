print('using a list object')
lstRow = []
objFile = open("HomeInventory.txt", 'r')
for row in objFile:
    lstRow = row.split(',')
    print(lstRow)
    print(lstRow[0] + '|' + lstRow[1].strip())
objFile.close()

print('using Dictionary objects')
lstTable = []
dicRow = {}
objFile = open("HomeInventory.txt", 'r')
for row in objFile:
    i, v = row.split(',')
    dicRow = {'item': i, 'value': v}
    lstTable.append(dicRow)
    print(lstTable, '<< List with Dictionary objects')
objFile.close()
