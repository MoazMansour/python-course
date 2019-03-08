import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","Alive toys in an adventure","http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc&frags=pl%2Cwn")

avatar = media.Movie("Avatar","Fight for fredoom","http://boomstickcomics.com/wp-content/uploads/2014/06/another-avatar.jpg","https://www.youtube.com/watch?v=6ziBFh3V1aM&frags=pl%2Cwn")

braveheart = media.Movie("Brave Heart","Scotland fighting for its freedom","https://upload.wikimedia.org/wikipedia/en/thumb/5/55/Braveheart_imp.jpg/220px-Braveheart_imp.jpg","https://www.youtube.com/watch?v=1NJO0jxBtMo&frags=pl%2Cwn")

movies = [toy_story, avatar, braveheart]

#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__module__)
print(media.Movie.__name__)
