
class WildAnimal:
    def __init__(self, sanctuary_id, animal_type, vaccinated, admission_reason,
                 arrival_date, departure_date, destination, destination_address):
        self.sanctuary_id = sanctuary_id
        self.animal_type = animal_type
        self.vaccinated = vaccinated
        self.admission_reason = admission_reason
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        self.destination = destination
        self.destination_address = destination_address

    def __str__(self):
        return_str = "Sanctuary: " + self.sanctuary_id + "|"
        return_str += "Type: " + self.animal_type + "|"
        return_str += "Vaccinated: " + self.vaccinated + "|"
        return_str += "Reason for Admission: " + self.admission_reason + "|"
        return_str += "Date of Arrival: " + self.arrival_date + "|"
        return_str += "Date of Departure: " + self.departure_date + "|"
        return_str += "Destination: " + self.destination + "|"
        return_str += "Destination Address: " + self.destination_address + "|"
        return return_str

# Lower than 
    def __lt__(self, other):
        return self.sanctuary_id < other.sanctuary_id

# Greater than
    def __gt__(self, other):
        return self.sanctuary_id > other.sanctuary_id
