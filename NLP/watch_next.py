import spacy
nlp = spacy.load('en_core_web_md')

# open file and store descriptions in a list
with open("movies.txt", "r") as file:
    # split to get rid of Movie A etc.
    movie_list = file.readlines()

planet_hulk =  "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

def compare_movies(description):
    # read description into nlp
    model_sentence = nlp(description)

    # create variables to store highest similarity value and movie string
    suggested_movie = "None"
    highest = 0.0

    # loop through each sentence taken from the file
    for sentence in movie_list:
        # split sentence to remove Movie A : etc.
        split_sentence = sentence.split(" :")

        # compare description to split sentence
        similarity = nlp(split_sentence[1]).similarity(model_sentence)

        # update highest
        if similarity > highest:
            suggested_movie = sentence
            highest = similarity

    return suggested_movie

# call compare_movies function
print(f"Based on your viewing habits, I suggest you watch the following movie next...\n\n{compare_movies(planet_hulk)}")
