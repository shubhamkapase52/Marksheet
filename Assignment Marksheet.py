class Marksheet():
    def __init__(self):
       self.name=input("enter the name of Candidate: ")
    def average(self):
        sub1=int(input("Enter the sub1 mark:"))
        sub2=int(input("Enter the sub2 mark:"))
        sub3=int(input("Enter the sub3 mark:"))
        sub4=int(input("Enter the sub4 mark:"))
        sub5=int(input("Enter the sub5 mark:"))
        sub6=int(input("Enter the sub6 mark:"))
        list=[sub1,sub2,sub3,sub4,sub5,sub6]
        sum=sub1+sub2+sub3+sub4+sub5+sub6
        avg=sum/6
        print("Average of Student is:",avg)
        a=0
        a1=0
        
        if(75>avg>90):
            print("Average Student")
        elif(avg>90):
            for x in list:
                if x>95:
                    a+=1
            if a>=3:
                print("gold medalist")
            else:
                print("good")

        elif(65>avg>75):
            for x in list:
                if x<60:
                    a1+=1
            if  a1>=3:
                print("fail")
            else:
                print("Give a chance")
        else:
            print("fail")
s=Marksheet()
s.average()
        
            
        
        
        








        





    
