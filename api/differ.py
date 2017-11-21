def getDiffedSkills(user):
    user.diffed_skills = (set(user.curr_skills).intersection(user.required_skills))
