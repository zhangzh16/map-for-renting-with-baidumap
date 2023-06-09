import xlrd

df = xlrd.open_workbook('mapdraw_test.xlsx')
sheet = df.sheets()[0]
#print(sheet.nrows)
f=open('mapdraw.txt','w')

for mark in range(sheet.nrows):
    rows_value = sheet.row_values(mark)
    if rows_value[0] == 'address': continue
    #print(rows_value)
    #print('var opts'+str(mark)+' = {position: new BMapGL.Point('+str(rows_value[1])+', '+str(rows_value[2])+'), offset: new BMapGL.Size(0, 0) };')
    #print('var label'+str(mark)+' = new BMapGL.Label(\''+str(rows_value[0])+'\', opts'+str(mark)+');')
    #print('map.addOverlay(label'+str(mark)+');')
    #print('')
    
    f.write('var opts'+str(mark)+' = {position: new BMapGL.Point('+str(rows_value[1])+', '+str(rows_value[2])+'), offset: new BMapGL.Size(0, 0) };\n')
    f.write('var label'+str(mark)+' = new BMapGL.Label(\''+str(rows_value[0])+'\', opts'+str(mark)+');\n')
    f.write('map.addOverlay(label'+str(mark)+');\n')
    f.write('\n')
    
f.close()
