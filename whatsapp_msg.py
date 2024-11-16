import pywhatkit
import pyautogui
import time
 
def whatsapp_bot(bday_numbers, bday_wishes):
    country_code = '+'  
    hour = int(input("Enter Hour to send [24hr Format][Don't use 0 before hour]: "))
    minute = int(input("Enter Minute to send[Don't use 0 before minute]: "))
    if minute==60:
            hour=hour+1
            minute=0
    minute = minute + 2
    n=len(bday_numbers)
    minute_estimator=n+2
    print("\n")
    print(f"APPROXIMATED ESTIMATED TIME TO FINISH : {hour}:{minute_estimator}")
    time.sleep(1)

    image_bday = r"bday_wish1.jpg"

    for number, msg in zip(bday_numbers, bday_wishes):
        try:
            full_number = country_code + str(number)
            print(f"Message is scheduled for {full_number}")
            pywhatkit.sendwhatmsg(full_number, msg, hour, minute, 15, True, 2)
            pywhatkit.sendwhats_image(full_number, image_bday)
            time.sleep(3)
            print(f"Message delivered successfully for {full_number}")
            print("\n")
            pyautogui.hotkey('ctrl', 'w')
        except Exception as e:
             print(f"Failed to send a message to {number}: {str(e)}")
        minute = minute + 1
    


