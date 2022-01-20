import json
import os
main_dict={}
list=[]
dic_out={}
user_info={}
if os.path.exists("userdetails.json"):
    pass
else:
    create=open("userdetails.json","w+")
    create.close()
choose = int(input("choose 1. for sign up or 2. for log in="))
if choose == 1:
    name=input("enter your first and last name__=")
    print(name)
    pas=input("enter your password (password should conatain Upper,Small Letter, Special Character and number)=")
    u,l,d,s=0,0,0,0
    for check in pas:
        if (check.isupper()):
            u+=1
        if (check.isdigit()):
            d+=1
        if (check.islower()):
            l+=1
        if(check=='@'or check=='$' or check=='_' or check=='#'):
            s+=1
    try:
        with open("userdetails.json","r") as output:
            user_data=json.load(output)
            for info in user_data["user"]:
                pass
    except:
        pass
    if (l>=1 and u>=1 and s>=1 and d>=1 and l+s+u+d==len(pas)):
        pas1=input("enter your password again=")
        if pas==pas1: 
            if  os.stat("userdetails.json").st_size==0:
                print("Congracts",name,"You are signed up Succesfully","\U0001F929")
                description=input("Enter your Description=")
                birth_date=input("enter Your Date Of Birth=")
                Gender=input("enter your Gender=")
                hobbies=input("Enter Your hobby=")
                try:
                    user_info["description" ]=description
                    user_info["d_o_b"]=birth_date
                    user_info["Gender"]=Gender
                    user_info["Hobbies"]=hobbies
                    dic_out["Username"]=name
                    dic_out["Password"]=pas
                    dic_out["Profile"]=user_info
                    list.append(dic_out)
                    main_dict["user"]=list
                    with open("userdetails.json","r+") as file:
                        read_file= file.read()
                        userdata=json.loads(read_file)
                        for i in userdata:
                            if i =="user":
                                x=userdata[i]
                                x.append(dic_out.copy())
                                main_dict["user"]=x
                                json.dumps(main_dict,file)
                                file.close()
                except:
                    with open("userdetails.json","w") as f:
                        f.write(json.dumps(main_dict, indent=2))
            else:
                if info["Username"]!= name  or info["Password"]!= pas:
                    print("Congracts",name,"You are signed up Succesfully","\U0001F929")
                    description=input("Enter your Description=")
                    birth_date=input("enter Your Date Of Birth=")
                    Gender=input("enter your Gender=")
                    hobbies=input("Enter Your hobby=")
                    try:
                        user_info["description"]=description
                        user_info["d_o_b"]=birth_date
                        user_info["Gender"]=Gender
                        user_info["Hobbies"]=hobbies
                        dic_out["Username"]=name
                        dic_out["Password"]=pas
                        dic_out["Profile"]=user_info
                        list.append(dic_out)
                        main_dict["user"]=list
                        with open("userdetails.json","r+") as file:
                            read_file= file.read()
                            userdata=json.loads(read_file)
                            for i in userdata:
                                if i =="user":
                                    x=userdata[i]
                                    x.append(dic_out.copy())
                                    main_dict["user"]=x
                                    json.dumps(main_dict,file)
                                    file.close()
                    except:
                        with open("userdetails.json","w") as f:
                            f.write(json.dumps(main_dict, indent=4))
                else:
                    print("Your account is already Exsist!")
        else:
            print("both password are not same")
    else:
        print("At least password should contain one Specail number or one digit")

elif choose==2:
    user_name=input("enter your username=")
    log_in_password=input("enter your Log in Password=")
    with open("userdetails.json","r") as log_in_file:
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