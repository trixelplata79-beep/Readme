import openpyxl as trix

wbk = trix.Workbook()

sheet = wbk.active
sheet.title = "Favorite People"

def main():

    people = []
    current_year = 2026
    header = ["ID", "First Name", "Last Name", "Birth Year", "Age"]
    sheet.append(header)

    for person in range(1, 4):

        print(f"\nPerson {person}")

        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        birth = int(input("Enter birth year: "))

        age = current_year - birth

        people.append([person, fname, lname, birth, age])

    for data in people:
        sheet.append(data)

    wbk.save("favorite_people.xlsx")

    print("\nFavorite people saved successfully!")

    print("\n===== FAVORITE PEOPLE LIST =====")

    print(tuple(header))

    for data in people:
        print(tuple(data))

main()