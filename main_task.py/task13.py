# Write a program that takes the email and password as input from a user and checks if they are equal to
# “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print
# “Invalid username or password”.
# ONLY accept 3 tries after which it notifies you that you have been blocked.
correct_email='admin@mail.com'
correct_password='Admin@123'
attempts=3
for login in range(1,4):
        email=input('enter your email: ').casefold()
        password=input('enter your password: ') 
        if email==correct_email and password==correct_password:
            print('Login successful')
            break
        else:
            remaining_attempts=attempts-login
            if remaining_attempts>0:
                print(f'invalid username or password you have {remaining_attempts} attempts remaining')
            else:
                print('you have been blocked')
   
        












    
   

        











