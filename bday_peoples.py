import datetime
import random
import pandas as pd
import time
import sys

excel_file_path = r"D:\Projects'23\Bday Final\test1.xlsx"
df = pd.read_excel(excel_file_path)

def get_birthday_info(df):
    today = datetime.datetime.now()
    name = df['NAME']
    date = df['DOB']
    year = df['YEAR']
    numbers = df['NUMBER']
    age = []  
    bday_numbers = []  
    bday_wishes = []

    thisyear = today.strftime("%Y")
    dob_input = today.strftime("%d/%m")

    for k in year:  # age
        ageyear = int(thisyear) - k
        age.append(ageyear)

    for i, j in enumerate(date):  
        if dob_input == j:
            store = i
            print(f"Today's Birthday is for {name[store]}")
            print(f"Recipient age is {age[store]}")
            print("Make sure to leave a birthday wish!!!\n")
            number_store = numbers[store]
            bday_numbers.append(number_store)
            message = [
                f"Wishing you a very happy birthday {name[store]}! May all your dreams come true on this auspicious {age[store]}th birthday",
                f"{age[store]}th is a perfect age {name[store]} You're just old enough to recognize your mistakes, but still young enough to make some more. Happy Birthday!",
                f"Congratulations {name[store]} on your {age[store]}th birthday! Wishing you a truly fabulous day."
            ]
            rd_msg = random.choices(message)
            bday_wishes.append(rd_msg)
            time.sleep(2)

    if bday_numbers and bday_wishes =='\0':
        print("No birthday wishes to wish")
        print("Thank You for your time...CLosing services")
        time.sleep(3)
        sys.exit()

def only_infos(df):
    today = datetime.datetime.now()
    name = df['NAME']
    date = df['DOB']
    year = df['YEAR']
    numbers = df['NUMBER']
    age = []  # calculating age
    bday_numbers = []  # to store birthday people numbers
    bday_wishes = []
    thisyear = today.strftime("%Y")
    dob_input = today.strftime("%d/%m")
    for k in year:  # age
        ageyear = int(thisyear) - k
        age.append(ageyear)
    for i, j in enumerate(date):  # fetching who's bday
        if dob_input == j:
            store = i
            number_store = numbers[store]
            bday_numbers.append(number_store)
            message = [
                f"Wishing You A Very Happy Birthday {name[store]}! May All Your Dreams Come True On This Auspicious {age[store]}th Birthday",
                f"{age[store]}th Is A Perfect Age {name[store]}. You're Just Old Enough To Recognize Your Mistakes, But Still Young Enough To Make Some More. Happy Birthday!",
                f"Congratulations {name[store]} On Your {age[store]}th Birthday! Wishing You A Truly Fabulous Day."
            ]
            rd_msg = random.choice(message)
            bday_wishes.append(rd_msg)         
    return bday_numbers, bday_wishes

