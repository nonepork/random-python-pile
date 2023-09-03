import time

# https://www.youtube.com/watch?v=PNXXqzU4YnM
def check_card_valid(card_number):
    product = 0

    for i in range(0, 16):
        if (i+1)%2==0: 
            product += int(card_number[i])*1
        else:
            num = int(card_number[i])*2
            # If length of product is larger than 1
            if len(str(num)) >= 2:
                first_num = int(num/10)
                second_num = num%10
                product += first_num + second_num
            else:
                product += num

    # If the last digit of product sum is 0
    if str(product)[-1] == '0':
        print('Valid card number')
        print(card_number)
        time.sleep(100)
    else:
        pass

first = input('Enter the first few digit of credit card(blank if none): ')
last = input('Enter the last few digit of credit card(blank if none): ')
total_len = 16 - len(first) - len(last)
top = first + '0' * total_len + last
bottom = first + '9' * total_len + last
add = '1' + len(last) * '0'
print(top, bottom, add)
for i in range(int(top), int(bottom), int(add)):
    #if i%123457 == 0:
        check_card_valid(str(i))
