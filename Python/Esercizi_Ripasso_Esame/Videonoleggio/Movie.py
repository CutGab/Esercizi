class Movie:

    def __init__(self, movie_ID: str, title: str, director: str, is_rented: bool):

        self.movie_ID = movie_ID
        self.title = title
        self.director = director
        self.is_rented = is_rented


    def rent(self):

        if self.is_rented == False:

            self.is_rented == True

        else:

            raise Exception(f"Il film {self.title} è già stato noleggiato.")
        

    def return_movie(self):

        if self.is_rented == True:

            self.is_rented == False

        else:

            raise Exception(f"Il film {self.title} non è stato noleggiato da questo utente.")