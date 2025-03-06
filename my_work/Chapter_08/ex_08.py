# --- 8.2

# def favorite_book(title):
#     print(f"One of my favorite books is {title}")


# favorite_book('Alice in the Wonderland')

# --- 8.3

# def make_shirt(size, text):
#     print(f"The {size} size t-shirt with printed text: \"{text}\"")


# make_shirt(48, 'cocksucker')
# make_shirt(text='pussy_destroyer', size=38)


# --- 8.4

# def make_shirt(size='L', text='I love Python'):
#     print(f"The {size} size t-shirt with printed text: \"{text}\"")


# make_shirt()
# make_shirt(48, 'CUMMER')

# --- 8.5

# def describe_city(city, country='portugal'):
#     print(f"City {city.title()} is located in {country.title()}")


# describe_city('lissabon')
# describe_city('moscow', 'russia')
# describe_city(city='seul', country='south korea')

# --- 8.6

# def city_country(city, country):
#     location = f"{city}, {country}"
#     return location.title()


# while True:
#     print("\nEnter city name, then country name")
#     print("Or enter 'q' to quit")

#     city_name = input("\nEnter city name: ")
#     if city_name == 'q':
#         break
#     country_name = input("Enter country name: ")
#     if country_name == 'q':
#         break

#     entered_location = city_country(city_name, country_name)
#     print(f"\n{entered_location}")

# --- 8.7

# def make_album(artistName, albumName, tracksAmount=''):
#     album = {'Artist': artistName.title(), 'Album': albumName.title()}
#     if tracksAmount:
#         album['Tracks'] = tracksAmount
#     return album


# print(make_album('guf', 'pizdaland', 2))
# print(make_album('sigur ros', 'von'))

# --- 8.8

# def make_album(artistName, albumName, tracksAmount=''):
#     albumTotal = {'Artist': artistName.title(), 'Album': albumName.title()}
#     if tracksAmount:
#         albumTotal['Tracks'] = tracksAmount
#     return albumTotal


# while True:
#     print("\nEnter artist name, album name and number of tracks (optional)")
#     print("Or enter 'q' to quit")

#     userArtist = input("\nEnter artist name: ")
#     if userArtist == 'q':
#         break
#     userAlbum = input("Enter album name: ")
#     if userAlbum == 'q':
#         break
#     userTracks = input("Enter number of tracks (optional):")
#     if userTracks == 'q':
#         break

#     entered_album = make_album(userArtist, userAlbum, userTracks)
#     print(f"\n{entered_album}")

# --- 8.9


# messages = ['the conciousness', 'is', 'the truth']


# def show_messages(arg):
#     for message in arg:
#         print(message.title())


# show_messages(messages)


# --- 8.10

# messages = ['the conciousness', 'is', 'the truth']
# sent_messages = []


# def send_messages(messages, sent_messages):
#     while messages:
#         current_message = messages.pop()
#         sent_messages.append(current_message)


# def show_messages(arg):
#     for message in arg:
#         print(message.title())


# send_messages(messages, sent_messages)
# show_messages(sent_messages)

# print(messages)
# print(sent_messages)


# --- 8.11

# messages = ['the conciousness', 'is', 'the truth']
# sent_messages = []


# def send_messages(messages, sent_messages):
#     while messages:
#         current_message = messages.pop(0)
#         sent_messages.append(current_message)


# def show_messages(arg):
#     for message in arg:
#         print(message.title())


# send_messages(messages[:], sent_messages)
# show_messages(sent_messages)

# print(messages)
# print(sent_messages)


# --- 8.12

# def make_sandwich(*arg):
#     print("Sandwich toppings:")
#     for topping in arg:
#         print(f" {topping.title()}")


# make_sandwich('salad', 'chilie')
# make_sandwich('sosige')


# --- 8.13

# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first.title()
#     user_info['last_name'] = last.title()
#     return user_info


# user_profile = build_profile(
#     'dmitriy', 'ermakov', location='saint-petersburg', field='absolute')

# print(user_profile)

# --- 8.14

# def buildCar(carManufacturer, carModel, **options):
#     car_dict = {}

#     car_dict['manufactor'] = carManufacturer.title()
#     car_dict['car_model'] = carModel.title()
#     for option, v in options.items():
#         car_dict[option] = v

#     return car_dict


# carInfo = buildCar('subaru', 'impreza 1995', color='blue', drive='front-wheel')

# print(carInfo)

# --- grok extra

# def create_employee_profile(name, surname, **options):
#     """Create user profile dictionary"""
#     employee_profile_dic = {
#         'first_name': name.title(),
#         'last_name': surname.title()
#     }
#     for option, value in options.items():
#         employee_profile_dic[option] = value

#     return employee_profile_dic


# employee_profile = create_employee_profile(
#     'dim', 'erm', vacation='useless shit', age=31)

# print(employee_profile)

# --- 8.15

# from printing_func import print_models, show_models

# print_models(['geralt', 'ciri', 'ada wong'], [])
# show_models([])

# --- 8.16

# import making_pizzas
# from making_pizzas import make_pizza
# from making_pizzas import make_pizza as MP
# import making_pizzas as MP
# from making_pizzas import *

# making_pizzas.make_pizza(22, 'bbq', 'extra cheese')
# make_pizza(22, 'bbq', 'extra cheese')
# MP(22, 'bbq', 'extra cheese')
# MP.make_pizza(22, 'bbq', 'extra cheese')
# make_pizza(22, 'bbq', 'extra cheese')
