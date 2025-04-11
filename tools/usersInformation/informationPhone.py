import phonenumbers # парсить номер телефона жертвы
from phonenumbers import timezone
from phonenumbers import geocoder, carrier

def TimeZone(phone):
    phone = phone
    number = phonenumbers.parse(phone) 

    timeZone = timezone.time_zones_for_number(number) 

    print(number)
    print("".join(timeZone))

def RegionAndOption(phone):
    phone = phone
    x = phonenumbers.parse(phone) 

    Carrier = carrier.name_for_number(x, "ru") 

    Region = geocoder.description_for_number(x, "ru") 

    print(Carrier)
    print(Region)

def validNumbers(phone):
    phone = phone
    x = phonenumbers.parse(phone)
    valid = phonenumbers.is_valid_number(x) 

    posible = phonenumbers.is_possible_number(x) 

    print(valid)
    print(posible)