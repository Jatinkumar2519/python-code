# # import  phonenumbers
# # from phonenumbers import geocoder
# # phone_number1 = phonenumbers.parse("+9813434777")
# # phone_number2 = phonenumbers.parse("+9813462128")
# # phone_number3 = phonenumbers.parse("+8607266355")
# # phone_number4 = phonenumbers.parse("+9034543477")

# # print("\nPhone Number Location\n")
# # print(geocoder.description_for_number(phone_number1,"en"))
# # print(geocoder.description_for_number(phone_number2,"en"))
# # print(geocoder.description_for_number(phone_number3,"en"))
# # print(geocoder.description_for_number(phone_number4,"en"))



# import phonenumbers
# from text import number
# from phonenumbers import geocoder, carrier

# ch_number = phonenumbers.parse(number, "CH")
# print(geocoder.description_for_number(ch_number, "en"))

# service_provider = phonenumbers.parse(number, "RO")
# print(carrier.name_for_number(service_provider, "en")
# x = input("x: ")
# list1 = []
# mylist = []
# for i in x:
#     list1.append(i)

# for i in range(len(list1)):
#     if i % 2 == 0:
#         mylist.append(list1[i])
#     else:
#         mylist.append(list1[i].lower())
# mylist1 = ''.join(mylist)
# print(mylist1)
number = input("number: ")
import phonenumbers
form phonenumbers import geocoder
pepnumbers = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumbers,"en")
print(location)


