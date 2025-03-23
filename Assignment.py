def mainmenu():

    while True:
        print("\nMain Menu:")
        print("----------------")
        inputlogin = input("Enter login mode (A for Admin, U for User): ")
        if inputlogin == "A" or inputlogin == "a":
            adminlogin()
        elif inputlogin == "U" or inputlogin == "u":
            userchoose()


def adminlogin():

    print("\nAdmin Login:")
    print("----------------")
    inputUN = input("Enter your username:")
    inputPwd = input("Enter your password:")
    with open("adminusers.txt", 'r') as f:
        data = f.read().split("\n")

    flag = False
    for count in range(0, len(data)):
        check = data[count].split(";")
        if(inputUN == check[0] and inputPwd == check[1]):
            admin_menu()
    print("\nInvalid login details!\n")


def admin_menu():

    while True:
        print("\nAdmin Menu:")
        print("----------------")
        print("1) Hall Management")
        print("2) Booking Management")
        print("3) User Management")
        print("4) Logout")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            hall_menu()
        elif choice == '2':
            adminbookingmenu()
        elif choice == '3':
            usermanagementmenu()
        elif choice == '4':
            mainmenu()
        else:
            print("\nInvalid!\n")


def hall_menu():

    while True:
        print("\nHall Management Menu:")
        print("----------------")
        print("1) Enter Hall Information")
        print("2) View all the hall information")
        print("3) Search the hall information")
        print("4) Edit the hall information")
        print("5) Delete the hall information")
        print("6) Go back to Admin Menu")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            enterhallinfo()
        elif choice == '2':
            viewhallinfo()
        elif choice == '3':
            searchhallinfo()
        elif choice == '4':
            edithallinfo()
        elif choice == '5':
            deletehallinfo()
        elif choice == '6':
            break
        else:
            print("\nInvalid number entered!\n")


def enterhallinfo():

    print("\nEnter Hall Information")
    print("----------------")
    hallid = input("Enter Hall ID: ")
    halltype = input("Enter Hall Type: ")
    halldesc = input("Enter Hall decription: ")
    hallpax = input("Enter Hall pax: ")
    hallstatus = input("Enter Hall availability status Y/N: ")
    hallprice = input("Enter Hall rate price per day: ")
    with open("hallinfo.txt", "a") as f:
        f.write(hallid +";"+ halltype +";"+ halldesc +";"+ hallpax +";"+ hallstatus +";"+ hallprice + "\n")
    print("\nNew Hall data created!\n")


def viewhallinfo():

    print("\n\nHall Information")
    print("----------------")
    with open("hallinfo.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                print("\nHall ID:", data[0], "\nHall Type:", data[1], "\nHall Description:", data[2], "\nHall Pax:", data[3], "\nHall Availability Status:", data[4], "\nHall Rate Price:", data[5], "\n")


def searchhallinfo():

    print("\nHall Information Search")
    print("----------------")
    print("1) Hall ID")
    print("2) Hall Type")
    print("3) Hall Description")
    print("4) Hall Pax")
    print("5) Hall Availability Status")
    print("6) Hall Rate Price")
    find = int(input("\nEnter the number corresponding to what you want to search for: "))
    if find in [1,2,3,4,5,6]:
        inputfind = input("\nEnter the data you want to search for: ")
        found = False
        with open("hallinfo.txt", "r") as f:
            fulldata = f.read().split("\n")
        for count in range(0, len(fulldata)-1):
            data = []
            data = fulldata[count].split(";")
            if inputfind == data[find-1]:
                print('\nData Found!')
                found = True
                print("\nHall ID:", data[0], "\nHall Type:", data[1], "\nHall Description:", data[2], "\nHall Pax:", data[3], "\nHall Availability Status:", data[4], "\nHall Rate Price:", data[5], "\n")
        if found == False:
            print("\nData not found!\n")
    else: 
        print("\nInvalid Number\n")


def edithallinfo():

    print("\nEdit Hall Information")
    print("----------------")

    with open("hallinfo.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                print("\nHall ID:", data[0], "\nHall Type:", data[1], "\nHall Description:", data[2], "\nHall Pax:", data[3], "\nHall Availability Status:", data[4], "\nHall Rate Price:", data[5], "\n")

    edithallid = input("Enter the Hall ID of the Hall you want to edit: ")
    flag = False
    with open("hallinfo.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                if data[0] == edithallid:
                    fulldata[count] = ""
                    flag = True
    if flag == True:
        fulldata.pop(fulldata.index(""))
        with open("hallinfo.txt", "w") as f:
            f.write("")
        with open("hallinfo.txt", "a") as f:
            for count in range(0, len(fulldata)-1):
                f.write(fulldata[count] + "\n")
        
        halltype = input("\n\nEnter Hall Type: ")
        halldesc = input("Enter Hall decription: ")
        hallpax = input("Enter Hall pax: ")
        hallstatus = input("Enter Hall availability status Y/N: ")
        hallprice = input("Enter Hall rate price per day: ")
        with open("hallinfo.txt", "a") as f:
            f.write(edithallid +";"+ halltype +";"+ halldesc +";"+ hallpax +";"+ hallstatus +";"+ hallprice + "\n")
        print("\nHall Information edited successfully!\n")
    else:
        print("\nHall ID does not exist!\n")


def deletehallinfo():

    print("\nDelete Hall Information")
    print("----------------")
    with open("hallinfo.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                print("\nHall ID:", data[0], "\nHall Type:", data[1], "\nHall Description:", data[2], "\nHall Pax:", data[3], "\nHall Availability Status:", data[4], "\nHall Rate Price:", data[5], "\n")

    delhallid = input("\n\nEnter the Hall ID of the Hall you want to delete: ")
    flag = False
    with open("hallinfo.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                if data[0] == delhallid:
                    fulldata[count] = ""
                    flag = True
    if flag == True:
        fulldata.pop(fulldata.index(""))
        with open("hallinfo.txt", "w") as f:
            f.write("")
        with open("hallinfo.txt", "a") as f:
            for count in range(0, len(fulldata)-1):
                f.write(fulldata[count] + "\n")
        print("\nHall information edited successfully!\n")
    else:
        print("\nHall ID does not exist!\n")


def adminbookingmenu():

    while True:
        print("\nBooking Management Menu:")
        print("----------------")
        print("1) View all Booking Information")
        print("2) Search Booking Information")
        print("3) Edit Booking Information")
        print("4) Delete Booking Information")
        print("5) Go back to Admin Menu")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            viewbookinginfo()
        elif choice == '2':
            searchbookinginfo()
        elif choice == '3':
            editbookinginfo()
        elif choice == '4':
            deletebookinginfo()
        elif choice == '5':
            admin_menu()
        else:
            print("\nInvalid number entered!\n")


def viewbookinginfo():

    print("\n\nBooking Information")
    print("----------------")
    with open("booking.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                print("\nUsername:", data[0], "\nEvent Name:", data[1], "\nEvent Description:", data[2], "\nEvent Hall ID:", data[3], "\nEvent Pax:", data[4], "\nEvent Date:", data[5], "\nEvent Start Time:", data[6], "\nEvent End Time:", data[7], "\nBooking ID:", data[8], "\n")


def searchbookinginfo():

    print("\nBooking Information Search")
    print("----------------")
    print("1) Username")
    print("2) Event Name")
    print("3) Event Description")
    print("4) Event Hall ID")
    print("5) Event Pax")
    print("6) Event Date")
    print("7) Event Start Time")
    print("8) Event End Time")
    print("9) Booking ID")
    
    find = int(input("\nEnter the number corresponding to what you want to search for: "))
    if find in [1,2,3,4,5,6,7,8,9]:
        inputfind = input("\nEnter the data you want to search for: ")
        found = False
        with open("booking.txt", "r") as f:
            fulldata = f.read().split("\n")
        for count in range(0, len(fulldata)-1):
            data = []
            data = fulldata[count].split(";")
            if inputfind == data[find-1]:
                print('\nData Found!')
                found = True
                print("\nUsername:", data[0], "\nEvent Name:", data[1], "\nEvent Description:", data[2], "\nEvent Hall ID:", data[3], "\nEvent Pax:", data[4], "\nEvent Date:", data[5], "\nEvent Start Time:", data[6], "\nEvent End Time:", data[7], "\nBooking ID:", data[8], "\n")
        if found == False:
            print("\nData not found!\n")
    else: 
        print("\nInvalid Number\n")


def editbookinginfo():

    print("\nEdit Booking Information")
    print("----------------")

    delbookingid = input("\nEnter the Booking ID of the booking you want to edit: ")
    flag = False
    with open("booking.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                if data[8] == delbookingid:
                    fulldata[count] = ""
                    flag = True
    if flag == True:
        fulldata.pop(fulldata.index(""))
        with open("booking.txt", "w") as f:
            f.write("")
        with open("booking.txt", "a") as f:
            for count in range(0, len(fulldata)-1):
                f.write(fulldata[count] + "\n")
        
        flag = False
        while flag == False:
            username = input("\nEnter the Username for the booking: ")
            with open("users.txt", "r") as f:
                fulldata = f.read().split("\n")
                for count in range(0, len(fulldata)-1):
                    data = []
                    data = fulldata[count].split(";")
                    if data[0] == username:
                        flag = True
            if flag == False:
                print("\nUsername does not exist!\n")
            

        eventname = input("Enter the event name: ")
        eventdesc = input("Enter the event description: ")
        with open("hallinfo.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                print("\nHall ID:", data[0], "\nHall Type:", data[1], "\nHall Description:", data[2], "\nHall Pax:", data[3], "\nHall Availability Status:", data[4], "\nHall Rate Price:", data[5], "\n")

        eventhallid = input("Enter the Hall ID to host the event: ")
        flag = False
        while flag == False:
            with open("hallinfo.txt", 'r') as f:
                    data = f.read().split("\n")
            for count in range(0, len(data)-1):
                    check = data[count].split(";")
                    if(eventhallid == check[0] and check[4]== "Y"):
                        flag = True
            if flag == False:
                print("\nInvalid Hall ID!")
                eventhallid = input("\nEnter the Hall ID to host the event: ")

        eventpax = input("Enter the number of pax: ")
        flag = False
        while flag == False:
            with open("hallinfo.txt", 'r') as f:
                    data = f.read().split("\n")
            for count in range(0, len(data)-1):
                    check = data[count].split(";")
                    if(int(eventpax) <= int(check[3]) and int(eventpax) > 0 and eventhallid == check[0]):
                        flag = True
            if flag == False:
                print("\nInvalid number of pax!")
                eventpax = input("\nEnter the number of pax: ")


        eventdate = input("Enter date of the booking in the format DD/MM/YY: ")
        while len(eventdate) != 8 or int(eventdate.split("/")[0])>31 or int(eventdate.split("/")[1])>12 or int(eventdate.split("/")[2])<23:
            print("\nInvalid Date entered!\n")
            eventdate = input("Enter date of the booking in the format DD/MM/YY: ")


        eventstarttime = input("Enter the event start time in the format hh/mm: ")
        while len(eventstarttime) != 5 or int(eventstarttime.split("/")[0])>17 or int(eventstarttime.split("/")[0])<8 or int(eventstarttime.split("/")[1])>59:
            print("\nInvalid Time entered!\n")
            eventstarttime = input("Enter the event start time in the format hh/mm: ")

        eventendtime = input("Enter the event end time in the format hh/mm: ")
        while len(eventendtime) != 5 or int(eventendtime.split("/")[0])>17 or int(eventendtime.split("/")[0])<8 or int(eventendtime.split("/")[1])>59:
            print("\nInvalid Time entered!\n")
            eventendtime = input("Enter the event end time in the format hh/mm: ")

        starttime = int(eventstarttime.replace("/",""))
        endtime = int(eventendtime.replace("/",""))

        while starttime >= endtime:
            print ("\nInvalid Start time and/or End time entered!\n")

            eventstarttime = input("Enter the event start time in the format hh/mm: ")
            while len(eventstarttime) != 5 or int(eventstarttime.split("/")[0])>17 or int(eventstarttime.split("/")[0])<8 or int(eventstarttime.split("/")[1])>59:
                print("\nInvalid Time entered!\n")
                eventstarttime = input("Enter the event start time in the format hh/mm: ")

            eventendtime = input("Enter the event end time in the format hh/mm: ")
            while len(eventendtime) != 5 or int(eventendtime.split("/")[0])>17 or int(eventendtime.split("/")[0])<8 or int(eventendtime.split("/")[1])>59:
                print("\nInvalid Time entered!\n")
                eventendtime = input("Enter the event end time in the format hh/mm: ")


            starttime = int(eventstarttime.replace("/",""))
            endtime = int(eventendtime.replace("/",""))

        flag = True
        while flag == True:
            with open("booking.txt", 'r') as f:
                    data = f.read().split("\n")
                    
            for count in range(0, len(data)-1):
                check = data[count].split(";")
                checkstarttime = int(check[6].replace("/", ""))
                checkendtime = int(check[7].replace("/", ""))

                if(((eventdate == check[5]) and (eventhallid == check[3]) and ((starttime > checkstarttime and starttime < checkendtime) or (endtime > checkstarttime and endtime < checkendtime) or (starttime <= checkstarttime and endtime >= checkendtime)))):
                    flag = False

            if flag == False:
                print("\nHall is already booked in that time! \nTry again!\n\n")
                
                eventdate = input("Enter date of the booking in the format DD/MM/YY: ")
                while len(eventdate) != 8 or int(eventdate.split("/")[0])>31 or int(eventdate.split("/")[1])>12 or int(eventdate.split("/")[2])<23:
                    print("\nInvalid Date entered!\n")
                    eventdate = input("Enter date of the booking in the format DD/MM/YY: ")

                eventstarttime = input("Enter the event start time in the format hh/mm: ")
                while len(eventstarttime) != 5 or int(eventstarttime.split("/")[0])>17 or int(eventstarttime.split("/")[0])<8 or int(eventstarttime.split("/")[1])>59:
                    print("\nInvalid Time entered!\n")
                    eventstarttime = input("Enter the event start time in the format hh/mm: ")

                eventendtime = input("Enter the event end time in the format hh/mm: ")
                while len(eventendtime) != 5 or int(eventendtime.split("/")[0])>17 or int(eventendtime.split("/")[0])<8 or int(eventendtime.split("/")[1])>59:
                    print("\nInvalid Time entered!\n")
                    eventendtime = input("Enter the event end time in the format hh/mm: ")


                starttime = int(eventstarttime.replace("/",""))
                endtime = int(eventendtime.replace("/",""))

                while starttime >= endtime:
                    print ("\nInvalid Start time and/or End time entered!\n")

                    eventstarttime = input("Enter the event start time in the format hh/mm: ")
                    while len(eventstarttime) != 5 or int(eventstarttime.split("/")[0])>17 or int(eventstarttime.split("/")[0])<8 or int(eventstarttime.split("/")[1])>59:
                        print("\nInvalid Time entered!\n")
                        eventstarttime = input("Enter the event start time in the format hh/mm: ")

                    eventendtime = input("Enter the event end time in the format hh/mm: ")
                    while len(eventendtime) != 5 or int(eventendtime.split("/")[0])>17 or int(eventendtime.split("/")[0])<8 or int(eventendtime.split("/")[1])>59:
                        print("\nInvalid Time entered!\n")
                        eventendtime = input("Enter the event end time in the format hh/mm: ")


                    starttime = int(eventstarttime.replace("/",""))
                    endtime = int(eventendtime.replace("/",""))

                flag = True
            else:
                break

        with open("booking.txt", "a") as f:
            f.write(username +";"+ eventname +";"+ eventdesc +";"+ eventhallid +";"+ eventpax +";"+ eventdate +";" + eventstarttime + ";" + eventendtime + ";" + delbookingid + "\n")

        eventhours = input("\nPlease confirm the number of hours (in whole numbers) you have booked for: ")
        with open("hallinfo.txt", 'r') as f:
            data = f.read().split("\n")
            for count in range(0, len(data)-1):
                    check = data[count].split(";")
                    if(eventhallid == check[0]):
                        rate = int(check[5])
        print("\n\nBooking Updated! \n\nThe Payment Price is:", int(eventhours) * int(rate))
        print("\nYour Booking ID is:", delbookingid, "\nPlease keep the Booking ID safe for future reference\n")

    else:
        print("\n\nInvalid Booking ID enetered!\n")


def deletebookinginfo():

    print("\nDelete Booking Information")
    print("----------------")

    delbookingid = input("\nEnter the Booking ID of the booking you want to delete: ")
    flag = False
    with open("booking.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                if data[8] == delbookingid:
                    fulldata[count] = ""
                    flag = True
    if flag == True:
        fulldata.pop(fulldata.index(""))
        with open("booking.txt", "w") as f:
            f.write("")
        with open("booking.txt", "a") as f:
            for count in range(0, len(fulldata)-1):
                f.write(fulldata[count] + "\n")
        print("\nBooking deleted successfully!\n")
    else:
        print("\nBooking ID does not exist!\n")


def usermanagementmenu():

    while True:
        print("\nUser Management Menu:")
        print("----------------")
        print("1) View all User Information")
        print("2) Search User Information")
        print("3) Edit User Information")
        print("4) Delete User Information")
        print("5) Go back to Admin Menu")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            viewuserinfo()
        elif choice == '2':
            searchuserinfo()
        elif choice == '3':
            edituserinfo()
        elif choice == '4':
            deleteuserinfo()
        elif choice == '5':
            admin_menu()
        else:
            print("\nInvalid number entered!\n")


def viewuserinfo():

    print("\n\nUser Information")
    print("----------------")
    with open("users.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                print("\nUsername:", data[0], "\nPassword:", data[1], "\nFirst Name:", data[2], "\nLast Name:", data[3], "\nDate of Birth:", data[4], "\nContact:", data[5], "\nEmail:", data[6], "\n")


def searchuserinfo():

    print("\nUser Information Search")
    print("----------------")
    print("1) Username")
    print("2) Password")
    print("3) First Name")
    print("4) Last Name")
    print("5) Date of Birth")
    print("6) Contact")
    print("7) Email")
    
    find = int(input("\nEnter the number corresponding to what you want to search for: "))
    if find in [1,2,3,4,5,6,7]:
        inputfind = input("\nEnter the data you want to search for: ")
        found = False
        with open("users.txt", "r") as f:
            fulldata = f.read().split("\n")
        for count in range(0, len(fulldata)-1):
            data = []
            data = fulldata[count].split(";")
            if inputfind == data[find-1]:
                print('\nData Found!')
                found = True
                print("\nUsername:", data[0], "\nPassword:", data[1], "\nFirst Name:", data[2], "\nLast Name:", data[3], "\nDate of Birth:", data[4], "\nContact:", data[5], "\nEmail:", data[6], "\n")
        if found == False:
            print("\nData not found!\n")
    else: 
        print("\nInvalid Number\n")


def edituserinfo():

    print("\nEdit User Information")
    print("----------------")

    delusername = input("Enter the Username of the user you want to edit: ")
    flag = False
    with open("users.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                if data[0] == delusername:
                    fulldata[count] = ""
                    flag = True
    if flag == True:
        fulldata.pop(fulldata.index(""))
        with open("users.txt", "w") as f:
            f.write("")
        with open("users.txt", "a") as f:
            for count in range(0, len(fulldata)-1):
                f.write(fulldata[count] + "\n")

        password = input("Enter new Password: ")
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        dob = input("Enter Date of Birth in the format DD/MM/YYYY: ")
        while len(dob) != 10 or int(dob.split("/")[0])>31 or int(dob.split("/")[1])>12 or int(dob.split("/")[2])>2023:
            print("\nInvalid Date entered!\n")
            dob = input("Enter Date of Birth in the format DD/MM/YY: ")
        contact = input("Enter the user's current contact: ")
        email = input("Enter the user's email id: ")
        with open("users.txt", "a") as f:
            f.write(delusername +";"+ password +";"+ fname +";"+ lname +";"+ dob +";"+ contact +";"+ email + "\n")
        print("\nUser Information successfully updated!\n")
    else:
        print("\nUsername does not exist!\n")


def deleteuserinfo():

    print("\Delete User Information")
    print("----------------")

    delusername = input("Enter the Username of the user you want to delete: ")
    flag = False
    with open("users.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                if data[0] == delusername:
                    fulldata[count] = ""
                    flag = True
    if flag == True:
        fulldata.pop(fulldata.index(""))
        with open("users.txt", "w") as f:
            f.write("")
        with open("users.txt", "a") as f:
            for count in range(0, len(fulldata)-1):
                f.write(fulldata[count] + "\n")
        print("\nUser deleted successfully!\n")
    else:
        print("\nUsername does not exist!\n")


def userchoose():

    userans = input ("\nEnter R to register as a New User or Enter L to proceed to User Login: ")
    if userans == "R" or userans == "r":
        newuser()
    elif userans == "L" or userans == "l":
        userlogin()
    else:
        print("\nInvalid letter entered!\n")


def newuser():

    print("\nEnter User Information")
    print("----------------")
    flag = True
    while flag == True:
        username = input("Enter Username: ")
        with open("users.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = fulldata[count].split(";")
                if data[0] == username:
                    flag = False
        if flag == False:
            print("\nUsername already exists! \nTry again!\n")
            flag = True
        else:
            flag = False
  
    password = input("Enter Password: ")
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    dob = input("Enter Date of Birth in the format DD/MM/YYYY: ")
    while len(dob) != 10 or int(dob.split("/")[0])>31 or int(dob.split("/")[1])>12 or int(dob.split("/")[2])>2023:
        print("\nInvalid Date entered!\n")
        dob = input("Enter Date of Birth in the format DD/MM/YYYY: ")
    contact = input("Enter your current contact: ")
    email = input("Enter your email id: ")
    with open("users.txt", "a") as f:
        f.write(username +";"+ password +";"+ fname +";"+ lname +";"+ dob +";"+ contact +";"+ email + "\n")
    print("\nNew User created successfully!\n")


def userlogin():

    while True:
        print("\nUser Login:")
        print("----------------")
        global inputUN
        inputUN = input("Enter your username: ")
        inputPwd = input("Enter your password: ")
        with open("users.txt", 'r') as f:
            data = f.read().split("\n")

        for count in range(0, len(data)):
            check = data[count].split(";")
            if(inputUN == check[0] and inputPwd == check[1]):
                user_menu()
        print("\nInvalid login!\n")
        mainmenu()


def user_menu():

    while True:
        print("\n\nUser Menu:")
        print("----------------")
        print("1) Make New Booking")
        print("2) View your booking information")
        print("3) Cancel Booking")
        print("4) Edit booking information")
        print("5) Search booking information")
        print("6) Update profile information")
        print("7) Logout")
        choice = input("Enter your choice: ")
        if choice == '1':  
            newbooking()
        elif choice == '2':
            viewbooking()
        elif choice == '3':
            cancelbooking()
        elif choice == '4':
            editbooking()
        elif choice == '5':
            searchbooking()
        elif choice == '6':
            updateprofile()
        elif choice == '7':
            inputUN = ""
            mainmenu()
        else:
            print("\nInvalid!\n")


def newbooking():

    print("\nEnter new booking information")
    print("----------------")
    eventname = input("Enter the event name: ")
    eventdesc = input("Enter the event description: ")

    with open("hallinfo.txt", "r") as f:
        fulldata = f.read().split("\n")
        for count in range(0, len(fulldata)-1):
            data = []
            data = fulldata[count].split(";")
            print("\nHall ID:", data[0], "\nHall Type:", data[1], "\nHall Description:", data[2], "\nHall Pax:", data[3], "\nHall Availability Status:", data[4], "\nHall Rate Price:", data[5], "\n")

    eventhallid = input("Enter the Hall ID to host the event: ")

    flag = False
    while flag == False:
        with open("hallinfo.txt", 'r') as f:
                data = f.read().split("\n")
        for count in range(0, len(data)-1):
                check = data[count].split(";")
                if(eventhallid == check[0] and check[4]== "Y"):
                    flag = True
        if flag == False:
            print("\nInvalid Hall ID!")
            eventhallid = input("\nEnter the Hall ID to host the event: ")

    eventpax = input("Enter the number of pax: ")
    flag = False
    while flag == False:
        with open("hallinfo.txt", 'r') as f:
                data = f.read().split("\n")
        for count in range(0, len(data)-1):
                check = data[count].split(";")
                if(int(eventpax) <= int(check[3]) and int(eventpax) > 0 and eventhallid == check[0]):
                    flag = True
        if flag == False:
            print("\nInvalid number of pax!")
            eventpax = input("\nEnter the number of pax: ")

    eventdate = input("Enter date of the booking in the format DD/MM/YY: ")
    while len(eventdate) != 8 or int(eventdate.split("/")[0])>31 or int(eventdate.split("/")[1])>12 or int(eventdate.split("/")[2])<23:
        print("\nInvalid Date entered!\n")
        eventdate = input("Enter date of the booking in the format DD/MM/YY: ")

    eventstarttime = input("Enter the event start time in the format hh/mm: ")
    while len(eventstarttime) != 5 or int(eventstarttime.split("/")[0])>17 or int(eventstarttime.split("/")[0])<8 or int(eventstarttime.split("/")[1])>59:
        print("\nInvalid Time entered!\n")
        eventstarttime = input("Enter the event start time in the format hh/mm: ")

    eventendtime = input("Enter the event end time in the format hh/mm: ")
    while len(eventendtime) != 5 or int(eventendtime.split("/")[0])>17 or int(eventendtime.split("/")[0])<8 or int(eventendtime.split("/")[1])>59:
        print("\nInvalid Time entered!\n")
        eventendtime = input("Enter the event end time in the format hh/mm: ")

    starttime = int(eventstarttime.replace("/",""))
    endtime = int(eventendtime.replace("/",""))

    while starttime >= endtime:
        print ("\nInvalid Start time and/or End time entered!\n")

        eventstarttime = input("Enter the event start time in the format hh/mm: ")
        while len(eventstarttime) != 5 or int(eventstarttime.split("/")[0])>17 or int(eventstarttime.split("/")[0])<8 or int(eventstarttime.split("/")[1])>59:
            print("\nInvalid Time entered!\n")
            eventstarttime = input("Enter the event start time in the format hh/mm: ")

        eventendtime = input("Enter the event end time in the format hh/mm: ")
        while len(eventendtime) != 5 or int(eventendtime.split("/")[0])>17 or int(eventendtime.split("/")[0])<8 or int(eventendtime.split("/")[1])>59:
            print("\nInvalid Time entered!\n")
            eventendtime = input("Enter the event end time in the format hh/mm: ")


        starttime = int(eventstarttime.replace("/",""))
        endtime = int(eventendtime.replace("/",""))

    flag = True
    while flag == True:
        with open("booking.txt", 'r') as f:
                data = f.read().split("\n")
                
        for count in range(0, len(data)-1):
            check = data[count].split(";")
            checkstarttime = int(check[6].replace("/", ""))
            checkendtime = int(check[7].replace("/", ""))

            if(((eventdate == check[5]) and (eventhallid == check[3]) and ((starttime > checkstarttime and starttime < checkendtime) or (endtime > checkstarttime and endtime < checkendtime) or (starttime <= checkstarttime and endtime >= checkendtime)))):
                flag = False

        if flag == False:
            print("\nHall is already booked in that time! \nTry again!\n\n")
            
            eventdate = input("Enter date of the booking in the format DD/MM/YY: ")
            while len(eventdate) != 8 or int(eventdate.split("/")[0])>31 or int(eventdate.split("/")[1])>12 or int(eventdate.split("/")[2])<23:
                print("\nInvalid Date entered!\n")
                eventdate = input("Enter date of the booking in the format DD/MM/YY: ")

            eventstarttime = input("Enter the event start time in the format hh/mm: ")
            while len(eventstarttime) != 5 or int(eventstarttime.split("/")[0])>17 or int(eventstarttime.split("/")[0])<8 or int(eventstarttime.split("/")[1])>59:
                print("\nInvalid Time entered!\n")
                eventstarttime = input("Enter the event start time in the format hh/mm: ")

            eventendtime = input("Enter the event end time in the format hh/mm: ")
            while len(eventendtime) != 5 or int(eventendtime.split("/")[0])>17 or int(eventendtime.split("/")[0])<8 or int(eventendtime.split("/")[1])>59:
                print("\nInvalid Time entered!\n")
                eventendtime = input("Enter the event end time in the format hh/mm: ")


            starttime = int(eventstarttime.replace("/",""))
            endtime = int(eventendtime.replace("/",""))

            while starttime >= endtime:
                print ("\nInvalid Start time and/or End time entered!\n")

                eventstarttime = input("Enter the event start time in the format hh/mm: ")
                while len(eventstarttime) != 5 or int(eventstarttime.split("/")[0])>17 or int(eventstarttime.split("/")[0])<8 or int(eventstarttime.split("/")[1])>59:
                    print("\nInvalid Time entered!\n")
                    eventstarttime = input("Enter the event start time in the format hh/mm: ")

                eventendtime = input("Enter the event end time in the format hh/mm: ")
                while len(eventendtime) != 5 or int(eventendtime.split("/")[0])>17 or int(eventendtime.split("/")[0])<8 or int(eventendtime.split("/")[1])>59:
                    print("\nInvalid Time entered!\n")
                    eventendtime = input("Enter the event end time in the format hh/mm: ")


                starttime = int(eventstarttime.replace("/",""))
                endtime = int(eventendtime.replace("/",""))

            flag = True
        else:
            break

    global bookingid
    with open("bookingid", "r") as f:
        bookingid = str(int(f.read()) + 1)
    with open("bookingid", "w") as f:
        f.write(bookingid)

    with open("booking.txt", "a") as f:
        f.write(inputUN +";"+ eventname +";"+ eventdesc +";"+ eventhallid +";"+ eventpax +";"+ eventdate +";" + eventstarttime + ";" + eventendtime + ";" + bookingid + "\n")

    eventhours = input("\nPlease confirm the number of hours (in whole numbers) you have booked for: ")
    with open("hallinfo.txt", 'r') as f:
        data = f.read().split("\n")
        for count in range(0, len(data)-1):
                check = data[count].split(";")
                if(eventhallid == check[0]):
                    rate = int(check[5])
    print("\n\nBooking Updated! \n\nYour Payment Price is:", int(eventhours) * int(rate))
    print("\nYour Booking ID is:", bookingid, "\nPlease keep the booking ID safe for future reference\n")


def viewbooking():

    print("\nBooking Information")
    print("----------------")
    with open("booking.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                if data[0] == inputUN:
                    print("\nEvent Name:", data[1], "\nEvent Description:", data[2], "\nBooked Hall ID:", data[3], "\nEvent Pax:", data[4], "\nBooking Date:", data[5], "\nBooking Start Time:", data[6], "\nBooking End Time:", data[7], "\nBooking ID:", data[8],"\n")


def cancelbooking():

    print("\nBooking Cancellation")
    print("----------------")

    delbookingid = input("Enter the Booking ID of the booking you want to cancel: ")
    flag = False
    with open("booking.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                if data[8] == delbookingid and data[0] == inputUN:
                    fulldata[count] = ""
                    flag = True
    if flag == True:
        fulldata.pop(fulldata.index(""))
        with open("booking.txt", "w") as f:
            f.write("")
        with open("booking.txt", "a") as f:
            for count in range(0, len(fulldata)-1):
                f.write(fulldata[count] + "\n")
        print("\n\nBooking successfully cancelled!\n")
    else:
        print("\n\nInvalid Booking ID enetered!\n")


def editbooking():

    print("\nEdit Booking")
    print("----------------")

    delbookingid = input("Enter the Booking ID of the booking you want to edit: ")
    flag = False
    with open("booking.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                if data[8] == delbookingid and data[0] == inputUN:
                    fulldata[count] = ""
                    flag = True

    if flag == True:
        fulldata.pop(fulldata.index(""))
        with open("booking.txt", "w") as f:
            f.write("")
        with open("booking.txt", "a") as f:
            for count in range(0, len(fulldata)-1):
                f.write(fulldata[count] + "\n")
        eventname = input("Enter the event name: ")
        eventdesc = input("Enter the event description: ")

        with open("hallinfo.txt", "r") as f:
                fulldata = f.read().split("\n")
                for count in range(0, len(fulldata)-1):
                    data = []
                    data = fulldata[count].split(";")
                    print("\nHall ID:", data[0], "\nHall Type:", data[1], "\nHall Description:", data[2], "\nHall Pax:", data[3], "\nHall Availability Status:", data[4], "\nHall Rate Price:", data[5], "\n")

        eventhallid = input("Enter the Hall ID to host the event: ")
        flag = False
        while flag == False:
            with open("hallinfo.txt", 'r') as f:
                    data = f.read().split("\n")
            for count in range(0, len(data)-1):
                    check = data[count].split(";")
                    if(eventhallid == check[0] and check[4]== "Y"):
                        flag = True
            if flag == False:
                print("\nInvalid Hall ID!")
                eventhallid = input("\nEnter the Hall ID to host the event: ")

        eventpax = input("Enter the number of pax: ")
        flag = False
        while flag == False:
            with open("hallinfo.txt", 'r') as f:
                    data = f.read().split("\n")
            for count in range(0, len(data)-1):
                    check = data[count].split(";")
                    if(int(eventpax) <= int(check[3]) and int(eventpax) > 0 and eventhallid == check[0]):
                        flag = True
            if flag == False:
                print("\nInvalid number of pax!")
                eventpax = input("\nEnter the number of pax: ")


        eventdate = input("Enter date of the booking in the format DD/MM/YY: ")
        while len(eventdate) != 8 or int(eventdate.split("/")[0])>31 or int(eventdate.split("/")[1])>12 or int(eventdate.split("/")[2])<23:
            print("\nInvalid Date entered!\n")
            eventdate = input("Enter date of the booking in the format DD/MM/YY: ")


        eventstarttime = input("Enter the event start time in the format hh/mm: ")
        while len(eventstarttime) != 5 or int(eventstarttime.split("/")[0])>17 or int(eventstarttime.split("/")[0])<8 or int(eventstarttime.split("/")[1])>59:
            print("\nInvalid Time entered!\n")
            eventstarttime = input("Enter the event start time in the format hh/mm: ")

        eventendtime = input("Enter the event end time in the format hh/mm: ")
        while len(eventendtime) != 5 or int(eventendtime.split("/")[0])>17 or int(eventendtime.split("/")[0])<8 or int(eventendtime.split("/")[1])>59:
            print("\nInvalid Time entered!\n")
            eventendtime = input("Enter the event end time in the format hh/mm: ")

        starttime = int(eventstarttime.replace("/",""))
        endtime = int(eventendtime.replace("/",""))

        while starttime >= endtime:
            print ("\nInvalid Start time and/or End time entered!\n")

            eventstarttime = input("Enter the event start time in the format hh/mm: ")
            while len(eventstarttime) != 5 or int(eventstarttime.split("/")[0])>17 or int(eventstarttime.split("/")[0])<8 or int(eventstarttime.split("/")[1])>59:
                print("\nInvalid Time entered!\n")
                eventstarttime = input("Enter the event start time in the format hh/mm: ")

            eventendtime = input("Enter the event end time in the format hh/mm: ")
            while len(eventendtime) != 5 or int(eventendtime.split("/")[0])>17 or int(eventendtime.split("/")[0])<8 or int(eventendtime.split("/")[1])>59:
                print("\nInvalid Time entered!\n")
                eventendtime = input("Enter the event end time in the format hh/mm: ")

            starttime = int(eventstarttime.replace("/",""))
            endtime = int(eventendtime.replace("/",""))

        flag = True
        while flag == True:
            with open("booking.txt", 'r') as f:
                    data = f.read().split("\n")
                    
            for count in range(0, len(data)-1):
                check = data[count].split(";")
                checkstarttime = int(check[6].replace("/", ""))
                checkendtime = int(check[7].replace("/", ""))

                if(((eventdate == check[5]) and (eventhallid == check[3]) and ((starttime > checkstarttime and starttime < checkendtime) or (endtime > checkstarttime and endtime < checkendtime) or (starttime <= checkstarttime and endtime >= checkendtime)))):
                    flag = False

            if flag == False:
                print("\nHall is already booked in that time! \nTry again!\n\n")
                
                eventdate = input("Enter date of the booking in the format DD/MM/YY: ")
                while len(eventdate) != 8 or int(eventdate.split("/")[0])>31 or int(eventdate.split("/")[1])>12 or int(eventdate.split("/")[2])<23:
                    print("\nInvalid Date entered!\n")
                    eventdate = input("Enter date of the booking in the format DD/MM/YY: ")

                eventstarttime = input("Enter the event start time in the format hh/mm: ")
                while len(eventstarttime) != 5 or int(eventstarttime.split("/")[0])>17 or int(eventstarttime.split("/")[0])<8 or int(eventstarttime.split("/")[1])>59:
                    print("\nInvalid Time entered!\n")
                    eventstarttime = input("Enter the event start time in the format hh/mm: ")

                eventendtime = input("Enter the event end time in the format hh/mm: ")
                while len(eventendtime) != 5 or int(eventendtime.split("/")[0])>17 or int(eventendtime.split("/")[0])<8 or int(eventendtime.split("/")[1])>59:
                    print("\nInvalid Time entered!\n")
                    eventendtime = input("Enter the event end time in the format hh/mm: ")


                starttime = int(eventstarttime.replace("/",""))
                endtime = int(eventendtime.replace("/",""))

                while starttime >= endtime:
                    print ("\nInvalid Start time and/or End time entered!\n")

                    eventstarttime = input("Enter the event start time in the format hh/mm: ")
                    while len(eventstarttime) != 5 or int(eventstarttime.split("/")[0])>17 or int(eventstarttime.split("/")[0])<8 or int(eventstarttime.split("/")[1])>59:
                        print("\nInvalid Time entered!\n")
                        eventstarttime = input("Enter the event start time in the format hh/mm: ")

                    eventendtime = input("Enter the event end time in the format hh/mm: ")
                    while len(eventendtime) != 5 or int(eventendtime.split("/")[0])>17 or int(eventendtime.split("/")[0])<8 or int(eventendtime.split("/")[1])>59:
                        print("\nInvalid Time entered!\n")
                        eventendtime = input("Enter the event end time in the format hh/mm: ")


                    starttime = int(eventstarttime.replace("/",""))
                    endtime = int(eventendtime.replace("/",""))

                flag = True
            else:
                break

        with open("booking.txt", "a") as f:
            f.write(inputUN +";"+ eventname +";"+ eventdesc +";"+ eventhallid +";"+ eventpax +";"+ eventdate +";" + eventstarttime + ";" + eventendtime + ";" + delbookingid + "\n")

        eventhours = input("\nPlease confirm the number of hours (in whole numbers) you have booked for: ")
        with open("hallinfo.txt", 'r') as f:
            data = f.read().split("\n")
            for count in range(0, len(data)-1):
                    check = data[count].split(";")
                    if(eventhallid == check[0]):
                        rate = int(check[5])
        print("\n\nBooking Updated! \n\nYour Payment Price is:", int(eventhours) * int(rate))
        print("\nYour Booking ID is:", delbookingid, "\nPlease keep the Booking ID safe for future reference\n")

    else:
        print("\n\nInvalid Booking ID enetered!\n")   


def searchbooking():

    print("\nBooking Information Search")
    print("----------------")
    print("1) Event Name")
    print("2) Event Description")
    print("3) Hall ID")
    print("4) Number of Pax")
    print("5) Event Date")
    print("6) Event Start Time")
    print("7) Event End Time")
    print("8) Booking ID")
    find = int(input("\nEnter the number corresponding to what you want to search for: "))
    if find in [1,2,3,4,5,6,7,8]:
        inputfind = input("\nEnter the data you want to search for: ")
        found = False
        with open("booking.txt", "r") as f:
            fulldata = f.read().split("\n")
        for count in range(0, len(fulldata)-1):
            data = []
            data = fulldata[count].split(";")
            if inputfind == data[find] and inputUN == data[0]:
                print('\nData Found!')
                found = True
                print("\nEvent Name:", data[1], "\nEvent Description:", data[2], "\nHall ID:", data[3], "\nNumber of Pax:", data[4], "\nEvent Date:", data[5], "\nEvent Start Time:", data[6], "\nEvent End Time:", data[7], "\nBooking ID:", data[8],"\n")
        if found == False:
            print("\nData not found!\n")
    else: 
        print("\nInvalid Number\n")


def updateprofile():

    print("\nUpdate Profile Information")
    print("----------------")

    flag = False
    with open("users.txt", "r") as f:
            fulldata = f.read().split("\n")
            for count in range(0, len(fulldata)-1):
                data = []
                data = fulldata[count].split(";")
                if data[0] == inputUN:
                    fulldata[count] = ""
                    flag = True
    if flag == True:
        fulldata.pop(fulldata.index(""))
        with open("users.txt", "w") as f:
            f.write("")
        with open("users.txt", "a") as f:
            for count in range(0, len(fulldata)-1):
                f.write(fulldata[count] + "\n")
        
        password = input("\nEnter new Password: ")
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        dob = input("Enter Date of Birth in the format DD/MM/YYYY: ")
        while len(dob) != 10 or int(dob.split("/")[0])>31 or int(dob.split("/")[1])>12 or int(dob.split("/")[2])>2023:
            print("\nInvalid Date entered!\n")
            dob = input("Enter Date of Birth in the format DD/MM/YYYY: ")
        contact = input("Enter your current contact: ")
        email = input("Enter your email id: ")
        with open("users.txt", "a") as f:
            f.write(inputUN +";"+ password +";"+ fname +";"+ lname +";"+ dob +";"+ contact +";"+ email + "\n")
        print("\nProfile Information successfully updated!\n")

mainmenu()