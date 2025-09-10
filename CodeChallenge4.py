print("Welcome to the Manga Reader Recommender\nAnswer a few questions to find your next read.")
genre = input("What genre do you like?(Action, Romance, Horror): ")
duration = input("How long should the manga be?(Short, Medium, Long): ")

decade = input("which decade?(2000's or 2010's): ")

short_2010s = "Jujutsu Kaisen"
short_2000s = "Hunter X Hunter"
medium_2010s = "One piece"
medium_2000s = "one-punch Man"
long_2000s = "Lupin"
long_2010s = "Naruto"

if genre.lower() == "action":
    if duration.lower() == "short":
        if decade.lower() == "2010s":
            print(f"We recommend: {short_2010s}")
        elif decade.lower() == "2000s":
            print(f"We recommend: {short_2000s}")
        else:
            pass
    elif duration.lower() == "medium":
        if decade.lower() == "2010s":
            print(f"We recommend: {medium_2010s}")
        elif decade.lower() == "2000s":
            print(f"We recommend: {medium_2000s}")
        else:
            pass
    elif duration.lower() == "long":
        if decade.lower() == "2000s":
            print(f"We recommend: {long_2000s}")
        elif decade.lower() == "2010s":
            print(f"We recommend: {long_2010s}")
        else:
            pass
    else:
        pass