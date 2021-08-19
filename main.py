class Mentors:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.curses = []



class Lectures(Mentors):
    def __init__(self,name,surname):
        super().__init__(name,surname)



class Reviewer(Mentors):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    





