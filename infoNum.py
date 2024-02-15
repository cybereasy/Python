print("Created by CyberEasy")
import phonenumbers 
from phonenumbers import timezone,geocoder, carrier 
num_1 = input("Enter the country code:")
num_2 = input("Enter the Number: ")
len1 = len(num_1)
len2 = len(num_2)
if len1 == 3:
    print("country code Done...")
else:
    print( "Try again...")
    exit()
if len2 == 10:
    print("country number Done...")
else:
    print(" Try again...")
    exit()
num_3 = str(num_1+num_2)
phoneNumber = phonenumbers.parse(num_3)
timeZone = timezone.time_zones_for_number(phoneNumber)
Carrier = carrier.name_for_number(phoneNumber, 'en')
Region = geocoder.description_for_number(phoneNumber, 'en')
print (num_3)
print(Carrier) 
print(Region) 
print(timeZone)
