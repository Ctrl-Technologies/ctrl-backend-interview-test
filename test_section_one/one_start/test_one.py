import random


def combine_two_lists_parallel():
    result_list = []
    first_list = [1, 2, 3, 4, 5, 6]
    second_list = ['A', 'B', 'C', 'D', 'E', 'F']

    """
    A PEP20 way of iterating efficiently through 2 lists.
    
    Hint python has a built in method for this that takes two lists.
    
    Result should be a list of tuples: EX: [(C,3),...]
    """

    return result_list


def return_matches_in_list_parallel():
    result_list = []
    first_input_string = """Two of the fairest stars in all the heaven,
    Having some business, do entreat her eyes
    To twinkle in their spheres till they return.
    What if her eyes were there, they in her head?
    The brightness of her cheek would shame those stars,
    As daylight doth a lamp; her eyes in heaven
    Would through the airy region stream so bright
    That birds would sing and think it were not night.
    See, how she leans her cheek upon her hand!
    O, that I were a glove upon that hand,
    That I might touch that cheek
    """.replace(";", "").replace(",", "").replace(".", "").replace("?", "").replace("\n", "").strip().lower()
    second_input_string = """Sleep dwell upon thine eyes, peace in thy breast!
    Would I were sleep and peace, so sweet to rest!
    Hence will I to my ghostly father's cell,
    His help to crave, and my dear hap to tell.
    """.replace(";", "").replace(",", "").replace(".", "").replace("?", "").replace("\n", "").strip().lower()

    first_input_string = first_input_string.split()
    second_input_string = second_input_string.split()
    first_list = sorted(first_input_string, key=lambda k: random.random())
    second_list = sorted(second_input_string, key=lambda k: random.random())

    # in case its not random enough
    if first_list[0] == second_list[0]:
        second_list = sorted(second_list, key=lambda k: random.random())

    """
    Return matches found in both lists, as pythonic as possible
    
    """

    return set(result_list)


def count_shakespeare():
    with open("one_start/shakespeare.txt") as file:
        shakespeare_text = file.read()

        """
        The challenge here is to count the occurances of words occuring more than once.
        
        Also indicate the total word count of the piece of text as well as the longest word in the text.
        
        return {
            occurances: object,
            total: int,
            longest_word: int
        }
        
        """


def infinite_loop():
    """
    List will keep on running, break the list on iteration 784 and return the list of results.

    :return:
    """
    result_list = []
    i = 0
    while i < 1000:
        """
        Add potential code
        """
        print(i)

        i += 1

    return result_list

