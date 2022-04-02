f1r=open('file1.txt')
data1=f1r.read()

f2r=open('file2.txt')
data2=f2r.read()
f1w=open('file1.txt','w')
f1w.write(data2)
f2w=open('file2.txt','w')
f2w.write(data1)

