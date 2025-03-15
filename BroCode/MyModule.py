
# __name__ is a special built-in dunder variable that displays __main__ when the script is directly run and it displays the name of the script when the script is imported and run from another script. 


from datetime import datetime

current_hour = int(datetime.now().strftime("%H"))


def greetUser(user_name):

    # 00 - 11   Morning
    # 12 - 16   Noon 
    # 17 - 20   Evening
    # 21 - 23   Night

    if 00 <= current_hour <=11:
        salutation = "Good Morning!"
    elif 12 <= current_hour <= 16:
        salutation = "Good AfterNoon"
    elif 17 <= current_hour <= 20:
        salutation = "Good Evening"
    else:  # 21 - 23
        salutation = "Good Night"
        
    print(f"{salutation}, {user_name}")



def main():
    user = input("Enter your name: ")
    greetUser(user)



if __name__ == "__main__":
    main()