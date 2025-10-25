anime_lists = [ ]

while True:
    anime_title = input("Enter the title of an anime(type 'exit' to finish): " )
    
    if anime_title == "exit": 
        print("Existing the program")
        break
        
    else:
         anime_lists.append(anime_title)
         print("{anime_title}" "has been added to your lists")
        
print("Your anime lists: ")
for anime in anime_lists:
       print(f"• {anime}")       
       