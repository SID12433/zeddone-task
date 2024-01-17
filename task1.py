pdt1_name="Product A"
pdt1_price=20
pdt1_qty=int(input("\nEnter the quantity of product A= "))
pdt1_wrap=input("do you want to wrap in gift? y/n= ")
pdt1_total=pdt1_qty*pdt1_price
pdt1_discount=pdt1_total*0.05 if pdt1_qty>10 else 0
pdt1_wrapfee=pdt1_qty if pdt1_wrap=="y" else 0

pdt2_name="Product B"
pdt2_price=40
pdt2_qty=int(input("\nEnter the quantity of product B= "))
pdt2_wrap=input("do you want to wrap in gift? y/n= ")
pdt2_total=pdt2_qty*pdt2_price
pdt2_discount=pdt2_total*0.05 if pdt2_qty>10 else 0
pdt2_wrapfee=pdt2_qty if pdt2_wrap=="y" else 0

pdt3_name="Product C"
pdt3_price=50
pdt3_qty=int(input("\nEnter the quantity of product C= "))
pdt3_wrap=input("do you want to wrap in gift? y/n= ")
pdt3_total=pdt3_qty*pdt3_price
pdt3_discount=pdt3_total*0.05 if pdt3_qty>10 else 0
pdt3_wrapfee=pdt3_qty if pdt3_wrap=="y" else 0

subtotal=pdt1_total+pdt2_total+pdt3_total

bulk_10_discount = max(pdt1_discount,pdt2_discount,pdt3_discount)
flat_10_discount = 10 if subtotal>200 else 0
best_discount = max(bulk_10_discount,flat_10_discount)
best_discountname= "bulk_10_discount"  if best_discount==bulk_10_discount else "flat_10_discount"

totalwrappingfees=pdt1_wrapfee+pdt2_wrapfee+pdt3_wrapfee

totalquantity=pdt1_qty+pdt2_qty+pdt3_qty
shippingfee=(totalquantity//10)*5

total=(subtotal-best_discount)+shippingfee+totalwrappingfees

print("\ndetails of the products")
print(f"{pdt1_name}= {pdt1_qty} qty")
print(f"{pdt2_name}= {pdt2_qty} qty")
print(f"{pdt3_name}= {pdt3_qty} qty")

print(f"\nsubtotal={subtotal}")
print(f"\n{best_discountname} is applied={best_discount} discount")
print(f"\nshippingfees={shippingfee}")
print(f"\ngift wrap fee={totalwrappingfees}")
print(f"\nTotal= {total}")




# steps
# >run the code in terminal
# >then enter the product quantity and y/n for wrapping
# >then you will be provided with the details

