"""
A program with a dictionary to store a movie record
"""

# create movie database
movie = {
  "title": "The GodFather",
  "director" : "Francis Ford Coppola",
  "year": 1972,
  "rating": 9.2
}

# accessing some info from database
print(movie["year"])

# changing some data; updating in place
movie["rating"] = (movie["rating"] + 9.3) / 2
print(movie["rating"])

# add more data
movie["actors"] = ["Marlon Brando", "Al Pacino", "James Caan"]
movie["other_details"] = {
  "runtime": 175,
  "language": "English"
}

# print out new movie
print(movie)