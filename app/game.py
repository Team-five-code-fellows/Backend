from scraper import get_links

base_url = "https://en.wikipedia.org"


# print rules
def print_rules():
    print("The goal of this game is to get from a starting article to an ending article using only internal wikipedia links!")
    print("To play the game, all you have to do is select the number that corresponds to the next page you want to move to.")
    print("ex. if you want to choose '7. North America', you would input '7'.\n")
    print("Would you like to (p)lay or (q)uit?")
    return input("> ")


def play_game():
    start_page = '' # starting page for game
    end_page = '' # ending page for game
    path = []

    # prompt for game difficulty
    print("Choose difficulty:")
    print("(e)asy (50 rounds) | (m)edium (10 rounds) | (h)ard (5 rounds)")# TODO subject to change of round amounts
    difficulty = input("> ")

    # Set turn count according to difficulty
    if difficulty == 'e':
        turn_count = 50
    if difficulty == 'm':
        turn_count = 10
    if difficulty == 'h':
        turn_count = 5

    # prompt user for mode
    print("Choose mode:")
    print("(r)andom (let the program choose your start and end page) | (m)anual (choose the start and end page yourself)")# TODO find a better mode name than manual
    mode = input("> ")

    # get random pages
    if mode == 'r':
        start_page = base_url + "/wiki/Special:Random"
        end_page = base_url + "/wiki/Special:Random"
    # get user input pages
    if mode == 'm':
        print("Input your starting article")
        start_page_query = input("> ")
        start_page = base_url + "/wiki/" + start_page_query
        print("Select your ending article")
        end_page_query = input("> ")
        end_page = base_url + "/wiki/" + end_page_query

    counter = 0
    current_page = start_page

    # loop that contains turn actions
    while counter < turn_count and current_page != end_page:
        # add current page to page path list
        path.append(current_page)# TODO append scrubbed value of page
        # Scrape current page for all links # TODO bring in scraper method
        #link_list = scraper()
        # display remaining turns
        print(f"You have {turn_count - counter} turns left to reach the target page.")
        # present page titles from links to user TODO print return from scraper method in nice format
        # prompt user to input number corresponding to link or quit
        print("Input the link's corresponding number")
        choice = input("> ")
        # navigate to new page
        choice_index = int(choice) - 1
        #current_page = link_list[choice_index]
        counter += 1

    # if current page is the target present with win screen (show path list)
    if current_page == end_page:
        print("Congrats!")
        print(f"It took you {counter} turns to get from {start_page} to {end_page}!")
        print(f"The path you took was {path}.") #TODO format path nicely
    # if current page is not the target present with loss screen
    if current_page != end_page:
        print("Aw shucks! Better luck next time!")
        print("Would you like to see the path you took?")
        print("y/n")
        view_path = input("> ")
        if view_path == 'y':
            print(f"The path you took was {path}.")  # TODO format path nicely

    # ask if the user would like to play again or quit
    print("Would you like to (p)lay again or (q)uit?")
    return input("> ")

# print welcome message
print("Welcome to 5 Degrees of Wiki!")
print("Would you like to (p)lay, (q)uit, or see (r)ules?")
start_choice = input("> ")

# print rules
if start_choice == 'r':
    start_choice = print_rules()
# play game
if start_choice == 'p':
    while start_choice == 'p':
        start_choice = play_game()
# quit program, print creator info
if start_choice == 'q':
    print("Okay, thanks for stopping by!")
    print("This project was created by:")
    print("BIOS GO HERE")
