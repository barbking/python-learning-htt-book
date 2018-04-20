# Barbara King
# htt9_ex22.py


def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: ${:.2f}'.format(total))
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total ${:.2f}'.format(total))
    print('Average price per item: $', round(average,2))

checkout()