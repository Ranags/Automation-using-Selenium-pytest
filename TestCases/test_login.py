# import pytest
#
# @pytest.mark.regression
# def testLogin():
#     print("Login ")
#
# @pytest.mark.sanity
# def testsearch():
#     print("hello")
#     print("This is search")
#
#
# def testcalculation():
#     assert 2+2 == 4
lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

uniqueList = []
duplicateList = []

for i in lis:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)
print(duplicateList)