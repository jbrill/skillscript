import requests

def findCurrSkills(pastJobs):
	print (pastJobs)
	for job in pastJobs:
		# print (job)
		link = "http://api.dataatwork.org/v1/jobs/" + str(job)
		r = requests.get(link)
		json_val = (r.json())
		# print(json_val)
		uuid = json_val['uuid']
		# name = json_val['title']
		# desc = json_val['description']
		# print('UUID:\t', uuid)
		# print(y_test)
		# print(entry['title'] + ":\t" + y_test[0])
		link = "http://api.dataatwork.org/v1/jobs/" + str(uuid) + "/related_skills"
		r = requests.get(link)
		json_val = (r.json())

		# new_entry = {}
		# new_entry['classification'] = y_test[0]
		# new_entry['title'] = entry['title']
		skills = []
		if 'skills' in json_val:
			for skill in json_val['skills']:
				# print("SKILL:\t", skill)
				if skill['importance'] > 3:
					skills.append(skill['skill_name'])

		return skills
	    # if not 'skills' in json_val:
	    #     # no skills!
	    #     continue
	    # for new_skill in json_val['skills']:
	    #     #iterate through skills of a gig
	    #     if float(new_skill['importance']) > 3.0:
	    #         new_entry['weight'] = new_skill['importance']
	    #         if new_skill['normalized_skill_name'] in skills:
	    #             flag = False
	    #             for entry_title in skills[new_skill['normalized_skill_name']]:
	    #                 if entry_title['title'] == new_entry['title']:
	    #                     flag = True
	    #             if flag == True:
	    #                 print("DUPLICATE\n")
	    #             else:
	    #                 skills[new_skill['normalized_skill_name']].append(new_entry)
	    #                 # break
	    #         else:
	    #             skills[new_skill['normalized_skill_name']] = [new_entry]
	    #         # append our new entry

def findRequiredSkills(targetJob):
	link = "http://api.dataatwork.org/v1/jobs/" + str(targetJob)
	r = requests.get(link)
	json_val = (r.json())
	if json_val['uuid']:
		uuid = json_val['uuid']
	else:
		return []
	link = "http://api.dataatwork.org/v1/jobs/" + str(uuid) + "/related_skills"
	r = requests.get(link)
	json_val = (r.json())

	skills = []
	if 'skills' in json_val:
		for skill in json_val['skills']:
			# print("SKILL:\t", skill)
			if skill['importance'] > 3:
				skills.append(skill['skill_name'])

	return skills


def findGigSkills(gigList):
	for gig in gigList:
		link = "http://api.dataatwork.org/v1/jobs/" + str(gig.o_net_cat)
		r = requests.get(link)
		json_val = (r.json())
		if json_val['uuid']:
			uuid = json_val['uuid']
		else:
			continue
		link = "http://api.dataatwork.org/v1/jobs/" + str(uuid) + "/related_skills"
		r = requests.get(link)
		json_val = (r.json())

		skills = []
		if 'skills' in json_val:
			for skill in json_val['skills']:
				# print("SKILL:\t", skill)
				if skill['importance'] > 3:
					skills.append(skill['skill_name'])

		gig.addSkills(skills)
