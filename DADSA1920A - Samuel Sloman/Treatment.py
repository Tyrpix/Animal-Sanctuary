class Treatment:
    def __init__(self, sanctuary_id, surgery, surgery_date, medication,
                 med_start, med_finish, abused_by, abandoned_by):
        self.sanctuary_id = sanctuary_id
        self.surgery = surgery
        self.surgery_date = surgery_date
        self.medication = medication
        self.med_start = med_start
        self.med_finish = med_finish
        self.abused_by = abused_by
        self.abandoned_by = abandoned_by

    def __str__(self):
        return_str = "Sanctuary: " + self.sanctuary_id + "|"
        return_str += "Surgery: " + self.surgery + "|"
        return_str += "Surgery Date: " + self.surgery_date + "|"
        return_str += "Medication: " + self.medication + "|"
        return_str += "Medication Start: " + self.med_start + "|"
        return_str += "Medication Finish: " + self.med_finish + "|"
        return_str += "Responsible for Abuse : " + self.abused_by + "|"
        return_str += "Responsible for Abandoning: " + self.abandoned_by + "|"
        return return_str

    

    