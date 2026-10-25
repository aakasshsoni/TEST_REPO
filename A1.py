x = 2.5
y = 2.5
x = x + y
# print(x)

#-------------------------------------------------------#

def table(number, times):
    for i in range(1, times + 1):
        result = number * i 
        # print(result)
        print (number,"*",i,"=",result)
    
table(21, 20)


#------------------------------------------------------#
#Ruff 
# '''
#     for (i=1, i<=times, i++){
#        result = number * i;
#        print ("number * i = result");
#     }
    
# '''