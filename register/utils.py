from django.contrib.auth.models import User
from data.models import ContactsItem

character_numbers = {
    "A": 141,
    "B": 282,
    "C": 423,
    "D": 564,
    "E": 705,
    "F": 846,
    "G": 987,
    "H": 1128,
    "I": 1269,
    "J": 1410,
    "K": 1551,
    "L": 1692,
    "M": 1833,
    "N": 1974,
    "O": 2115,
    "P": 2256,
    "Q": 2397,
    "R": 2538,
    "S": 2679,
    "T": 2820,
    "U": 2961,
    "V": 3102,
    "W": 3243,
    "X": 3384,
    "Y": 3525,
    "Z": 3666,
    "Ä": 3807,
    "Ö": 3948,
    "Ü": 4089,
    "ß": 4230,
}


def convert_to_three_digit_hex(number):
    hex_value = hex(number)[2:]
    hex_value = hex_value.zfill(3)
    return hex_value


def create_background_color(first_letter, second_letter):
    hexcode1 = convert_to_three_digit_hex(character_numbers[first_letter])
    hexcode2 = convert_to_three_digit_hex(character_numbers[second_letter])
    return '#' + hexcode1 + hexcode2
    

def create_Contact(ident):
        try:
            user = User.objects.get(id=ident)
            user_dic = create_contact_dic(user, ident)
            ContactsItem.objects.create(**user_dic)
            print("User found:", user)
        except User.DoesNotExist:
            print("User not found for user_id:", ident)
            
            
def create_user_dic(request):
    user_dic = {
        "first_name": request.data.get('firstname'),
        "last_name": request.data.get('lastname'),
        "email": request.data.get('email'),
        "password": request.data.get('password'),
        "username": request.data.get('username'),
    }
    return user_dic


def create_contact_dic(user, ident):
    contact_dic = {
        "id_user": ident,
        "username": user.username,
        "email": user.email,
        "firstname": user.first_name,
        "lastname": user.last_name,
        "name_abbreviation": user.first_name[0] + user.last_name[0],
        "background_color": create_background_color(user.first_name[0], user.last_name[0] ),
        "checked": False,
        "phone": '',
        "has_account": True,
    }
    return contact_dic
