price,discount,vat=float(input()),float(input()),float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print('База после скидки:','%.2f' %base,'₽','\nНДС:','%.2f' %vat_amount,'₽','\nИтого к оплате:','%.2f' %total,'₽')