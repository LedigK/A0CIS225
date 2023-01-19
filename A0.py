# I used chat gpt to start the program off with opening a file. It has been over
# a year since I used python, so I needed a refresher.
# I fixed the program and ran it a few times, and it worked for me.


file_name = "A0.txt"

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

def user_exists(file_name, first_name, last_name):
    with open(file_name, "r") as file:
        for line in file:
            user_info = line.strip().split(",")
            if user_info[0] == first_name and user_info[1] == last_name:
                return True
    return False

def user_does_not_exist(file_name, first_name, last_name, movies):
    with open(file_name, "a") as file:
        for movie in movies:
            file.write(f"{first_name},{last_name},{movie['title']},{movie['director']},{movie['year']},{movie['imdb']},{movie['rotten']},{movie['mpaa']}\n")

def display_user(file_name, first_name, last_name):
    with open(file_name, "r") as file:
        for line in file:
            user_info = line.strip().split(",")
            if user_info[0] == first_name and user_info[1] == last_name:
                print("First Name:", user_info[0])
                print("Last Name:", user_info[1])
                print("Movie Title:", user_info[2])
                print("Director:", user_info[3])
                print("Year Released:", user_info[4])
                print("IMDB Rating:", user_info[5])
                print("Rotten Tomatoes Rating:", user_info[6])
                print("MPAA Rating:", user_info[7])


if user_exists(file_name, first_name, last_name):
    display_user(file_name, first_name, last_name)
else:
    movies = []
    for i in range(5):
        title = input("Please enter the title of your favorite movie: ")
        director = input("Please enter the director of the movie: ")
        year = input("Please enter the year the movie was released: ")
        imdb = input("Please enter the IMDB rating for the movie: ")
        rotten = input("Please enter the Rotten Tomatoes rating percent out of 100: ")
        mpaa = input("Please enter the MPAA rating for the movie (PG, PG-13, R, etc.): ")

        movie = {
            "title": title,
            "director": director,
            "year": year,
            "imdb": imdb,
            "rotten": rotten,
            "mpaa": mpaa
        }
        movies.append(movie)

    user_does_not_exist(file_name, first_name, last_name, movies)
    print("Your movie data has been saved")
