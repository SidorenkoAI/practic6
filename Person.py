class Person:
    def __init__(self):
        self.first_name_changes = {}
        self.last_name_changes = {}

    def ChangeFirstName(self, year, first_name):
        self.first_name_changes[year] = first_name

    def ChangeLastName(self, year, last_name):
        self.last_name_changes[year] = last_name

    def GetFullName(self, year):
        first_name = self.find_latest_change(year, self.first_name_changes)
        last_name = self.find_latest_change(year, self.last_name_changes)

        if first_name is None and last_name is None:
            return "Incognito"
        elif first_name is None:
            return f"{last_name} with unknown first name"
        elif last_name is None:
            return f"{first_name} with unknown last name"
        else:
            return f"{first_name} {last_name}"

    def find_latest_change(self, year, changes):
        latest_change = None
        for change_year in changes:
            if change_year <= year:
                latest_change = changes[change_year]
            else:
                break
        return latest_change
