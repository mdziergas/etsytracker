#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 00:54:59 2020

@author: marekdziergas
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:16:50 2020

@author: marekdziergas
"""

import csv


class Etsy():

    def __init__(self, filename):
        self.filename = filename
        
    def sum_col(self, column):
        f = open(self.filename)
        csv_f = csv.reader(f)
        list = []
        total = 0
        count = 0
        for row in csv_f:
            if count > 0:
                list.append(float(row[column]))
                total += float(row[column])
            count +=1
        return total
    
    def sum_rows(self):
        f = open(self.filename)
        csv_f = csv.reader(f)
        count = 0
        for row in csv_f:
           count += 1
        return count - 1
    
#Fee breakdown
processing_fixed_fee = .25
processing_rate_fee = .03
transaction_fee = 0.05
listing_fee = .20


review2020 = Etsy('etsyorders.csv')
#items purchased
total_items_sold = review2020.sum_col(6)
#sums order total
total_revenue = review2020.sum_col(23)
#sums order value
total_order_value = review2020.sum_col(16)
#finds tax by subtracting: total revenue - total order value. Might only work with free shipping.
total_tax_collected = total_revenue - total_order_value
#transaction fees: 5% of order value
total_transaction_fees = total_order_value * transaction_fee
#finds number of orders placed
total_orders = review2020.sum_rows()
#finds fixed fees per each order placed: orders * $0.25
total_processing_fixed_fees = total_orders * processing_fixed_fee
#finds total variable fees: total revenue * 3%
total_processing_variable_fee = total_revenue * processing_rate_fee
#sum of card processing fees
total_proccessing_fees = total_processing_fixed_fees + total_processing_variable_fee
#finds total listing fees: total orders * $0.20
total_listing_fees = total_items_sold * listing_fee
#finds total fees = total processing fees: (3% + $0.25) + (5%) + ($0.2)
total_sold_item_fees = total_proccessing_fees + total_transaction_fees + total_listing_fees
#additional expenses
#COGS
cogs = float(input('Enter the cost of goods sold: $'))
#ask for marketing expense
etsy_marketing_expense = float(input('Enter marketing expenses: $'))
#shipping expense
shipping_expenses = float(input('Enter shipping expenses: $'))
#ask for additional current listings
total_current_listings = int(input('Enter the number of current listings: '))
#calculates additional listing fee
additional_listing_fee = total_current_listings * listing_fee
#calculates total expenses outside of etsy tracking
total_expenses_outside_etsy = cogs + shipping_expenses
#calculates expenses tracked in etsy
total_expenses_tracked_by_etsy = total_sold_item_fees + additional_listing_fee + etsy_marketing_expense + total_tax_collected
#calculates total expenses in and out of etsy
total_expenses = total_expenses_outside_etsy + total_expenses_tracked_by_etsy
#calculates etsy balance
etsy_balance = total_revenue - total_sold_item_fees - etsy_marketing_expense - additional_listing_fee
#calculates profit
net_income = total_revenue - total_expenses


print('\n\nETSY STORE SUMMARY')
print('\n ORDERS\n')
print(f'     Total Orders: {total_orders}')
print(f'     Total Items Sold: {int(total_items_sold)}')
print(f'     Average Items Sold Per Order: {total_items_sold/total_orders:.2f}')

print('\n FINANCIALS\n')
print('  REVENUES\n')
print(f'     Total Revenue: ${total_revenue:.2f}')
print('\n  EXPENSES\n')
print(f'     Cost of Goods Sold: ${cogs:.2f}')
print(f'     Shipping: ${shipping_expenses}')
print('    Etsy Expenses')
print(f'     Total Sold Item Fees: ${total_sold_item_fees}')
print(f'     Additional Listing Fees: ${additional_listing_fee}')
print(f'     Etsy Marketing Expense: ${etsy_marketing_expense}')
print(f'     Taxes Remitted: ${total_tax_collected:.2f}')
print(f'    Total Etsy Expenses: ${total_expenses_tracked_by_etsy}')
print(f'    Total Non-Etsy Expenses: ${total_expenses_outside_etsy:.2f}')
print(f'  Total Expenses: ${total_expenses:.2f}')
print(f'  Net Income: ${net_income:.2f}')
print(f'Etsy Balance: ${total_revenue-total_expenses_tracked_by_etsy:.2f}')








    




    