from flask import *
import feedparser
from .mapper import *
from .user import *
from .differ import *
from .scraper import *

# import sys
# sys.path.insert(0, '..models')
# import sys
# sys.path.append('..')
# from models import *
# from .classifier import classifier

api = Blueprint('api', __name__, template_folder='templates')

# @api.route('/api/v1/gigs', methods=['POST', 'GET'])
# @api.route('/api/v1/gigs/<gigid>', methods=['POST', 'GET'])
# def getGigs():
# 	# if request.method == "GET":
# 	LINK = "https://detroit.craigslist.org/d/jobs/search/jjj?format=rss"
#
# 	entries = []
# 	skills = {}
# 	entries_num = 0
# 	feed = feedparser.parse(LINK)
# 	print ("LENGTH OF FEED:\t", len(feed['entries']))
# 	for entry in feed['entries']:
# 	    entries_num += 1
# 	    print ("ENTRY:\n", entry)
# 	    entr = entry['summary'] + " " + entry['title']
# 	    entries.append(entr)
# 	    y_test = classifier.predict([entr])
# 	    link = "http://api.dataatwork.org/v1/jobs/" + str(y_test[0])
# 	    r = requests.get(link)
# 	    json_val = (r.json())
# 	    uuid = json_val['uuid']
# 	    name = json_val['title']
# 	    desc = json_val['description']
# 	    print('UUID:\t', uuid)
# 	    print(y_test)
# 	    print(entry['title'] + ":\t" + y_test[0])
# 	    link = "http://api.dataatwork.org/v1/jobs/" + str(uuid) + "/related_skills"
# 	    r = requests.get(link)
# 	    json_val = (r.json())
#
# 	    new_entry = {}
# 	    new_entry['classification'] = y_test[0]
# 	    new_entry['title'] = entry['title']
#
#
# 	    if not 'skills' in json_val:
# 	        # no skills!
# 	        continue
# 	    for new_skill in json_val['skills']:
# 	        #iterate through skills of a gig
# 	        if float(new_skill['importance']) > 3.0:
# 	            new_entry['weight'] = new_skill['importance']
# 	            if new_skill['normalized_skill_name'] in skills:
# 	                flag = False
# 	                for entry_title in skills[new_skill['normalized_skill_name']]:
# 	                    if entry_title['title'] == new_entry['title']:
# 	                        flag = True
# 	                if flag == True:
# 	                    print("DUPLICATE\n")
# 	                else:
# 	                    skills[new_skill['normalized_skill_name']].append(new_entry)
# 	                    # break
# 	            else:
# 	                skills[new_skill['normalized_skill_name']] = [new_entry]
# 	            # append our new entry
#
# 	skill_len = 0
# 	gig_len = 0
# 	for skill in skills:
# 	    skill_len += 1
# 	    print (skill, "\n")
# 	    for gig in skills[skill]:
# 	        gig_len += 1
# 	        print (gig['title'] + ": \t" + str(gig['weight']))
# 	    print ("\n\n")
#
# 	print("SKILL_LEN:\t", str(skill_len))
# 	print("GIG_LEN:\t", str(gig_len))
# 	print("ENTRY_LEN:\t", str(entries_num))
# 	return

def classifyGig(gigs):
	from .classifier import classifier
	for gig in gigs:
		entry = gig.getAllText()
		# print("ENTRY:\t", entry)
		classification = classifier.predict([entry])
		print ("Classification:\t", classification)
		gig.setClassification(classification[0])

@api.route('/api/v1/getSkills', methods=['POST', 'GET'])
def getSkills():
	if request.method == "POST":
		print("HERE")
		print(request.json)
		userName = request.json['userName']
		pastJobs = request.json['pastJobs'].split(',')
		targetJob = request.json['targetJob']

		currSkills = findCurrSkills(pastJobs)
		print ("CURRSKILLS:\t", currSkills)

		requiredSkills = findRequiredSkills(targetJob)

		user = User(userName, currSkills, requiredSkills)
		print ("REQUIREDSKILLS:\t", requiredSkills)
		getDiffedSkills(user)
		print ("DIFFEDSKILLS:\t", user.diffed_skills)
		gigs = getEntries()
		print("Importing Classifier!")


		classifyGig(gigs)

		findGigSkills(gigs)

		returned_gigs = {}

		for skill in user.diffed_skills:
			print(skill)
			returned_gigs[skill] = []
			for gig in gigs:
				print("SKILLS\t", gig.skills)
				for gig_skill in gig.skills:
					print (skill, ":\t", gig_skill)
					if gig_skill == skill:
						new_gig = {}
						new_gig['title'] = gig.title
						new_gig['description'] = gig.description
						new_gig['url'] = gig.url
						new_gig['o_net_cat'] = gig.o_net_cat
						new_gig['skills'] = gig.skills
						# new_gig['skill_needed'] = skill
						returned_gigs[skill].append(new_gig)
		print ("FINAL GIGS:\t", returned_gigs)
		return jsonify(returned_gigs, 200)
		# gigs = getGigs()
	return
