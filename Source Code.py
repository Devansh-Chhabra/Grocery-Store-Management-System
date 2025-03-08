import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='123654',database='grocery_shop')

if conn.is_connected():
    print('successfully connected')
else:
    print('ERROR in establishing connection')

c=conn.cursor()

print('grocery shop management system')
while True:
    print('1 Login')
    print('2 Exit')

    choice=int(input('enter your choice: '))

    if choice==1:
        user_name=input('enter your user name = ')
        password=input('enter your password = ')
        if user_name=='devansh' and password=='123654':
             print('connected successfully')
             print('grocery shop')
             print('1 Customer Details')
             print('2 Product Details')
             print('3 Worker Details')
             print('4 See all Customer Details')
             print('5 See all Product Details')
             print('6 See all Worker Details')
             print('7 See one Customer Detail')
             print('8 See one Product Detail')
             print('9 See one Worker Detail')
             print('10 Stocks')
             print('11 Pie Chart for availability of Stock')
             
             choice=int(input('enter the choice '))
    
             if choice==1:
                 print("Enter Customer Details")
                 while True:
                     cust_name=input('enter your name = ')
                     phone_no=int(input('enter your  phone number = '))
                     amount=float(input('enter your amount =  '))
                     sql_insert="insert into customer_details values('"+(cust_name)+"',"+str(phone_no)+","+str(amount)+")"
                     c.execute(sql_insert)
                     conn.commit()
                     print('data is updated')
                     x=int(input("Press 1 to enter more records, Press 2 to exit  "))
                     if x==2:
                         break
                     elif x==1:
                         print("Enter Again")
                     else:
                         print("Incorrect Option")

             elif choice==2:
                  print("Enter Product Details")
                  while True:
                      product_name=input('enter  product name = ')
                      product_brand=input('enter product brand = ')
                      product_cost=float(input('enter the cost = '))
                      sql_insert="insert into product_details values(""'"+(product_name)+"',""'"+(product_brand)+"',"+str(product_cost)+")"
                      c.execute(sql_insert)
                      conn.commit()
                      print('data is updated')
                      x=int(input("Press 1 to enter more records, Press 2 to exit  "))
                      if x==2:
                          break
                      elif x==1:
                         print("Enter Again")
                      else:
                          print("Incorrect Option")
            
             elif choice==3:
                  print("Enter Worker Details")
                  while True:
                      name=input('enter your name = ')
                      designation=input('enter your work = ')
                      age=int(input('enter your  age = '))
                      salary=float(input('enter your salary = '))
                      phone_no =int(input('enter your  phone number = '))
                      sql_insert="insert into worker_details values(" "'"+(name)+"'," "'"+(designation)+"',"+str(age)+","+str(salary)+","+str(phone_no)+ ")"
                      c.execute(sql_insert)
                      conn.commit()
                      print('data is updated')
                      x=int(input("Press 1 to enter more records, Press 2 to exit  "))
                      if x==2:
                          break
                      elif x==1:
                         print("Enter Again")
                      else:
                          print("Incorrect Option")
            
             elif choice==4:
                t=conn.cursor()
                t.execute('select * from customer_details')
                record=t.fetchall()
                for i in record:
                    print(i)
                
             elif choice==5:
                t=conn.cursor()
                t.execute('select * from product_details')
                record=t.fetchall()
                for i in record:
                    print(i)
                
                
             elif choice==6:
                t=conn.cursor()
                t.execute('select * from worker_details')
                record=t.fetchall()
                for i in record:
                    print(i)
                
             elif choice==7:
                  print("Enter Customer Name")
                  while True:
                      a=input('enter your name = ') 
                      t='select * from customer_details where cust_name=("{}")'.format(a)
                      c.execute(t)
                      v=c.fetchall()
                      if len(v)==0:
                          print("Not Registered")
                      for i in v:
                          print(v)
                      x=int(input("Press 1 to retrieve more records, Press 2 to exit "))
                      if x==2:
                          break
                      elif x==1:
                          print("Enter Again")
                      else:
                          print("Incorrect Option")
                          exit()
                      
             elif choice==8:
                 print("Enter Product Name")
                 while True:
                     a=input('enter your product_name = ')
                     t='select * from product_details where product_name=("{}")'.format(a)
                     c.execute(t)
                     v=c.fetchall()
                     if len(v)==0:
                         print("Not Available")
                     for i in v:
                         print(v)
                     x=int(input("Press 1 to retrieve more records, Press 2 to exit  "))
                     if x==2:
                         break
                     elif x==1:
                         print("Enter Again") 
                     else:
                         print("Incorrect Option")
             
             elif choice==9:
                 print("Enter Worker Name")
                 while True:
                     a=input('enter your name = ')
                     t='select * from worker_details where name=("{}")'.format(a)
                     c.execute(t)
                     v=c.fetchall()
                     if len(v)==0:
                          print("Not Registered")
                     for i in v:
                         print(v)
                     x=int(input("Press 1 to retrieve more records, Press 2 to exit  "))
                     if x==2:
                         break
                     elif x==1:
                         print("Enter Again")   
                     else:
                         print("Incorrect Option")
           
             elif choice==10:
                print('******************************************')
                f=open("Stock.txt","r")
                data=f.read()
                print(data)
                f.close()
                print('******************************************')
            
             elif choice==11:
                import matplotlib.pyplot as plt
                items=('Shoes','Stationary','Watch','Household','Food Items')
                avalibility=[156,200,103,206,196]
                colors=['red','green','blue','cyan','yellow']
                plt.pie(avalibility,labels=items,colors=colors)
                plt.title('Avalibility of items in Shop')
                plt.savefig("x.png")
                plt.show()
            
             else:
                 print("Wrong Option! try again")
             
        else:
            print("Wrong Details! try again")
        
    elif choice==2:
            exit()  
    else:
        print('Wrong Choice! try again')
        x=int(input("Press 1 to restart the program, Press 2 to exit  "))
        if x==2:
            exit()
        elif x==1:
            print("Enter Again")   
        else:
            print("Incorrect Option")
