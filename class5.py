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

while(True):
    strItem = input('Item: ')
    strValue = input('Value: ')
    lstTable.append({'item': strItem, 'value': strValue})
    strChoice = input("Exit? ('y/n'): ")
    if strChoice.lower() == 'y':
        break
    print('Current data:', lstTable)

while(True):
    strItem = input('Item to remove: ')
    strStatus = 'Row not found' # Boolean flag method
    for row in lstTable:
        if row['item'].lower() == strItem.lower():
            lstTable.remove(row)
            strStatus = 'Row removed.'
    print(strStatus)
    print('Updated data:', lstTable)
