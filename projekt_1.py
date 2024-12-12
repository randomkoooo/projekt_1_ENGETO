"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Pavel Bartoš
email: pavel.bartos97@email.cz
"""
user_name = input("Your username: ")
user_password = input("Your password: ")

users = {"bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123"
        }

if users.get(user_name) == user_password:
    print("*" * 40)
    print(f"Welcome to the app {user_name.upper()}.")
    print("We have 3 texts to be analyzed.")
    print("*" * 40)

    texts_number = input("Enter a number btw. 1 and 3 to select: ")
    print("*" * 40)

    if texts_number.isdigit() and 1 <= int(texts_number) <= 3:
        
        TEXTS = ['''
        Situated about 10 miles west of Kemmerer,
        Fossil Butte is a ruggedly impressive
        topographic feature that rises sharply
        some 1000 feet above Twin Creek Valley
        to an elevation of more than 7500 feet
        above sea level. The butte is located just
        north of US 30N and the Union Pacific Railroad,
        which traverse the valley.''',
        '''At the base of Fossil Butte are the bright
        red, purple, yellow and gray beds of the Wasatch
        Formation. Eroded portions of these horizontal
        beds slope gradually upward from the valley floor
        and steepen abruptly. Overlying them and extending
        to the top of the butte are the much steeper
        buff-to-white beds of the Green River Formation,
        which are about 300 feet thick.''',
        '''The monument contains 8198 acres and protects
        a portion of the largest deposit of freshwater fish
        fossils in the world. The richest fossil fish deposits
        are found in multiple limestone layers, which lie some
        100 feet below the top of the butte. The fossils
        represent several varieties of perch, as well as
        other freshwater genera and herring similar to those
        in modern oceans. Other fish such as paddlefish,
        garpike and stingray are also present.'''
        ]

        texts_str = TEXTS[int(texts_number) - 1]

        texts_words = texts_str.split()
        texts_words_number = len(texts_words)

        texts_titwords = [titword for titword in texts_words if titword[0].istitle()]
        texts_titwords_number = len(texts_titwords)

        texts_upwords = [upwords for upwords in texts_words if upwords.isupper() and upwords.isalpha()]
        texts_upwords_number = len(texts_upwords)

        texts_lowords = [lowords for lowords in texts_words if lowords.islower()]
        texts_lowords_number = len(texts_lowords)

        texts_num = [num for num in texts_words if num.isnumeric()]
        texts_num_number = len(texts_num)

        texts_sumnum = 0
        for sumnum in texts_words:
            if sumnum.isnumeric():
                texts_sumnum += int(sumnum)
        
        graph_words = [texts_str.strip(".,") for texts_str in texts_words]
        graph_words_length = [len(texts_str) for texts_str in graph_words]

        length_counts = {}
        for length in graph_words_length:
            if length in length_counts:
                length_counts[length] += 1
            else:
                length_counts[length] = 1

        print(f"There are {texts_words_number} words in the selected text.",
              f"There are {texts_titwords_number} titlecase words.",
              f"There are {texts_upwords_number} uppercase words",
              f"There are {texts_lowords_number} lower case words.",
              f"There are {texts_num_number} numeric strings.",
              f"The sum of all the number {texts_sumnum}.",
              sep="\n"
              )
        print("*" * 40)
        print(f"{"LENGHT":<10}{"OCCURENCES":<20}{"NUMBER"}")
        print("*" * 40)
        for length, count in sorted(length_counts.items()):
            print(f"{length:<10}{'*' * count:<20}{count}")
    else:
        if not texts_number.isdigit():
            print("You have to enter only numbers, closing the program.")
        else:
            print("You have entered the wrong number, closing the program.")
else:
    print("Unregistered user, closing the program.")