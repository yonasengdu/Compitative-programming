class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        decoder ={'0':0,'1':1 ,'2':2 ,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        int_num1 = 0
        int_num2 = 0
        
        for i in range(len(num1)):
            decoded_num1 = decoder[num1[~i]]
            int_num1 += ((10**i)*(decoded_num1))
                         
        for j in range(len(num2)):
                         decoded_num2 = decoder[num2[~j]]
                         int_num2 += ((10**j)*(decoded_num2))
        print(int_num1, int_num2)
                         
        return str(int_num1*int_num2)