class User:
    name = ""
    curr_skills = []
    required_skills = []
    diffed_skills = []
    completed_gigs = []
    target_job = ""

    def __init__(self, nameIn, currSkills, requiredSkills):
        self.name = nameIn
        self.curr_skills = currSkills
        self.required_skills = requiredSkills
