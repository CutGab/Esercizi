from Movie import Movie

class Customer:

    def __init__(self, customer_id: str, name: str):

        self.customer_id = customer_id
        self.name = name
        self.rented_movies : list[Movie] = []


    def rent_movie(self, movie:Movie):

        if movie.is_rented == False:
            
            self.rented_movies.append(movie)
            movie.rent()


        else:

            raise Exception(f"Il film {movie.title} è già stato noleggiato.")
        
    
    def return_movie(self, movie:Movie):

        if movie in self.rented_movies:

            self.rented_movies.remove(movie)
            movie.return_movie()

        else:
            raise Exception(f"Il film {movie.title} non è stato noleggato da questo utente.")
        

