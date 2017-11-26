class Gig:
    title = ""
    description = ""
    url = ""
    o_net_cat = ""
    skills = []

    def __init__(self, titleIn, descIn, urlIn):
        self.title = titleIn
        self.Redescription = descIn
        self.url = urlIn

    def getAllText(self):
        return self.title + self.description

    def setClassification(self, classification):
        self.o_net_cat = classification

    def addSkills(self, skills_in):
        self.skills = skills_in

    def __repr__(self):
        return "{}: {}\n{}\n{}\nSkills\t:{}".format(self.title, self.description, self.url, self.o_net_cat, self.skills)

    def as_dict(self):
       return {c: getattr(self, c) for c in dir(self)}
