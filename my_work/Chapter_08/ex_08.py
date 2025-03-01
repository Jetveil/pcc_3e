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

def make_album(artistName, albumName, tracksAmount=''):
    albumTotal = {'Artist': artistName.title(), 'Album': albumName.title()}
    if tracksAmount:
        albumTotal['Tracks'] = tracksAmount
    return albumTotal


while True:
    print("\nEnter artist name, album name and number of tracks (optional)")
    print("Or enter 'q' to quit")

    userArtist = input("\nEnter artist name: ")
    if userArtist == 'q':
        break
    userAlbum = input("Enter album name: ")
    if userAlbum == 'q':
        break
    userTracks = input("Enter number of tracks (optional):")
    if userTracks == 'q':
        break

    entered_album = make_album(userArtist, userAlbum, userTracks)
    print(f"\n{entered_album}")
