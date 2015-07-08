#This program counts the number of letters in the names of all the numbers from 1 to 1000 (inclusive)

teen_arr = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens_arr = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

hun = 7
and_len = 3 
sum_of_digits = 36 #number of letters in one + num letters in two + ... + number of letters in nine
teen_len = 0
tens_len = 0
for s in teen_arr:
  teen_len += len(s)

for s in tens_arr:
  tens_len += len(s)

num_letters = 36*190+hun*900+and_len*(9*99)+tens_len*100+teen_len*10+len("onethousand")
print "The number of letters in all the words written out from one to 999 is " + str(num_letters)

