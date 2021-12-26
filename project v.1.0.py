list_of_media: dict[str, dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]] = {
    'movie_id_1': {'title': 'Mask', 'year': '2001', 'genre': 'comedy', 'rating': 0},
    'movie_id_2': {'title': 'Titanic', 'year': '1996', 'genre': 'drama', 'rating': 0},
    'movie_id_3': {'title': 'Screem', 'year': '2003', 'genre': 'horror', 'rating': 0},
    'movie_id_4': {'title': 'Matrix', 'year': '2003', 'genre': 'action', 'rating': 0},
}

list_of_users = {
    'user_1': 'tom',
    'user_2': 'mary',
    'user_3': 'bob',
}

movies_and_users = {
    'user_1': {'watched_movies': ['movie_id_1', 'movie_id_2', 'movie_id_3'],
               'favourite': ['movie_id_1', 'movie_id_2'],
               'liked_movies': ['movie_id_1', 'movie_id_2'],
               'planed_to_watch': ['movie_id_4']
               },
    'user_2': {'watched_movies': ['movie_id_2', 'movie_id_3', 'movie_id_4'],
               'favourite': ['movie_id_4'],
               'liked_movies': ['movie_id_4'],
               'planed_to_watch': ['movie_id_1']
               },
    'user_3': {'watched_movies': ['movie_id_2', 'movie_id_3', 'movie_id_4'],
               'favourite': ['movie_id_4'],
               'liked_movies': ['movie_id_2'],
               'planed_to_watch': ['movie_id_1']
               }
}


def looking_for():
    user = input('whom are you looking for?: ')
    return user


def is_member(name):
    return name in list_of_users.values()


def get_user_id(name):
    user_key = ''.join([k for k, v in list_of_users.items() if v == name])
    return (user_key)


def choose(user_id):
    action = input('Choose what you want to watch: ')
    if action == 'all':
        # красиво вывести только все titles
        return list_of_media
    elif action == 'fav':
        # ошибка если в списке больше чем 1 фильм
        return list_of_media[''.join(movies_and_users[user_id]['favourite'])]['title']
    elif action == 'liked':
        # #ошибка если в списке больше чем 1 фильм
        return list_of_media[''.join(movies_and_users[user_id]['liked_movies'])]['title']


def actions_with_movie(user_id):
    movie = input('Choose the movie: ')
    act = input('What you want to do with this movie? ')
    if act == 'fav':
        add_to_favourite(movie, user_id)
    if act == 'watch':
        add_to_watched(movie, user_id)
    if act == 'plan':
        add_to_planed(movie, user_id)
    if act == 'like':
        like_movie(movie, user_id)
    if act == 'not fav':
        del_from_favourite(movie, user_id)
    if act == 'not plan':
        del_from_planed(movie, user_id)
    if act == 'not like':
        unlike_movie(movie, user_id)


def get_movie_id(movie):
    movie_id = []
    for i in list_of_media.keys():
        movie_attributes = list_of_media[i]
        if [k for k, v in movie_attributes.items() if v == movie]:
            movie_id = i
            break
    return movie_id


def add_to_watched(movie, user_id):
    movie_id = get_movie_id(movie)
    if movie_id not in movies_and_users[user_id]['watched_movies']:
        list_of_watched = movies_and_users[user_id]['watched_movies']
        list_of_watched.append(movie_id)
        movies_and_users[user_id].update({'watched_movies': list_of_watched})
        print(f"{movie} is now in your watched movies")
        if movie_id in movies_and_users[user_id]['planed_to_watch']:
            list_of_planed = movies_and_users[user_id]['planed_to_watch']
            list_of_planed.remove(movie_id)
            movies_and_users[user_id].update({'planed_to_watch': list_of_planed})
    else:
        print("You have already watched this movie")
    print(f'Your list of movies: {movies_and_users[user_id]}')


def add_to_favourite(movie, user_id):
    movie_id = get_movie_id(movie)
    if movie_id not in movies_and_users[user_id]['favourite']:
        list_of_favourites = movies_and_users[user_id]['favourite']
        list_of_favourites.append(movie_id)
        movies_and_users[user_id].update({'favourite': list_of_favourites})
        print(f"Your list of movies: {movies_and_users[user_id]}")
        print(f"{movie} is in your favourites now")
    else:
        print('This movie is already in your favourites')


def add_to_planed(movie, user_id):
    movie_id = get_movie_id(movie)
    if movie_id not in movies_and_users[user_id]['planed_to_watch']:
        list_of_planed = movies_and_users[user_id]['planed_to_watch']
        list_of_planed.append(movie_id)
        movies_and_users[user_id].update({'planed_to_watch': list_of_planed})
        print(f"{movie} is now in your planed_to_watch movies")
        print(f"Your movies: {movies_and_users[user_id]}")
    else:
        print("You've already planed to watch this movie")


def like_movie(movie, user_id):
    movie_id = get_movie_id(movie)
    if movie_id not in movies_and_users[user_id]['liked_movies']:
        list_of_liked = movies_and_users[user_id]['liked_movies']
        list_of_liked.append(movie_id)
        movies_and_users[user_id].update({'liked_movies': list_of_liked})
        print(f"{movie} is now in your liked movies")
        print(f"Your movies: {movies_and_users[user_id]}")
        rating = list_of_media[movie_id]['rating'] + 1
        list_of_media[movie_id].update({'rating': rating})
        print(f'{list_of_media[movie_id]}')
    else:
        print("You've already liked this movie")


def del_from_favourite(movie, user_id):
    movie_id = get_movie_id(movie)
    if movie_id in movies_and_users[user_id]['favourite']:
        list_of_favourites = movies_and_users[user_id]['favourite']
        list_of_favourites.remove(movie_id)
        movies_and_users[user_id].update({'favourite': list_of_favourites})
        print(f"Your list of movies: {movies_and_users[user_id]}")
        print(f"You've removed this movie from favourites")


def del_from_planed(movie, user_id):
    movie_id = get_movie_id(movie)
    if movie_id in movies_and_users[user_id]['planed_to_watch']:
        list_of_planed = movies_and_users[user_id]['planed_to_watch']
        list_of_planed.remove(movie_id)
        movies_and_users[user_id].update({'planed_to_watch': list_of_planed})
        print(f"{movie} removed from your planed_to_watch movies")
        print(f"Your movies: {movies_and_users[user_id]}")
    else:
        print("You have not already planed to watch this movie")


def unlike_movie(movie, user_id):
    movie_id = get_movie_id(movie)
    if movie_id in movies_and_users[user_id]['liked_movies']:
        list_of_liked = movies_and_users[user_id]['liked_movies']
        list_of_liked.remove(movie_id)
        movies_and_users[user_id].update({'liked_movies': list_of_liked})
        print(f"{movie} removed from your liked movies")
        print(f"Your movies: {movies_and_users[user_id]}")
        rating = list_of_media[movie_id]['rating'] - 1
        list_of_media[movie_id].update({'rating': rating})
        print(f'{list_of_media[movie_id]}')
    else:
        print("You haven't liked this movie yet")


def filter_year():
    year = input('what year ')
    for k_1 in list_of_media.keys():
        a = []
        mydict = list_of_media[k_1]
        if ([v for k, v in mydict.items() if k == 'year' and v == year]) != []:
            a.append((mydict['title']))
        else:
            continue
        print(a)


def main():
    name = looking_for()
    user_id = get_user_id(name)
    actions_with_movie(user_id)


if __name__ == '__main__':
    main()
