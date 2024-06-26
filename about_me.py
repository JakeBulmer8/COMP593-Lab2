"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {

        # TODO: Put full name into data structure
        'full_name': 'Jake Bulmer',

        # TODO: Put student ID into data structure
        'student_id': 10232733,

        # TODO: Put list of 3 pizza toppings into data structure
        'pizza_toppings': ['PEPPERONI', 'CHEESE', 'BACON'],

    
        # List of dictionaries where each dictionary contains info about a movie          
        'movies': [
            # TODO: Change this to a movie you like
            {
                'title': 'John Wick',
                'genre': 'action thriller'
            },
            # TODO: Add one more movie
            {
                'title': 'Fall Guy',
                'genre': 'action comedy'
            }
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['mushrooms', 'sausage'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'harry potter', 'fantasy')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    # Print sentence containing name
    name_sentence= f"My name is {my_info['full_name']}, but you can call me Sir {my_info['full_name'].split(" ")[0]}!" # .split reg_brackets determine the seperator in the string.
                                                                                                                       # .split square brackets pick the word in the string to use "arg 0 in this case".
    # Print sentence containing student ID
    id_sentence= f"My student ID is {my_info['student_id']}."

    print(name_sentence, end='\n')
    print(id_sentence, end='\n\n')

def new_func(my_info):
    return my_info('full_name')

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    print ('My favourite pizza toppings are:', end="\n")
    
    # Print bullet list of favourite pizza toppings
    for topping in my_info['pizza_toppings']:
        print('-', topping, end="\n")

    print(end= "\n")
        
    

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5
    # Append new pizza toppings to end of list
    tuple_toppings= tuple(toppings)
    my_info['pizza_toppings'].append(tuple_toppings[0])
    my_info['pizza_toppings'].append(tuple_toppings[1])  

    # Convert all pizza toppings to lowercase
    for letters,lower in enumerate(my_info['pizza_toppings']):
        my_info['pizza_toppings'][letters] = lower.lower()
    
    # Sort toppings list alphabetically
    my_info['pizza_toppings'].sort()

    return

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    new_movie= {
        'title': title,
        'genre': genre
    }
    my_info['movies'].append(new_movie)

    return

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres 

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 7
    for genre in my_info['movies']:
        print("I like to watch", genre['genre'], "movies.") 
    
    print(end= "\n")


def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    for title in movie_list:
        print("Some of my favourite movies are", title['title'])
    print()

if __name__ == '__main__':
    main()


# final version