a = [['1', '2', '3', ],
     ['4', '5', '6', ],
     ['7', '8', '9', ],
     ['11', '13', '14']]  # m=4,n=3
b = []
for i in range(len(a[0])):
    row = []
    for j in range(len(a)):
        row.append(a[j][i])
    b.append(row)
for i in range(3):
    print(b[i])
# for j in range (len(a)):
#     row = []
#     for i in range(len(a)):
#         row.append(a[len(a)-1-i][j])
#     b.append(row)
# for i in range(len(a)):
#     print(b[i])
