print("===== BILL GENERATOR =====")

item1 = input("Enter Item 1: ")
price1 = float(input("Enter Price 1: "))
qty1 = int(input("Enter Quantity 1: "))

item2 = input("Enter Item 2: ")
price2 = float(input("Enter Price 2: "))
qty2 = int(input("Enter Quantity 2: "))

item3 = input("Enter Item 3: ")
price3 = float(input("Enter Price 3: "))
qty3 = int(input("Enter Quantity 3: "))

total1 = price1 * qty1
total2 = price2 * qty2
total3 = price3 * qty3

subtotal = total1 + total2 + total3
gst = subtotal * 0.18
grand_total = subtotal + gst

print("\n========== BILL ==========")
print(item1, "=", total1)
print(item2, "=", total2)
print(item3, "=", total3)

print("--------------------------")
print("Subtotal =", subtotal)
print("GST (18%) =", gst)
print("Grand Total =", grand_total)
print("==========================")
