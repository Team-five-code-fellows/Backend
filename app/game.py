from scraper import get_links, get_title

base_url = "https://en.wikipedia.org"


# print rules
def print_rules():
    print("The goal of this game is to get from a starting article to an ending article using only internal wikipedia links!")
    print("To play the game, all you have to do is select the number that corresponds to the next page you want to move to.")
    print("ex. if you want to choose '7. North America', you would input '7'.\n")
    print("Would you like to (p)lay or (q)uit?")
    return input("> ")

def quit_game():
    print("Okay, thanks for stopping by!")
    print("This project was created by:")
    print("BIOS GO HERE")


def play_game():
    path = []

    # prompt for game difficulty
    print("Choose difficulty:")
    print("(e)asy (50 rounds) | (m)edium (10 rounds) | (h)ard (5 rounds)")# TODO subject to change of round amounts
    difficulty = input("> ")

    # check user input
    while difficulty != 'e' and difficulty != 'm' and difficulty != 'h':
        print("Please choose a valid difficulty setting.")
        print("(e)asy (50 rounds) | (m)edium (10 rounds) | (h)ard (5 rounds)")
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

    # check user input
    while mode != 'r' and mode != 'm':
        print("Please choose a valid mode.")
        print(
            "(r)andom (let the program choose your start and end page) | (m)anual (choose the start and end page yourself)")
        mode = input("> ")

    # get random pages
    if mode == 'r':
        start_page_title = get_title(base_url + "/wiki/Special:Random")
        start_page = base_url + "/wiki/" + start_page_title
        end_page_title = get_title(base_url + "/wiki/Special:Random")
    # get user input pages
    if mode == 'm':
        print("Input your starting article")
        start_page_query = input("> ")
        start_page = base_url + "/wiki/" + start_page_query
        start_page_title = get_title(start_page)
        print("Select your ending article")
        end_page_query = input("> ")
        end_page = base_url + "/wiki/" + end_page_query
        end_page_title = get_title(end_page)


    counter = 0
    current_page_link = start_page

    print(f"Your starting page is {start_page_title} and your goal is to reach {end_page_title}.")
    print("You can enter 'q' to quit at any time.")
    print("Good Luck!\n")
    # loop that contains turn actions
    while counter < turn_count and get_title(current_page_link) != end_page_title:
        # add current page to page path list
        # path.append(current_page)# TODO append scrubbed value of page
        # Scrape current page for all links
        link_list = get_links(current_page_link)

        current_page = get_title(current_page_link)
        path.append(current_page)

        # display remaining turns
        print(f"You have {turn_count - counter} turns left to reach the target page, {end_page_title}.")
        print(f"You are currently on {get_title(current_page_link)}")
        print("Press enter to continue")
        input("> ")


        # present page titles from links to user
        for index, item in enumerate(link_list):
            print(index+1, item)
            if index == len(link_list)-1:
                 # prompt user to input number corresponding to link or quit
                print("Input the link's corresponding number")
                choice = input("> ")
                
            elif (index % 20) == 0 and index != 0:

                print("Input the link's corresponding number or press Enter to see the next page.")
                choice = input("> ")
                if choice != "":
                    break

            
         

        # check user input
        choice_switch = False
        while choice_switch is False:
            try:
                while int(choice) < 1 or int(choice) > len(link_list):
                    print("Please input a valid index from the list")
                    choice = input("> ")
                choice_switch = True
            except ValueError:
                if choice == 'q':
                    print("Are you sure you want to quit?")
                    print("y/n")
                    choice = input("> ")
                    if choice == 'y':
                        quit_game()
                        return
                print("Please input a valid index from the list")
                choice = input("> ")

        # navigate to new page
        choice_index = int(choice) - 1
        key_list = list(link_list)
        current_page = key_list[choice_index]
        
        

        current_page_link = base_url + link_list[current_page]
        

        counter += 1

    # if current page is the target present with win screen (show path list)
    if get_title(current_page_link) == end_page_title:
        print("Congrats!")
        print(f"It took you {counter} turns to get from {start_page_title} to {end_page_title}!")
        path_text = f'The path you took was '
        for index, item in enumerate(path):
            if index == len(path) - 1:
                path_text += item
            else:
                path_text += f"{item} -> " 
        print(f"The path you took was {path_text}.") 

    if get_title(current_page_link) != end_page_title:
        print("Aw shucks! Better luck next time!")
        print("Would you like to see the path you took?")
        print("y/n")
        view_path = input("> ")
        if view_path == 'y':
            path_text = f'The path you took was '
            for index, item in enumerate(path):
                if index == len(path) - 1:
                    path_text += item
                else:
                    path_text += f"{item} -> " 
            print(path_text) 

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
    quit_game()