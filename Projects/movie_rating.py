# Check whether the movie exists.
# If it exists, determine its rating using its index.
#
# If rating >= 9 → "Excellent"
# elif rating >= 8 → "Very Good"
# else → "Good"
#
# Otherwise → "Movie not found"

print("================================")
print("        MOVIE RATING            ")
print("================================")

movies = ("Interstellar", "Inception", "Avatar")
ratings = (9, 8, 7)

movie = input("Enter movie name: ")

if movie in movies:
    rating_index = movies.index(movie) 
    if(ratings[rating_index] >= 9):
        print("Exellent")
    elif(ratings[rating_index] >= 8):
        print("Very Good")
    else:
        print("Good")
else:
    print("Movie not found")