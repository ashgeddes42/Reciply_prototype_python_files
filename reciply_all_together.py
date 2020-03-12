import json

#Login Subprogram
def login():
    correct = False
    
    #Until a correct (corresponding) username and password are entered
    while correct != True:
        
        #Getting username and password information from the user
        entered_username = input('Username: ')
        #take away extra white space at the end of the word
        entered_username = entered_username.strip()
        entered_password = input('Password: ')
        #take away extra white space at the end of the word
        entered_password = entered_password.strip()
        data = (f'{entered_username}:{entered_password}')

        #Checking validity of login data
        file = open('users_passwords.txt')
        for line in file:
            line = line.strip()
            if line == data:
                correct = True
        if correct == False:
            print('Incorrect username or password please try again')
            print()
    print()

#Create Account Subprogram
def create_account():
    print('Please enter in your details below...')
    print()
    taken = True
    
    #Until the user enters a unique username
    while taken != False:
        #Getting the new username from the user
        entered_username = input('Username: ')
        #take away extra white space at the end of the word
        entered_username = entered_username.strip()
        
        #Checking the new username is unique
        f = open("usernames.txt")
        taken = False
        for line in f:
            line = line.strip()
            #take away extra white space at the end of the line
            if line == entered_username:
                taken = True
        if taken == True:
            print(f'{entered_username} is already in use. Please choose a unique username.')
            print()
    
    #Getting the new password from the user  
    entered_password = input('Password: ')
    entered_password = entered_password.strip()
    new_file_entry = (f'{entered_username}:{entered_password}')
    
    #Saving new user information to external files
    f = open("users_passwords.txt","a")
    f.write('\n' + new_file_entry)
    f.close()
    f = open("usernames.txt", "a")
    f.write('\n' + entered_username)
    f.close()
    
    #Introductions
    print()
    print(f'Welcome to Reciply {entered_username}!')
    print()
    print('Please login using your new username and password...')
    print()

#Upload Recipe Subprogram
def upload_recipe():
    #Get recipe information from user
    title = input('Recipe Title: ')
    title = title.lower()
    ingredients = input('Ingredients (in, in, in,): ')
    description = input('Description: ')
    ingredients = ingredients.split(',')
    steps = input('Method (step, step, step): ')
    method = steps.split(', ')
    #Convert the recipe information into json to save to an external file
    method = json.dumps(method)
    ingredients = json.dumps(ingredients)
    recipe_card = '{' + f'"Title":"{title}", "Description":"{description}", "Ingredients":{ingredients}, "Method":{method}' + '}'
    #Saving recipe information to an external file
    f = open("Public_Recipes.txt","a")
    f.write('\n' + recipe_card)
    f.close()
    print(f'Your recipe has been published!')
    print()

#Search User Subprogram
def search_users():
    #User enters search terms
    query = input('Search: ')
    query = query.lower()
    print()
    search_terms = query.split()
    results_level_1 = []
    results_level_2 = []
    found = []

    #Finding recipes in database and determining relevance
    f = open('usernames.txt')
    for user in f:
        name = user.strip()
        #Highest relevance: when the entered query matches a username exactly
        if name == query:
            results_level_1.append(name)
            found.append(name)
        #Second relevance: when the entered query is in a username
        elif query in name and name not in found:
            results_level_2.append(name)
            found.append(name)

    #Create a list of all results (keeping order of relevancy)
    results = results_level_1 + results_level_2
    #Determine number of results
    num_search_results = len(results)
    #Display results to user
    print(f'{num_search_results} result(s): ')
    print()
    #Display a corresponding number with each result so that users can choose a result
    count = 0
    for i in results:
        count += 1
        print(f' {count}. {i}')
    print()
    friend_request_number = input('Enter result number to send a friend request: ')
    print()
    print('Request sent')
    print()

#Search Recipes Subprogram
def search_recipes():
    #User enters search terms
    query = input('Search: ')
    query = query.lower()
    print()
    search_terms = query.split()
    results_level_1 = []
    results_level_2 = []
    results_level_3 = []
    results_level_4 = []
    found = []
    
    #Finding recipes in database and determining relevance
    f = open('public_recipes.txt')
    #Checking for title in each recipe in Public_Recipes.txt
    for line in f:
        line = line.strip()
        line_dict = json.loads(line)
        title = line_dict['Title']
        description = line_dict['Description']
        found_card = (f'{title} : {description}')
        if title == query:
            results_level_1.append(found_card)
            found.append(found_card)
        elif query in title and found_card not in found:
            results_level_2.append(found_card)
            found.append(found_card)
        for term in search_terms:
            if title == term and found_card not in found:
                results_level_3.append(found_card)
                found.append(found_card)
            if term in title and found_card not in found:
                results_level_4.append(found_card)
                found.append(found_card)
    f.close()
    
    #Display search results in order of relevancy
    results = results_level_1 + results_level_2 + results_level_3 + results_level_4
    num_search_results = len(results)
    print(f'{num_search_results} result(s): ')
    print()
    count = 0
    if results:
        for i in results:
            count += 1 
            print(f'{count}. {i}')
            print()
        print('Please enter the number of the result you would like to open...')
        chosen_number = int(input('Number: '))
        while chosen_number > (len(results)) or chosen_number <1:
            print('Please choose a number from the results listed above (eg. "1")')
            chosen_number = int(input('Number: '))
        chosen_result = results[int((chosen_number)-1)]
        chosen_result_parts = chosen_result.split(':')
        result_title = chosen_result_parts[0]
        #Remove white space from the title
        result_title = result_title.strip()
        print()
        #Find the rest of the data for the recipe the user wants to see
        f = open('public_recipes.txt')
        for line in f:
            line = line.strip()
            line_dict = json.loads(line)
            title = line_dict['Title']
            description = line_dict['Description']
            ingredients = line_dict['Ingredients']
            method = line_dict['Method']
            if title == result_title:
                print()
                print(f'*****{title.upper()}*****')
                print()
                print(f'Description: {description}')
                print()
                print("Ingredients: ")
                for i in ingredients:
                    print(f' - {i}')
                num = 0
                print()
                print('Method:')
                for i in method:
                    num += 1
                    print(f'Step {num}. {i}')
                print()
                print('*****' + len(title) * '*' + '*****')
                print()
    else:
        print('We found no related recipes in our data base. Please check your spelling and try again.')
   
#Help subprogram
def help_information():
    print('Helping you sooner or later.')
    print()

#Main Program
answer = input("Already a member? ('yes'/'no'): ")
print()

#Error handling
while answer != 'yes' and answer != 'no':
    answer = input("Please answer either 'yes' or 'no': ")
#New member or logging in
if answer == 'yes':
    login()
elif answer == 'no':
    create_account()
    login()

#Choosing a page (what to do)
print('Pages: upload a recipe, search recipes, search users, get help')
print("To exit the application, type 'EXIT'")
print("Please choose a page...")
print()
page_choice = input('Page choice: ')
print()

#Until the user wants to exit the application
while page_choice != 'EXIT':
    if page_choice == 'upload a recipe':
        upload_recipe()
    elif page_choice == 'search users':
        search_users()
    elif page_choice == 'search recipes':
        search_recipes()
    elif page_choice == 'get help':
        help_information()
    #Error handling
    else:
        print('Please choose one of the pages listed above. Check your spelling and try again.')
        print()
    #When each subprogram is finished, ask user to choose another page or to exit the application
    print("Choices: 'upload a recipe', 'search recipes', 'search users', 'get help'")
    print("To exit the application, type 'EXIT'")
    print('Please choose a page...')
    page_choice = input('Page Choice: ')
    print()
    
print()
print('Until next time...')