products = []

data = [1, 3, 5, 7, 9] # 清單中裝著一些整數
# 請開始寫"寫入檔案"的程式碼

with open('test.txt', 'w')as f:
    for i in data:
        f.write(str(data[0]) + '\n')

while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入商品價格:')
    p = []
    p.append(name)
    p.append(price)
    #快寫法 p = [name,price]
    products.append(p)
    #快寫法 products.append([name, price])
print(products)

for p in products:
    print(p[0], '的價格是', p[1])

with open('products.csv','w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')


products[0][0] #大清單中的第一個,小清單中的第一個