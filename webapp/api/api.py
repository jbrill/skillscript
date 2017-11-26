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

def classifyGig(gigs):
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	for gig in gigs:
		entry = gig.getAllText()
		link = "http://localhost:5000/api/v1/getClassification"
		r = requests.get(link, json=({"post_entry": str(entry)}))
		print(r)
		json_val = (r.json())
		print("JSON_VAL:\t", json_val)
		entry = json_val[0]
		print("ENTRY:\t", entry)
		# classification = classifier.predict([entry])
		# print ("Classification:\t", json_val)
		print("PLZ WORK:\t", entry[2:-2])
		classification = entry[2:-2]
		gig.setClassification(classification)

@api.route('/api/v1/getSkills', methods=['POST', 'GET'])
def getSkills():
	if request.method == "POST":
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
						continue
		print ("FINAL GIGS:\t", returned_gigs)
		return jsonify(returned_gigs, 200)
		# gigs = getGigs()
	return
