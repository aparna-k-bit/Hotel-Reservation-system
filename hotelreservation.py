
 print "--------------------------------------------------------------------------------------------------------------------------------------------------------------"
print "                                                           WELCOME TO REGENT HOTELS!!!!                                                                         "
print "--------------------------------------------------------------------------------------------------------------------------------------------------------------"

import os
import pickle
import random
class hotel:
   
   def getdata(self):
       
       self.rno=input("Enter the room no.: ")
       self.rtype=raw_input("Enter the room type: ")
       self.roomis="no"
       self.rtaken="_"
   def displaydata(self):
       print self.rno,"     ",self.rtype,"     ",self.roomis,"         ", self.rtaken

   def dispdata(self):
       print "Room Number= ",self.rno
       print "Room Type= ",self.rtype
       print "Room Booked= ", self.roomis
       print "Room Issued By= ", self.rtaken
   
   def roomtakenfn(self,rno,rtype,roomis,eno):
       self.rno=rno
       self.rtype=rtype
       self.roomis=roomis
       self.rtaken=eno

class hoteladmin:
   def getinfo(self):
       self.eno=input("Enter the employee number: ")
       self.ename=raw_input("Enter the employee name: ")
       self.pwd=random.randint(100000,999999)
       
   def displayinfo(self):
       print  self.eno,"       ",self.ename,"              ",self.pwd

   def infodate(self):
       print"Employee Number= ",self.eno
       print"Employee Name= ",self.ename
       print"Employee Pwd= ",self.pwd
   

class roomentry:
   
   def roomdata(self):
       self.rno=input("Enter the room no: ")
       self.eno=input("Enter id no.: ")
   def roomissuefn(self,eno,rno,rtype):
       self.eno=eno
       self.rno=rno
       self.rtype=rtype
   def disproomentry(self):   
       printself.eno,"          ",self.rno, "           ", self.rtype
       print    
       
       
def main():
   ansmain="y"
   while (ansmain=="y"):
       print "                                              ||HOTEL RESERVATION MANAGEMENT SYSTEM|| "
       print "                                                     1.ROOM ENTRY"
       print "                                                     2.HOTEL ADMIN ENTRY"
       print "                                                     3.HOTEL ADMIN LOGIN"
       print "                                                     4.EXIT "
       
       ch=input("Enter your choice: ")
       if(ch==1):
           ans1="y"
           
           print 'WELCOME TO THE ADMIN ENTRY MODULE!'
           while ans1=="y":
                   print "     ||ROOM ENTRY||"
                   print "         1.ADD"
                   print "         2.DISPLAY"
                   print "         3.SEARCH"
                   print "         4.UPDATE"
                   print "         5.DELETE"
                   print "         6.EXIT"
                   choice=input("Enter the choice: ")
                   if choice==1:
                       n=input("Enter the number of rooms to be added: ")
                       for i in range(n):
                           f1=open("hotel.dat","ab")
                           l1=hotel()
                           l1.getdata()
                           pickle.dump(l1,f1)
                           f1.close()
                           print "Added!"
                       
                   elif choice==2:
                       f1=open("hotel.dat","rb")
                       l1=hotel()
                       print "|RNO.|  |RTYPE|  |ROOM ISSUED|  |ROOM ISSUED BY|"
                       print "................................................................."
                       print
                       try:
                           while True:
                               l1=pickle.load(f1)
                               l1.displaydata()
                       except EOFError:
                           pass
                       f1.close()
                       
                   elif choice==3:
                       flag=0
                       f1=open("hotel.dat","rb")
                       l1=hotel()
                       rno=input("Enter the room no. to be searched: ")
                       try:
                           while True:
                               l1=pickle.load(f1)
                               if (l1.rno==rno):
                                   l1.dispdata()
                                   flag=1
                       except EOFError:
                           pass
                       f1.close()
                       if (flag==0):
                           print
                           print "........................................."
                           print "SORRY...PLEASE ENTER THE CORRECT ROOM NO.."
                           print "........................................."
                           print
                       

                   elif choice==4:
                       f1=open("hotel.dat","rb")
                       f2=open("temp.dat","ab")
                       f2.truncate()
                       l1=hotel()
                       bno=input("Enter the room no. to be updated: ")
                       try:
                           while True:
                               l1=pickle.load(f1)
                               if l1.rno!=rno:
                                 pickle.dump(l1,f2)
                               else:
                                   l1.getdata()
                                   pickle.dump(l1,f2)
                                 
                       except EOFError:
                           pass
                       f1.close()
                       f2.close()
                       os.remove("hotel.dat")
                       os.rename("temp.dat","hotel.dat")
                       print "...................................."
                       print "           UPDATED           "
                       print "...................................."
                       

                   elif choice==5:
                       f1=open("hotel.dat","rb")
                       f2=open("temp.dat","ab")
                       f2.truncate()
                       l1=hotel()
                       rno=input("Enter the room no. to be deleted: ")
                       try:
                           while True:
                               l1=pickle.load(f1)
                               if l1.rno!=rno:
                                   pickle.dump(l1,f2)
                       except EOFError:
                           pass
                       f1.close()
                       f2.close()
                       os.remove("room.dat")
                       os.rename("temp.dat","room.dat")
                       print "...................................."
                       print "           DELETED           "
                       print "...................................."
                   elif(choice==6):
                       print"........................................."
                       print "              EXIT "
                       print"........................................."
                       break
                       
                   ans1= raw_input('Do you wish to perform any operation ---> y/n? ')
       elif(ch==2):
           ans2="y"
           
           while(ans2=="y"):
                   print "     ||HOTEL ADMINISTRATOR ENTRY DETAILS||"
                   print "         1.ADD"
                   print "         2.DISPLAY"
                   print "         3.SEARCH"
                   print "         4.UPDATE"
                   print "         5.DELETE"
                   print "         6.EXIT"
                   choice= int(raw_input('Enter your choice: '))
                   if choice==1:
                       n=input("Enter the number of the hotel administrators: ")
                       for i in range (0,n,1):
                           f3=open("hoteladmin.dat","ab")
                           l3=hoteladmin()    
                           l3.getinfo()
                           pickle.dump(l3,f3)
                           f3.close()
                           print ".........................................."
                           print"  HOTEL ADMINISTRATOR RECORD ADDED!"
                           print ".........................................."
                           
                   elif choice==2:
                       f3=open("hoteladmin.dat","rb")
                       l3=hoteladmin()
                       print "|ENO|      |HOTEL ADMINISTRATOR NAME|      |PASSWORD|"
                       print "..........................................................."
                       print
                       try:
                           while True:
                               l1=pickle.load(f3)
                               l1.displayinfo()
                       except EOFError:
                           pass
                       f3.close()
                       
                   elif choice==3:
                       f3=open("hoteladmin.dat","rb")
                       eno=input("Enter the hotel administrator id to be searched: ")
                       try:
                           while True:
                               l3=pickle.load(f3)
                               if l3.eno==eno:
                                   l3.infodate()
                       except EOFError:
                           pass
                       f3.close()
                       

                   elif choice==4:
                       f3=open("hoteladmin.dat","rb")
                       f4=open("temporary.dat","ab")
                       f4.truncate()
                       l3=hoteladmin()
                       eno=input("Enter the hotel administrator id to be updated: ")
                       try:
                           while True:
                               l3=pickle.load(f3)
                               if l3.eno!=eno:
                                   pickle.dump(l3,f4)
                               else:
                                   l3.getinfo()
                                   pickle.dump(l3,f4)
                                 
                       except EOFError:
                           pass
                       f3.close()
                       f4.close()
                       os.remove("hoteladmin.dat")
                       os.rename("temporary.dat","hoteladmin.dat")
                       print "..........................................."
                       print "              UPDATED"
                       print "..........................................."

                   elif choice==5:
                       f3=open("hoteladmin.dat","rb")
                       f4=open("temporary.dat","ab")
                       f4.truncate()
                       l3=hoteladmin()
                       eno=input("Enter the hotel administrator no to be deleted: ")
                       try:
                           while True:
                               l3=pickle.load(f3)
                               if l3.eno!=eno:
                                   pickle.dump(l3,f4)
                       except EOFError:
                           pass
                       f3.close()
                       f4.close()
                       os.remove("hoteladmin.dat")
                       os.rename("temporary.dat","hoteladmin.dat")
                       print"........................................."
                       print "              DELETED "
                       print"........................................."
                   elif(choice==6):
                       print"........................................."
                       print "        HOTEL ADMINISTRATOR EXIT "
                       print"........................................."
                       break
                   
       elif (ch==3):
           logg=0
           print "....................................."
           print "             LOG IN            "
           print "......................................"
           
           eno=input("Enter Hotel Administrator Employee No.: ")
           pwd=input("Enter password: ")
           f3=open("hoteladmin.dat","rb")
           try:
               while True:
                   l3=pickle.load(f3)
                   if ((l3.eno==eno) and (l3.pwd==pwd)):
                       print "LOGGED IN SUCCESSFULLY!"
                       logg=1
           except EOFError:
               pass
           f3.close()
                    
           if(logg==0):
               print "INVALID EMPLOYEE NO AND PWD!"
               
           ans3="y"
           while((ans3=="y" ) and (logg==1)):
               print "     1.LIST OF ROOMS AVAILABLE "
               print "     2.USER ACCOUNT"
               print "     3.ROOM ISSUE   "
               print "     4.ROOM RETURN"
               print "     5.LOG OUT"
               choice=input("Enter your choice:")
               if(choice==1):
                   print "LIST OF ROOMS "
                   f1=open("hotel.dat","rb")
                   l1=hotel()
                   print "|ROOM NO.|   |ROOM TYPE|    |ROOM ISSUED|      |ROOM ISSUED BY|"
                   print "................................................................."
                   print
                   try:
                       while True:
                           l1=pickle.load(f1)
                           if(l1.roomis=="no"):
                               l1.displaydata()
                   except EOFError:
                       pass
                   f1.close()
                   
               elif(choice==2):
                   print "ROOM DETAILS"
                   f1=open("roomissue.dat","rb")
                   r1=roomentry()
                   print "|ID NO|      |ROOM NO|    |ROOM TYPE|"
                   print "..........................................."
                   print
                   
                   
                   try:
                       while True:
                           r1=pickle.load(f1)
                           if(r1.eno==eno):
                               r1.disproomentry()
                   except EOFError:
                       pass
                   f1.close()
                   
                   
               elif(choice==3):
                   print "ROOM ISSUE"
                   f1=open("hotel.dat","rb")
                   f2=open("hoteladmin.dat","rb")
                   f3=open("roomissue.dat","ab")
                   f4=open("temp.dat","ab")
                   f4.truncate()
                   
                   l1=hotel()
                   s1=hoteladmin()
                   rno=input("Enter the room no. to be issued: ")
                   r1=roomentry()
                   try:
                       while True:
                           l1=pickle.load(f1)
                           if((l1.rno==rno) and(l1.roomis=="yes")):
                               print "SORRY...THIS ROOM IS ALREADY ISSUED..!"
                           elif((l1.rno==rno) and(l1.roomis=="no")):
                               r1.roomissuefn(eno,l1.rno,l1.rtype)
                               
                               pickle.dump(r1,f3)
                               print "ROOM ISSUED!"
                               l1.roomtakenfn(l1.rno,l1.rtype,"yes",eno)
                               pickle.dump(l1,f4)
                           else:
                               pickle.dump(l1,f4)
                           
                               
                   except EOFError:
                       pass
                   f1.close()
                   f2.close()
                   f3.close()
                   f4.close()
                   os.remove("hotel.dat")
                   os.rename("temp.dat","hotel.dat")
                   print "DATA UPDATED!"
                   
               elif(choice==4):
                   print "ROOM RELEASE"
                   f3=open("roomissue.dat","rb")
                   
                   rno=input("Enter room no. to return: ")
                   l1=roomentry()
                   l2=hotel()
                   roomfound=0
                   try:
                       while True:
                           l1=pickle.load(f3)
                           if((l1.eno==eno)and(l1.rno==rno)):
                               print "THIS ROOM IS ALREADY BOOKED!"
                               dans=raw_input("Do you want to release this room ----> y/n ")
                               dans.lower()
                               roomfound=1
                   except EOFError:
                       pass
                   f3.close()
                   
                   if((roomfound==1) and(dans=="y")):
                       f1=open("roomissue.dat","rb")
                       f2=open("temp.dat","ab")
                       f2.truncate()
                       try:
                           while True:
                               l1=pickle.load(f1)
                               if(l1.rno!=rno):
                                   pickle.dump(l1,f2)
                       except EOFError:
                           pass
                       f1.close()
                       f2.close()
                       os.remove("roomissue.dat")
                       os.rename("temp.dat","roomissue.dat")
                       print "ROOM RELEASED!"

                       f1=open("hotel.dat","rb")
                       f2=open("temp.dat","ab")
                       f2.truncate()
                       try:
                           while True:
                               l2=pickle.load(f1)
                              
                               if(l2.rno!=rno):
                                   pickle.dump(l2,f2)
                               else:
                                   l2.roomtakenfn(l2.rno,l2.rtype,"no","_")
                                   pickle.dump(l2,f2)
                                   
                       except EOFError:
                           pass
                       f1.close()
                       f2.close()
                       os.remove("hotel.dat")
                       os.rename("temp.dat","hotel.dat")
                       print "DATA UPDATED!"
                       
                   elif((roomfound==1) and(dans!="y")):
                       print "ROOM IS NOT RELEASED!"
                   elif(roomfound==0):
                       print "SORRY THIS ROOM IS ALREADY BOOKED...CHECK THE ROOM NO..! "
                   
                                   
               elif (choice==5):
                   logg=0
                   print "......................................."
                   print "              LOG OUT"
                   print "......................................."
                   

               ans3=raw_input("Do you want to continue?(y/n) ")
               ans3.lower()
           
       elif(ch==4):
           print"........................................................"
           print "            HOTEL ADMINISTRATOR EXIT "
           print"........................................................"
           break


main()
