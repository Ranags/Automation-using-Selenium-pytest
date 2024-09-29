# from openpyxl import Workbook , load_workbook
# wb=Workbook()
#
# ws = wb.active
#
# # ws['A10'] = "RCV Academy"
# # testdata = [['Name','Gohar'],['address','soan garden'],['university','cust university'],['age','23'],['gender','M']]
#
# # for data in testdata:
# #     ws.append(data)
# # wb.save("demo.xlsx")
#
#
# for i in range(1,6):
#     for j in range(1,5):
#         ws.cell(row=i , column=j).value  = i+j
# wb.save("demo.xlsx")
#
#



# # ************************* Read Data *******************************
#
#
lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9,23,450]
lis.remove(450)
print(lis)
# for i in lis:
#     print(lis.remove(i--))


# uniqueList = []
# duplicateList = []
#
# for i in lis:
#     if i not in uniqueList:
#         uniqueList.append(i)
#     elif i not in duplicateList:
#         duplicateList.append(i)
# print(duplicateList)



# thisdict = {
#
#     "name":"gohar",
#     "age":34,
#     "address":"bharia town"
#
# }
# print(thisdict["name"])