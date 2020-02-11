from Pet import Pet
from WildAnimal import WildAnimal
from Treatment import Treatment
import csv

pet_list = []
wanimal_list = []
treatment_list = []
list_of_abusers = []
abandoned_list = []

file_pet = "DADSA 2019-20 CWK A DATA PETS.csv"
file_wanimal = "DADSA 2019-20 CWK A WILD ANIMALS.csv"
file_treatment = "DADSA 2019-20 CWK A TREATMENT.csv"


# load pet data from csv and populates class Pet
def load_pet_data():
    with open(file_pet, 'r', newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        # Skips first row
        first = True
        for row in reader:
            if first:
                first = False
            else:
                pet_list.append(Pet(row[0], row[1], row[2], row[3], row[4], row[5],
                                    row[6], row[7], row[8], row[9], row[10]))


# load wild animal data from csv and populates class WildAnimal
def load_wanimal_data():
    with open(file_wanimal, 'r', newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        # Skips first row
        first = True
        for row in reader:
            if first:
                first = False
            else:
                wanimal_list.append(WildAnimal(row[0], row[1], row[2], row[3], row[4], row[5],
                                               row[6], row[7]))


# load treatment data from csv and populates class Treatment
def load_treatment_data():
    with open(file_treatment, 'r', newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        # Skips first row
        first = True
        for row in reader:
            if first:
                first = False
            else:
                treatment_list.append(Treatment(row[0], row[1], row[2], row[3], row[4], row[5],
                                                row[6], row[7]))


# Prints objects in list for testing
def print_data(list_name):
    for row in list_name:
        print(row)


# Loads data from all csv files
def load_data():
    load_pet_data()
    load_treatment_data()
    load_wanimal_data()


# Task 2A
# Create a new entry for Pet in the Pet Data csv file
def new_entry_pet():
    print("Enter the following details;")
    # Sanctuary ID
    sanctuary_id = input("Sanctuary ID: ").title()
    # Animal Type
    animal_type = input("Animal Type: ").title()
    # Breed
    breed = input("Breed: ").title()
    # Vaccinated
    while True:
        vaccinated = input("Vaccinated, enter 'Yes' or press return for 'No': ").title()
        # Checks for valid input
        if vaccinated == 'Yes' or vaccinated == "":
            break
        else:
            print("\nInvalid Input Please Enter Again\n")
    # Neutered
    while True:
        neutered = input("Neutered enter 'Yes' or press return for 'No': ").title()
        # Checks for valid input
        if neutered == 'Yes' or neutered == "":
            break
        else:
            print("\nInvalid Input Please Enter Again\n")
    # Microchip Number
    microchip_num = input("Microchip number: ").title()
    # Admission Reason
    admission_reason = input("Reason for admission; Abused, Abandoned Car Accident, Lost, Stray:  ").title()
    # Arrival Date
    arrival_date = input("Arrival date (dd/mm/yyyy) : ")
    # Departure Date
    departure_date = input("Departure date (dd/mm/yyyy) : ")
    # Destination
    destination = input("Destination: ").title()
    # Destination Address
    destination_address = input("Destination Address: ").title()
    # Append inputs to a new row in csv file
    with open(file_pet, 'a', newline="") as csvfile:
        pet_list_writer = csv.writer(csvfile)
        pet_list_writer.writerow([sanctuary_id, animal_type, breed, vaccinated, neutered, microchip_num,
                                  admission_reason, arrival_date, departure_date, destination, destination_address])
        # Inputs assigned as attributes to create new object in Pet Class
        pet_list.append(Pet(sanctuary_id, animal_type, breed, vaccinated, neutered, microchip_num,
                            admission_reason, arrival_date, departure_date, destination, destination_address))

    # Shows the user the new entry
    print("\n|New Pet Information Added|")
    print(Pet(sanctuary_id, animal_type, breed, vaccinated, neutered, microchip_num,
              admission_reason, arrival_date, departure_date, destination, destination_address))
    print("\n")


# Task 2A
# New Entry for Wild Animal
def new_entry_wanimal():
    print("Enter the following details;")

    # Sanctuary ID
    sanctuary_id = input("Sanctuary ID: ").title()
    # Animal Type
    animal_type = input("Animal Type: ").title()
    # Vaccinated
    while True:
        vaccinated = input("Vaccinated, enter 'Yes' or press return for 'No': ").title()
        # Checks for valid input
        if vaccinated == 'Yes' or vaccinated == "":
            break
        else:
            print("\nInvalid Input Please Enter Again\n")
    # Admission Reason
    admission_reason = input("Reason for admission; Abused, Abandoned Car Accident, Lost, Stray:  ").title()
    # Arrival Date
    arrival_date = input("Arrival date (dd/mm/yyyy) : ")
    # Departure Date
    departure_date = input("Departure date (dd/mm/yyyy) : ")
    # Destination
    destination = input("Destination: ").title()
    # Destination Address
    destination_address = input("Destination Address: ").title()
    # Append inputs to a new row in csv file
    with open(file_wanimal, 'a', newline="") as csvfile:
        animal_writer = csv.writer(csvfile)
        animal_writer.writerow([sanctuary_id, animal_type, vaccinated, admission_reason,
                                arrival_date, departure_date, destination, destination_address])
        # Inputs assigned as attributes to create new object in WildAnimal class
        wanimal_list.append(WildAnimal(sanctuary_id, animal_type, vaccinated, admission_reason,
                            arrival_date, departure_date, destination, destination_address))

    # Shows the user the new entry
    print("\n|New Wild Animal Information Added|")
    print(WildAnimal(sanctuary_id, animal_type, vaccinated, admission_reason,
                     arrival_date, departure_date, destination, destination_address))
    print("\n")


# Task 2A
# New Entry for Treatment
def new_entry_treatment():
    print("Enter the following details;")
    # Sanctuary ID
    sanctuary_id = input("Sanctuary ID:").title()
    # Surgery
    surgery = input("Surgery: ").title()
    # Surgery Date
    while True:
        surgery_date = input("Date of Surgery:")
        if surgery_date != "":
            break
        else:
            print("Surgery must have a date:")
    # Medication
    medication = input("Medication: ").title()
    # Medication Start
    med_start = input("Medication Start Date:")
    # Medication End
    med_finish = input("Medication End Date:")
    # Responsible for Abuse
    abused_by = input("Responsible for Abuse:").title()
    # Responsible for Abandoning
    abandoned_by = input("Responsible for Abandoning:").title()

    # Append inputs to a new row in csv file
    with open(file_treatment, 'a', newline="") as csvfile:
        treatment_writer = csv.writer(csvfile)
        treatment_writer.writerow([sanctuary_id, surgery, surgery_date, medication,
                                   med_start, med_finish, abused_by, abandoned_by])
        # Inputs assigned as attributes to create new object in Treatment Class
        treatment_list.append(Treatment(sanctuary_id, surgery, surgery_date, medication,
                              med_start, med_finish, abused_by, abandoned_by))

    # Shows the user the new entry
    print("\n|New Treatment Information Added|")
    print(Treatment(sanctuary_id, surgery, surgery_date, medication,
                    med_start, med_finish, abused_by, abandoned_by))
    print("\n")


# Task 2B
# Returns animal data based on Sanctuary ID
def return_animal_data(id_num):
    found = False
    # Return the pet info if ID found in pet list
    for pet in pet_list:
        if pet.sanctuary_id == id_num:
            found = True
            # Output the pet information
            print("\n|PET INFORMATION|")
            print(pet)

    # If ID not in pet list, search wild animal list and return info
    if not found:
        for wild_animal in wanimal_list:
            if wild_animal.sanctuary_id == id_num:
                # Output wild animal information
                print(wild_animal)

        # Search treatment for corresponding ID
    print("\n|TREATMENT INFORMATION|")
    for treatment in treatment_list:
        if treatment.sanctuary_id == id_num:
            print(treatment)


# Task 2C
# Produces list of people who have abused animals
def abused():
    for treatment in treatment_list:
        if treatment.abused_by != '':
            list_of_abusers.append(treatment.abused_by)
    # Make names unique
    distinct_list = duplicate(list_of_abusers)
    # Sort A to Z
    insertion_sort(distinct_list)
    print("\n|PEOPLE WHO HAVE ABUSED ANIMALS IN THE PAST|")
    for name in distinct_list:
        print(name)
    print("\n")


# Task 2D
# Produces list of people who have abandoned animals
def abandoned():
    for treatment in treatment_list:
        if treatment.abandoned_by != '':
            abandoned_list.append(treatment.abandoned_by)
    # Make names unique
    distinct_list = duplicate(abandoned_list)
    # Sort A to Z
    insertion_sort(distinct_list)
    print("\n|PEOPLE WHO HAVE ABANDONED ANIMALS|")
    for name in distinct_list:
        print(name)
    print("\n")


# Task 2E/2F
# Produce Cats or Dogs ready for adoption
# Cat or Dog as parameter
def adoption(pet_type):
    print("\n|" + pet_type.title() + "s, Ready To Adopt|")
    for pet in pet_list:
        if pet_type.title() == pet.animal_type:
            # Must have microchip and vaccinated and neutered
            if pet.microchip_num != '' and pet.vaccinated == 'Yes' and pet.neutered == 'Yes' \
             and pet.admission_reason != 'Lost' and pet.admission_reason != 'Car Accident' and pet.destination == '':
                print(pet)
    print("\n")


# Task 2G
# Print list of pets ready to be returned to owners
def return_to_owner_pet():
    print("\n|Pets To Be Returned|")
    temp = []
    for pet in pet_list:
        if pet.microchip_num != "" and (pet.admission_reason == "Lost" or pet.admission_reason == "Car Accident") \
                and pet.departure_date == '' and pet.destination == '':
            temp.append(pet)
    insertion_sort(temp)
    for pet in temp:
        print(pet)


# Task 2G
# Print list of wild animals that need new zoo
def return_to_owner_wanimal():
    print("\n|Animals To Be Returned|")
    temp = []
    for animal in wanimal_list:
        if "Abandoned" in animal.admission_reason and animal.departure_date == "":
            temp.append(animal)
    insertion_sort(temp)
    for animal in temp:
        print(animal)


# Sorts items of list in ascending order using Insertion
def insertion_sort(list_name):
    for index in range(1, len(list_name)):
        temp = list_name[index]
        i = index - 1
        while i >= 0:
            if temp < list_name[i]:
                list_name[i + 1] = list_name[i]
                list_name[i] = temp
                i = i - 1
            else:
                break


# Removes duplicate items from a list
def duplicate(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique


# Returns Pet object hat matches ID
def return_pet(pet_id):
    found = False
    # Return the pet info if ID found in pet list
    for pet in pet_list:
        if pet.sanctuary_id == pet_id:
            found = True
            return pet
    if not found:
        return "not found"


# Updates Pet csv file
def update_pet(pet):
    r = csv.reader(open(file_pet))
    lines = list(r)
    for row in lines:
        if row[0] == pet.sanctuary_id:
            row[1] = pet.animal_type
            row[2] = pet.breed
            row[3] = pet.vaccinated
            row[4] = pet.neutered
            row[5] = pet.microchip_num
            row[6] = pet.admission_reason
            row[7] = pet.arrival_date
            row[8] = pet.departure_date
            row[9] = pet.destination
            row[10] = pet.destination_address
    writer = csv.writer(open(file_pet, 'w', newline=''))
    writer.writerows(lines)
    print(pet)


# Returns Wild Animal object that matches ID
def return_wanimal(animal_id):
    found = False
    # Return the wild animal info if ID found in wild animal list
    for animal in wanimal_list:
        if animal.sanctuary_id == animal_id:
            found = True
            return animal
    if not found:
        return "not found"


# Updates Wild Animal csv file
def update_wanimal(animal):
    r = csv.reader(open(file_wanimal))
    lines = list(r)
    for row in lines:
        if row[0] == animal.sanctuary_id:
            row[1] = animal.animal_type
            row[2] = animal.vaccinated
            row[3] = animal.admission_reason
            row[4] = animal.arrival_date
            row[5] = animal.departure_date
            row[6] = animal.destination
            row[7] = animal.destination_address
    writer = csv.writer(open(file_wanimal, 'w', newline=''))
    writer.writerows(lines)
    print(animal)


def return_treatment(treatment_id):
    pet_treatments = []
    for treatment in treatment_list:
        # Return the treatment info if ID found in treatment list and stores in new list
        if treatment.sanctuary_id == treatment_id:
            pet_treatments.append(treatment)
    if len(pet_treatments) > 1:
        print("Select Treatment:")
        # Outputs all treatment objects with same ID
        for i in range(1, len(pet_treatments) + 1):
            print(i, pet_treatments[i-1])
        s = int(input("Please choose:"))
        s = s - 1
        print("\n|Treatment Information|")
        return pet_treatments[s]
    else:
        print("\n|Treatment Information|")
        return treatment


# Updates treatment csv file
def update_treatment(treatment):
    r = csv.reader(open(file_treatment))
    lines = list(r)
    for row in lines:
        if row[0] == treatment.sanctuary_id and row[2] == treatment.surgery_date:
            row[1] = treatment.surgery
            row[2] = treatment.surgery_date
            row[3] = treatment.medication
            row[4] = treatment.med_start
            row[5] = treatment.med_finish
            row[6] = treatment.abused_by
            row[7] = treatment.abandoned_by
    writer = csv.writer(open(file_treatment, 'w', newline=''))
    writer.writerows(lines)
    print(treatment)


# Input new entry menu
def new_entry_sub_menu():
    print("Pet, Wild Animal or Treatment Data: \n")
    print("1. Pet Data")
    print("2. Wild Animal Data")
    print("3. Treatment Data")
    print("0. Back to Menu")

    while True:
        s = int(input("Enter Selection:"))
        # New Pet entry
        if s == 1:
            new_entry_pet()
            menu()
            break
        # New Wild Animal entry
        elif s == 2:
            new_entry_wanimal()
            menu()
            break
        # New Treatment entry
        elif s == 3:
            new_entry_treatment()
            menu()
            break
        # Back to menu
        elif s == 0:
            menu()
            break
        else:
            print("Invalid Input, Please Select Again")


# Update Pet menu
def update_pet_sub_menu():
    pet_id = input("Enter ID of Pet you wish to edit:").upper()
    # if ID not found, print ID does not exist and ask to enter again
    pet = return_pet(pet_id)
    if pet == "not found":
        print("\nPet ID not found, please enter again:")
        update_pet_sub_menu()
    else:
        print(pet)
        while True:
            try:
                print("What attribute would you like to change:")
                print("2. Animal Type:")
                print("3. Breed:")
                print("4. Vaccinated:")
                print("5. Neutered:")
                print("6. Microchip Number:")
                print("7. Reason for admission:")
                print("8. Date of Arrival:")
                print("9: Date of Departure:")
                print("10. Destination:")
                print("11. Destination Address:")
                print("0. Back to Menu:")
                s = int(input("Enter Selection:"))
                #  Update Animal Type
                if s == 2:
                    animal_type = input("Enter animal type:").title()
                    # update_selection(pet, animal_type)
                    pet.animal_type = animal_type
                    update_pet(pet)
                #  Update Breed
                elif s == 3:
                    breed = input("Enter breed:").title()
                    pet.breed = breed
                    update_pet(pet)
                # Update Vaccinated
                elif s == 4:
                    while True:
                        vaccinated = input("Enter Vaccinated, 'Yes' or blank for No:").title()
                        # Checks for valid input
                        if vaccinated == 'Yes' or vaccinated == '':
                            pet.vaccinated = vaccinated
                            update_pet(pet)
                            break
                    else:
                        print("Invalid Input Please Enter Again:")
                # Update Neutered
                elif s == 5:
                    while True:
                        neutered = input("Enter Neutered, 'Yes' or blank for No:").title()
                        # Checks for valid input
                        if neutered == 'Yes' or '':
                            pet.vaccinated = neutered
                            update_pet(pet)
                            break
                    else:
                        print("Invalid Input Please Enter Again:")
                # Update Microchip Number
                elif s == 6:
                    microchip_num = input("Enter Microchip Number:").upper()
                    pet.microchip_num = microchip_num
                    update_pet(pet)
                # Update Reason for Admission
                elif s == 7:
                    admission_reason = input("Enter Reason for Admission:").title()
                    pet.admission_reason = admission_reason
                    update_pet(pet)
                # Update Date of Arrival
                elif s == 8:
                    arrival_date = input("Enter Date of Arrival:")
                    pet.arrival_date = arrival_date
                    update_pet(pet)
                # Update Date of Departure
                elif s == 9:
                    departure_date = input("Enter Date of Departure:")
                    pet.departure_date = departure_date
                    update_pet(pet)
                # Update Destination
                elif s == 10:
                    destination = input("Enter Destination:").title()
                    pet.destination = destination
                    update_pet(pet)
                # Update Destination Address
                elif s == 11:
                    destination_address = input("Enter Destination Address:").title()
                    pet.destination_address = destination_address
                    update_pet(pet)
                elif s == 0:
                    menu()
                    break
                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid Input")
        exit


# Update Wild Animal menu
def update_wanimal_sub_menu():
    animal_id = input("Enter ID of Wild Animal you wish to edit:").upper()
    # if ID not found, print ID does not exist and ask to enter again
    animal = return_wanimal(animal_id)
    if animal == "not found":
        print("\nAnimal ID does not exist, please enter again: ")
        update_wanimal_sub_menu()
    else:
        print("\n")
        print(animal)
        while True:
            try:
                print("What attribute would you like to change:")
                print("2. Animal Type:")
                print("3. Vaccinated:")
                print("4. Reason for admission:")
                print("5. Date of Arrival:")
                print("6: Date of Departure:")
                print("7. Destination:")
                print("8. Destination Address:")
                print("0. Back to Menu:")
                s = int(input("Enter Selection:"))
                # Update Animal Type
                if s == 2:
                    animal_type = input("Enter animal type:").title()
                    animal.animal_type = animal_type
                    update_wanimal(animal)
                # Update Vaccinated
                elif s == 3:
                    while True:
                        vaccinated = input("Enter Vaccinated, 'Yes' or blank for No:").title()
                        # Checks for valid input
                        if vaccinated == 'Yes' or vaccinated == '':
                            animal.vaccinated = vaccinated
                            update_wanimal(animal)
                            break
                    else:
                        print("Invalid Input Please Enter Again:")
                # Update Admission Reason
                elif s == 4:
                    admission_reason = input("Enter Reason for Admission:").title()
                    animal.admission_reason = admission_reason
                    update_wanimal(animal)
                # Update Arrival Date
                elif s == 5:
                    arrival_date = input("Enter Date of Arrival:")
                    animal.arrival_date = arrival_date
                    update_wanimal(animal)
                # Update Departure Date
                elif s == 6:
                    departure_date = input("Enter Date of Departure:")
                    animal.departure_date = departure_date
                    update_wanimal(animal)
                # Update Destination
                elif s == 7:
                    destination = input("Enter Destination:").title()
                    animal.destination = destination
                    update_wanimal(animal)
                # Update Destination Address
                elif s == 8:
                    destination_address = input("Enter Destination Address:").title()
                    animal.destination_address = destination_address
                    update_wanimal(animal)
                elif s == 0:
                    menu()
                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid Input")
        exit


# Update Treatment menu
def update_treatment_sub_menu():
    sanctuary_id = input("Enter ID of Animal you wish to edit:").upper()
    # if ID not found, print ID does not exist and ask to enter again
    treatment = return_treatment(sanctuary_id)
    if treatment == "not found":
        print("\nAnimal ID does not exist, please enter again:")
        update_treatment_sub_menu()
    else:
        print(treatment)
        print("\n")
        while True:
            try:
                print("What attribute would you like to change:")
                print("1. Surgery:")
                print("2. Medication:")
                print("3. Date Medication Started:")
                print("4: Date Medication Ends:")
                print("5. Person Responsible for Abuse:")
                print("6. Person Responsible for Abandoning")
                print("0. Back to Menu:")
                s = int(input("Enter Selection:"))
                # Update Surgery
                if s == 1:
                    surgery = input("Enter Surgery:").title()
                    treatment.surgery = surgery
                    update_treatment(treatment)
                # Update Medication
                elif s == 2:
                    medication = input("Enter Name of Medication:").title()
                    treatment.medication = medication
                    update_treatment(treatment)
                # Update Medication Start Date
                elif s == 3:
                    med_start = input("Enter Medication Start Date: (dd/mm/yyyy)")
                    treatment.med_start = med_start
                    update_treatment(treatment)
                # Update Medication Finish Date
                elif s == 4:
                    med_finish = input("Enter Medication End Date: (dd/mm/yyyy)")
                    treatment.med_finish = med_finish
                    update_treatment(treatment)
                # Update Person Responsible for Abuse
                elif s == 5:
                    abused_by = input("Enter Name of Person Responsible for Abuse:").title()
                    treatment.abused_by = abused_by
                    update_treatment(treatment)
                # Update Person Resposible for Abandoning
                elif s == 6:
                    abandoned_by = input("Enter Name of Person Responsible for Abandoning:").title()
                    treatment.abandoned_by = abandoned_by
                    update_treatment(treatment)
                elif s == 0:
                    menu()
                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid Input")
        exit


# Sub Menu to access: update existing entry sub menus
def update_entry_sub_menu():
    while True:
        print("1. Update Pet")
        print("2. Update Wild Animal")
        print("3. Update Treatment")
        print("0. Back to Menu")
        s = int(input("Enter Selection: "))
        # Update Pet
        if s == 1:
            update_pet_sub_menu()
        # Update Wild Animal
        elif s == 2:
            update_wanimal_sub_menu()
        # Update Treatment
        elif s == 3:
            update_treatment_sub_menu()
        elif s == 0:
            menu()
            break
        else:
            print("\nInvalid Input")


# Sub Menu for adoption list
def adoption_sub_menu():
    print("1. Dog's ready to adopt")
    print("2. Cat's ready to adopt")
    print("0. Back to Menu")
    s = int(input("Enter Selection: "))
    if s == 1:
        adoption('dog')
        menu()
    elif s == 2:
        adoption('cat')
        menu()
    elif s == 0:
        menu()
    else:
        print("Invalid Input")


# Main menu
def menu():
    print("\n|Animal Sanctuary Main Menu|")
    print("1. Search for Animal")
    print("2. Create new entry")
    print("3. Update existing entry")
    print("4. Abandonment List")
    print("5. Abuser List")
    print("6. Adoption list")
    print("7. Return to owner, list")
    print("8. Quit")
    s = int(input("Enter Selection:"))
    # 1. Search for Animal Data by ID
    if s == 1:
        id_num = input("Enter Animals ID Number:").upper()
        return_animal_data(id_num)
        menu()
    # 2. Create new entry
    elif s == 2:
        new_entry_sub_menu()
    # 3. Update existing entry
    elif s == 3:
        update_entry_sub_menu()
    # 4. List of abuser names
    elif s == 4:
        abandoned()
        menu()
    # 5. List of names that have abandoned animals
    elif s == 5:
        abused()
        menu()
    # 6. Adoption list
    elif s == 6:
        adoption_sub_menu()
    # 7. Return to owners list
    elif s == 7:
        return_to_owner_pet()
        return_to_owner_wanimal()
        menu()
    # 8. Exit
    elif s == 8:
        print("|Programme Exited|")
        exit
    else:
        print("\nInvalid Input, Please Select Again\n")
        menu()


load_data()
menu()