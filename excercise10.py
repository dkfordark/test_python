# https://quantrimang.com/hon-100-bai-tap-python-co-loi-giai-code-mau-142456

# https://viettuts.vn/bai-tap-python/tinh-giai-thua-trong-python 

# Bai 10

input_Str =input("nhap so vao, cach nhau boi dau ',' : ").split(',');
dimensions = [int (x) for x in input_Str];

print (input_Str[0]);
print (dimensions);
print (type(dimensions[0]));

rowNum = dimensions[0];
colNum = dimensions[1];

multilist = [[0 for col in range(colNum)] for row in range(rowNum)];

print (multilist);

for row in range (rowNum):
    for col in range (colNum):
        multilist [row][col] = row * col;

print (multilist);

