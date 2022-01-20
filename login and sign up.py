import json
import os
main_dict={}
dic_out={}
user_info={}
list1=[]
if os.path.exists("loginoutput.json"):
    pass
else:
    create=open("loginoutput.json","w+")
    create.close()
choose = int(input("choose 1. for Sign UP 2. for log in:"))
if choose == 1:
    name=input("enter your first and last name__:")
    print(name)
    password=input("enter your password (password should conatain Upper,Small Letter, Special Character and number)=")
    Upper,lower,digit,Special_chr=0,0,0,0
    for check in password:
        if (check.isupper()):
            Upper+=1
        if (check.islower()):
            lower+=1
        if (check.isdigit()):
            digit+=1
        if(check=='@'or check=='$' or check=='&' or check=='#'):
            Special_chr+=1
       
    try:
        with open("loginoutput.json","r") as output:
            user_data=json.load(output)
            for info in user_data["user"]:
                pass
    except:
        pass
    if (lower>=1 and Upper>=1 and Special_chr>=1 and digit>=1 and Upper+lower+Special_chr+digit==len(password)):
        password1=input("enter your password again:")
        if password==password1:
            if  os.stat("loginoutput.json").st_size==0:
                print("Congracts",name,"You are signed up Succesfully","\U0001F929")
                description=input("Enter your Description:")
                birthday_date=input("enter Your Date Of Birth:")
                Gender=input("enter your Gender:")
                hobbies=input("Enter Your hobbies:")
                try:
                    user_data["description" ]=description
                    user_data["d_o_b"]=birthday_date
                    user_data["Gender"]=Gender
                    user_data["Hobbies"]=hobbies
                    dic_out["Username"]=name
                    dic_out["Password"]=password
                    dic_out["Profile"]=user_info
                    list1.append(user_data)
                    main_dict["user"]=list1
                    with open("loginoutput.json","r+") as file:
                        read_file= file.read()
                        userdata=json.loads(read_file)
                        for i in userdata:
                            if i =="user":
                                x=userdata[i]
                                x.append(user_data.copy())
                                main_dict["user"]=x
                                json.dumps(main_dict,file)
                                file.close()
                except:
                    with open("loginoutput.json","w") as f:
                        f.write(json.dumps(main_dict, indent=2))
            else:
                if  info["username"]!=name or info["password"]!=password:
                    print("congrats",name,"your are singed up succesfully","\U0001F929")
                    description=input("Enter your Description:")
                    birthday_date=input("Enter your Date of birth:")
                    Gender=input("Enter your gender:")
                    hobbies=input("Enter your hobby:")
                    try:
                        user_data["description" ]=description
                        user_data["d_o_b"]=birthday_date
                        user_data["Gender"]=Gender
                        user_data["Hobbies"]=hobbies
                        dic_out["Username"]=name
                        dic_out["Password"]=password
                        dic_out["Profile"]=user_info
                        list1.append(user_data)
                        main_dict["user"]=list1
                        with open("loginoutput.json","r+") as file:
                            read_file= file.read()
                            userdata=json.loads(read_file)
                            for i in userdata:
                                if i =="user":
                                    x=userdata[i]
                                    x.append(user_data.copy())
                                    main_dict["user"]=x
                                    json.dumps(main_dict,file)
                                    file.close()
                    except:
                        with open("loginoutput.json","w") as f:
                            f.write(json.dumps(main_dict, indent=2))
                    else:
                        print("Your account is already Exsist!")
        else:
            print("both password are not same")
    else:
        print("At least password should contain one Specail number or one digit")
elif choose==2:
    user_name=input("enter your username:")
    log_in_password=input("enter your Log in Password:")
    with open("loginoutput.json","r") as log_in_file:
        log_in_info=json.load(log_in_file)
        for output_data in log_in_info["user"]:
            if output_data["Username"] == user_name and output_data["Password"]==log_in_password:
                print(user_name+ "You Logged In Succesfully","\U0001F929")
                print("................")
                print("     PROFILE       ")
                print("................")
                print("Username",":",output_data["Username"])
                print("Gender",":",output_data["Profile"]["Gender"])
                print("Bio",":",output_data["Profile"]["description"])
                print("Dob",":",output_data["Profile"]["d_o_b"])
                break
        else:
            print("Password and same")