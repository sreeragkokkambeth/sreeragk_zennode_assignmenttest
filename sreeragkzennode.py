#declaring two arrays ,which is used to append values of discount and name of discounts seperately.
#thus we can calculate maximum discount for costomer ,and identify discount name
discount=[]
discount_=[]

# ask the user quantity of each product
product_a=int(input('enter number of product a'))
product_b=int(input('enter number of product b'))
product_c=int(input('enter number of product c'))

# ask the user whether the product is wraped as gift or not
print('do you want to wrap the product as gift? enter 1 for YES . enter 0 for NO')
gift_wrap=int(input("enter number"))

# calculating total quantity of all products purchas
total_quantity=product_a+product_b+product_c

# calculating cost of product a,b,c seperately and storing values in three variables
cost_a=product_a*20
cost_b=product_b*40
cost_c=product_c*50

# sub total of purchse is calculated and stored in a variable
total_cost=cost_a+cost_b+cost_c

# function to find discount
def discount_product():
        #if cart total exceeds 200 apply a flat 10 discount on cart total,
        #  means appending a value 10 to one array and and appending a value 'flat_10_discount '
        # on another array.these two values have same index numbers in both arrays
        if total_cost>200:
                        discount.append(10)
                        discount_.append('flat_10_discount')


        # declare and initialize a variable to store bulk 5 percentage discount
        total_bulk_5_discount=0

        # if quantity of product a exceeeds 10 ,apply a 5 persantage discount on product a's total cost
        if product_a>10:
                bulk_5_discount_a=cost_a*(5/100)
                total_bulk_5_discount+=bulk_5_discount_a
        
        # if quantity of product b exceeeds 10 ,apply a 5 persantage discount on product b's total cost    
        if product_b>10:
                bulk_5_discount_b=cost_b*(5/100)
                total_bulk_5_discount+=bulk_5_discount_b
          
        # if quantity of product c exceeeds 10 ,apply a 5 persantage discount on product c's total cost          
        if product_c>10:
                bulk_5_discount_c=cost_c*(5/100)
                total_bulk_5_discount+=bulk_5_discount_c
               
        # appending 'total bulk 5 discount' to one array and and appending a value 'total_bulk_5_discount '
        # on another array.these two values have same index numbers in both arrays
        discount.append(total_bulk_5_discount)
        discount_.append('bulk_5_discount')


        # if total quantity is greater than 20 units apply 10 percentage discount on cart total
        bulk_10_discount=0
        if total_quantity>20:
                bulk_10_discount+=total_cost*(10/100)

        # appending 'bulk_10_discount' to one array and and appending a value 'bulk_10_discount '
        # on another array.these two values have same index numbers in both arrays
        discount.append(bulk_10_discount)
        discount_.append("bulk_10_discount")

        # declare and initialize a variable to store tiered 50  discount
        total_tiered_50_discount=0
        if total_quantity>30:

                # if total quantity greater than 30 and quantity of product a greater than 15
                # apply a 50 % discount on products greater than 15
                if product_a>15:
                        unit_above_15=product_a-15
                        total_tiered_50_discount+=(unit_above_15*20)*(50/100)

                # if total quantity greater than 30 and quantity of product b greater than 15  
                # # apply a 50 % discount on products greater than 15     
                if product_b>15:
                        unit_above_15=product_b-15
                        total_tiered_50_discount+=(unit_above_15*40)*(50/100)
                        
                # if total quantity greater than 30 and quantity of product c greater than 15 
                # # apply a 50 % discount on products greater than 15       
                if product_c>15:
                        unit_above_15=product_c-15
                        total_tiered_50_discount+=(unit_above_15*50)*(50/100)

        # appending 'total_tiered_50_discount' to one array and and appending a value 'tiered 50 discount'
        # on another array.these two values have same index numbers in both arrays
        discount.append(total_tiered_50_discount)
        discount_.append("tiered_50_discount")

# function to find most beneficial discount for costomer       
def maximum_discount():
        # declare a global variable ,thus we can use it outside the bounded region
        global max_discount
        # declare and initialise a variable.this variable is used to compare all discount values and 
        # help to find maximum discount
        max_discount=0
        for i in range(len(discount)):
                if discount[i]>max_discount:
                        max_discount=discount[i]
        

# function to find the fee of product(gift wrap if present and shipping fee)
def fee_product():
        global fee
        global number_of_packs
        global gift_wrap_fee
        global shipping_fee
        fee=0

        # if user wants to gift wrap the product
        gift_wrap_fee=0
        if gift_wrap==1:
                gift_wrap_fee=total_quantity
                fee+=gift_wrap_fee
        # if user doesnt wants to gift wrap the product      
        else:
                print("gift wrap fee :",gift_wrap_fee)

        # initialise number of packs to 1.beacause atleast 1 pack is neccesary to ship the product
        number_of_packs=1

        # if total quantity is divisible by 10 ,we can use floor divided output itself for number of packs
        if total_quantity%10==0:
                number_of_packs=total_quantity//10
                shipping_fee=number_of_packs*5
        # if total quantity is not divisible by 10 ,we can use floor divided +1 for number of packs
        else:
                number_of_packs=(total_quantity//10)+1
                shipping_fee=number_of_packs*5
        print("shipping fee :",shipping_fee)
        fee+=shipping_fee
        print("total fee:",fee)

# function to display all the details of purchase
def purchase_details():
        print('name of product :product a ',',',"quantity of product a:",product_a,',','cost of product a:',cost_a)
        print('name of product :product b ',',',"quantity of product b:",product_b,',','cost of product b:',cost_b)
        print('name of product :product c ',',',"quantity of product c:",product_c,',','cost of product c:',cost_c)
        print('sub total :',total_cost)
        
        if max_discount!=0:
                # index of maximum discount
                discount_max_index=discount.index(max_discount)
                # index of maximum discount and maximum discount name in second array are same
                discount_name=discount_[discount_max_index]
                print( discount_name,":",max_discount)
        else:
                print("total discount :",max_discount)
        print("gift wrap fee :",gift_wrap_fee)
        print("shippinng fee :",shipping_fee)
        total_price_of_purchase=total_cost+fee-max_discount
        print("total price of purchase is:",total_price_of_purchase)



discount_product()
maximum_discount()
fee_product()
purchase_details()


