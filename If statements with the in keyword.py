movies_watched = {"the matrix", "green book", "her"}
user_movie = input("Enter something you have watched recently: ").lower()

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that one.")
