# f= open("writedemo.txt","w")
# f.write("this is 1st line")
# f.close()

# f = open("writedemo.txt","w")
# l  =[23,45,23,45]
# for item in l:
#     f.write(str(item)+"\n")

# f.close()
# f= open("2ndfile.txt","w")
#
# l=["gohar",23,"+92","soan garden"]
# for data in l:
#     f.write(str(data)+"\n")
#
# f=open("2ndfile.txt","r")
# # print(f.read())
# # f.close()
#
# print(f.readline())
# print(f.readline())
# f.close()
# fw = open("testfile.txt","w")
# fw.write("gohar")
#
#
# fr=open("testfile.txt","r")
# print(fr.read())

# lr=["gohar","4 street 32 soja garden","ahsan",23]
# with open("testfile2.txt","w") as fw:
#     for i in lr:
#         fw.write(str(lr))
#
#
# with open("testfile2.txt","r") as fr:
#     print(fr.read())

l=["Gohar","ahsan","ali","amad","imran"]

with open("test3.txt","w") as fr:
    for i in l:
        fr.write(str(i)+"\n")


with open("test3.txt","r") as fw:
    print(fw.read())


with open("myfile.txt","r") as fwrite:
    for i in l:
        fwrite.write(str(i)+"\n")









