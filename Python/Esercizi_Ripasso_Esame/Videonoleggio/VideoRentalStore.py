from Movie import Movie
from Customer import Customer

class VideoRentalStore:

    def __init__(self, movies: dict[str, Movie] = {}, customers: dict[str, Customer] = {}):
        
        self.movies = movies
        self.customers = customers

    
    def add_movie(self, movie_id: str, title: str, director: str):

        if movie_id not in self.movies:

            new_movie = Movie (movie_id, title, director)

            self.movies[movie_id] = new_movie

        else:

            raise Exception("Il film è già stato registrato")

    def register_customer(self, customer_id: str, name: str):

        if customer_id not in self.customers:

            new_customer = Customer (customer_id, name)

            self.customers[customer_id] = new_customer

        else:

            raise Exception("L'utente è già registrato")
        
    def rent_movie(self, customer_id: str, movie_id: str):

        if customer_id in self.customers and movie_id in self.movies:
            
            movie: Movie = self.movies[movie_id]

            self.customers[customer_id].rent_movie(movie)

        else:

            raise Exception ("Cliente o film non trovato")
        
    def return_movie(self, customer_id: str, movie_id: str):

        if movie_id in self.movies and customer_id in self.customers:

            movie: Movie = self.movies[movie_id]

            self.customers[customer_id].return_movie(movie)

        else:

            raise Exception("Cliente o film non trovato")

    def get_rented_movies(self, customer_id: str) -> list[Movie]:

        if customer_id in self.customers:

            return self.customers[customer_id].rented_movies
        
        else:

            raise Exception("Il cliente non esiste!")
        
    def get_all_movies(self) -> list[Movie]:

        """
        Ritorna la lista di film che sono stati dati dal videonoleggio a tutti i clienti del videonoleggio
        """

        film_noleggiati: list[Movie] = []

        for customer_id, customer in self.customers.items():

            film_noleggiati += customer.rented_movies

        return film_noleggiati

