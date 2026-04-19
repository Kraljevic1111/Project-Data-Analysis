import pandas as pd 

data = {
    "order_id": [1, 2, 3, 4, 5, 6],
    "customer": ["Ana", "Marko", "Ana", "Jovan", "Marko", "Ana"],
    "product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse", "Mouse"],
    "price": [800, 20, 50, 900, 25, 22],
    "quantity": [1, 2, 1, 1, 1, 3]
}

df = pd.DataFrame(data)

# total price 

df['total_price'] =df['price'] * df['quantity']

print(df['total_price'])

# ukupna potrosnja po kupcu 

total_price_by_customer = df.groupby('customer')['total_price'].sum()
print('Total price by customer:')
print(total_price_by_customer)

# top customer 

top_customer = total_price_by_customer.sort_values(ascending = False).head(1)
print('Top customer:')
print(top_customer)

# ukupan prihod po prozivodu 

total_revenue_per_product = df.groupby('product')['total_price'].sum()
print('Total revenue per product:')
print(total_revenue_per_product)

# po zaradi opadajuce 

revenue_sorted = total_revenue_per_product.sort_values(ascending = False)
print('Revenue sorted in descending order:')
print(revenue_sorted)

# proizvod koji se navise prodao u kolicini

best_quantity = df.groupby('product')['quantity'].sum().sort_values(ascending = False).head(1)
print('The best product sold in quantity:')
print(best_quantity)

# prosecna cena po proizvodu 

avg_price_per_product = df.groupby('product')['price'].mean()
print('Average price per product:')
print(avg_price_per_product)