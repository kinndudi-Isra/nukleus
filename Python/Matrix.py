#list slicing

amazon_card = ['notebooks','laptop','monitor','grappes','hdd']
amazon_card [0] = 'flowers'
print(amazon_card)

#copyng the list

copyng_list = amazon_card[:]
copyng_list [1] = 'large monitor'
print (copyng_list)

#matrix

matrix = [ [1,2,3,4,5,],
          ['a','b','c','d','e']]
print(matrix)
print(matrix[1][0])
print(matrix[0][0])
 

#adding
#adding element to list is not creating a new list just modify him

basket = [1,2,3,4,5,]

#append 
basket.append(100)
print(basket) 