import ast


def strtodict(text1):
    responsetext2 = ast.literal_eval(text1)
    return responsetext2




def gettxt(filepath,cishu1):
    myfile=open(filepath)
    mylist=myfile.readlines()
    lines=len(mylist)
    list3=[]
    cishu=cishu1
    cishu2=(cishu//lines)+1
    i=0
    while i<cishu2:
        for line in open(filepath):
            list1=line.split(",")
            list3.append(list1)
        i=i+1
    return list3