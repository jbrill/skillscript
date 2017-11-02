import pandas as pd
import requests
import csv
import sys
import nltk
from sklearn.cross_validation import train_test_split

def train(classifier, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

    classifier.fit(X_train, y_train)
    print ("Accuracy: \t", str(classifier.score(X_test, y_test)))
    return classifier

myjobs = {}

df = pd.read_csv('jobs.csv', sep=',')

jobs = {}
with open('All_Occupations.csv', 'r') as jobscsv:
    onetreader = csv.reader(jobscsv)

    jobs = {row[0]:row[1] for row in onetreader}

career_pathways = df['Career Pathways (O*Net Data)']
career_title = df['Title']
career_category = df['Category']
career_job_title = df['Job Title']
career_skills = df['Skills required (if listed)']
career_additional = df['Additional Requirements']

master_pathways = {}


keys = list(jobs.keys())
values = list(jobs.values())

with open('Occupation Data (1).csv', 'r') as newcsv:
    new_reader = csv.reader(newcsv)

    description = {}

    for row in new_reader:
        if row[0] in description:
            description[row[0]] += str(row[1] + " " + row[2]+ " ")
        else:
            description[row[0]] = str(row[1] + " " + row[2]+ " ")

    new_keys = list(description.keys())
    new_values = list(description.values())

    keys.extend(new_keys)
    values.extend(new_values)

with open('Alternate Titles.csv', 'r') as altcsv:
    alt_reader = csv.reader(altcsv)

    alts = {}

    for row in alt_reader:
        if row[0] in alts:
            alts[row[0]] += str(row[1] + " " + row[2]+ " ")
        else:
            alts[row[0]] = str(row[1] + " " + row[2]+ " ")

    new_keys = list(alts.keys())
    new_values = list(alts.values())

    keys.extend(new_keys)
    values.extend(new_values)

with open('Sample of Reported Titles.csv', 'r') as samplcsv:
    samp_reader = csv.reader(samplcsv)

    samps = {}

    for row in samp_reader:
        if row[0] in samps:
            samps[row[0]] += str(row[1] + " " + row[2]+ " ")
        else:
            samps[row[0]] = str(row[1] + " " + row[2]+ " ")

    new_keys = list(samps.keys())
    new_values = list(samps.values())

    keys.extend(new_keys)
    values.extend(new_values)

with open('Tools and Technology.csv', 'r') as toolscsv:
    tools_reader = csv.reader(toolscsv)

    tools = {}

    for row in tools_reader:
        if row[0] in tools:
            tools[row[0]] += str(row[1] + " " + row[2]+ " " + row[3] + " ")
        else:
            tools[row[0]] = str(row[1] + " " + row[2]+ " " + row[3] + " ")

    new_keys = list(tools.keys())
    new_values = list(tools.values())

    keys.extend(new_keys)
    values.extend(new_values)

with open('Task Statements.csv', 'r') as taskscsv:
    tasks_reader = csv.reader(taskscsv)

    tasks = {}

    for row in tasks_reader:
        if row[0] in tasks:
            tasks[row[0]] += str(row[1] + " " + row[3] + " ")
        else:
            tasks[row[0]] = str(row[1] + " " + row[3] + " ")

    new_keys = list(tasks.keys())
    new_values = list(tasks.values())

    keys.extend(new_keys)
    values.extend(new_values)

with open('Emerging Tasks.csv', 'r') as emscsv:
    emerge_reader = csv.reader(emscsv)

    emerge = {}

    for row in emerge_reader:
        if row[0] in emerge:
            emerge[row[0]] += str(row[1] + " " + row[2] + " " + row[5] + " ")
        else:
            emerge[row[0]] = str(row[1] + " " + row[2] + " " + row[5] + " ")

    new_keys = list(emerge.keys())
    new_values = list(emerge.values())

    keys.extend(new_keys)
    values.extend(new_values)

with open('Tasks to DWAs.csv', 'r') as DWAscsv:
    dwa_reader = csv.reader(DWAscsv)

    dwa = {}

    for row in dwa_reader:
        if row[0] in dwa_reader:
            dwa[row[0]] += str(row[1] + " " + row[3] + " " + row[5] + " ")
        else:
            dwa[row[0]] = str(row[1] + " " + row[3] + " " + row[5] + " ")

    new_keys = list(dwa.keys())
    new_values = list(dwa.values())

    keys.extend(new_keys)
    values.extend(new_values)

# for index in range(0, len(career_pathways)):
#     pathway = career_pathways[index]
#     if isinstance(pathway, float):
#         continue
#     onet_number = pathway.split(' -')[0]
#
#     textset = str(career_title[index])
#     textset += " " + str(career_category[index])
#     textset += " " + str(career_job_title[index])
#     textset += " " + str(career_skills[index])
#     textset += " " + str(career_additional[index])
#
#     keys.append(onet_number)
#     values.append(textset)
#
#     if onet_number in master_pathways:
#         #already exists
#         continue
#     print (onet_number)
#     print ("PATHWAY\t", pathway)
#     # addToDict(pathway)
#     try:
#         link = "http://api.dataatwork.org/v1/jobs/" + str(onet_number)
#         print (link)
#         r = requests.get(link)
#         json_val = (r.json())
#         uuid = json_val['uuid']
#         name = json_val['title']
#         desc = json_val['description']
#
#         try:
#             master_pathways[onet_number] = {}
#             master_pathways[onet_number]['name'] = name
#             master_pathways[onet_number]['uuid'] = uuid
#             master_pathways[onet_number]['description'] = desc
#             master_pathways[onet_number]['skills'] = []
#             link = "http://api.dataatwork.org/v1/jobs/" + str(uuid) + "/related_skills"
#             r = requests.get(link)
#             json_val = (r.json())
#             if not 'skills' in json_val:
#                 continue
#             for index in range(0,5):
#                 print (json_val['skills'][index]['skill_name'])
#
#
#                 master_pathways[onet_number]['skills'].append(json_val['skills'][index]['skill_name'])
#             print (master_pathways)
#             # break
#
#         except requests.exceptions.RequestException as e:  # This is the correct syntax
#             print (e)
#             sys.exit(1)
#
#
#     except requests.exceptions.RequestException as e:  # This is the correct syntax
#         print (e)
#         sys.exit(1)



with open('jobs copy.csv', 'w') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["Name", "Onet #", "Uuid", "Description", "Related Skills"])



    for onetnum in master_pathways:
        # print (onet/num)
        # print (master_pathways[onetnum]['name'])
        writer.writerow([master_pathways[onetnum]['name'], onetnum, master_pathways[onetnum]['uuid'], master_pathways[onetnum]['description'], ','.join(map(str, master_pathways[onetnum]['skills']))])
        keys.append(onetnum)
        values.append(str(master_pathways[onetnum]['name'] + " " +  master_pathways[onetnum]['uuid'] + " " + master_pathways[onetnum]['description']))
        # sys.exit(1)

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
import string
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk import word_tokenize


def stemming_tokenizer(text):
    stemmer = PorterStemmer()
    return [stemmer.stem(w) for w in word_tokenize(text)]

trial5 = Pipeline([
    ('vectorizer', TfidfVectorizer(tokenizer=stemming_tokenizer,
                             stop_words=stopwords.words('english') + list(string.punctuation))),
    ('classifier', MultinomialNB(alpha=0.05)),
])
print (keys)
# print (values)
classifier = train(trial5, values, keys)

print (len(values))

print(type(classifier))

import feedparser

LINK = "https://detroit.craigslist.org/d/jobs/search/jjj?format=rss"

entries = []
skills = {}
feed = feedparser.parse(LINK)
print ("LENGTH OF FEED:\t", len(feed['entries']))
for entry in feed['entries']:
    print ("ENTRY:\n", entry)
    entr = entry['summary'] + " " + entry['title']
    entries.append(entr)
    y_test = classifier.predict([entr])
    link = "http://api.dataatwork.org/v1/jobs/" + str(y_test[0])
    r = requests.get(link)
    json_val = (r.json())
    uuid = json_val['uuid']
    name = json_val['title']
    desc = json_val['description']
    print('UUID:\t', uuid)
    print(y_test)
    print(entry['title'] + ":\t" + y_test[0])
    link = "http://api.dataatwork.org/v1/jobs/" + str(uuid) + "/related_skills"
    r = requests.get(link)
    json_val = (r.json())

    new_entry = {}
    new_entry['classification'] = y_test[0]
    new_entry['title'] = entry['title']


    if not 'skills' in json_val:
        # no skills!
        continue
    for new_skill in json_val['skills']:
        #iterate through skills of a gig
        if float(new_skill['importance']) > 3.0:
            new_entry['weight'] = new_skill['importance']
            if new_skill['normalized_skill_name'] in skills:
                flag = False
                for entry_title in skills[new_skill['normalized_skill_name']]:
                    if entry_title['title'] == new_entry['title']:
                        flag = True
                if flag == True:
                    print("DUPLICATE\n")
                else:
                    skills[new_skill['normalized_skill_name']].append(new_entry)
                    # break
            else:
                skills[new_skill['normalized_skill_name']] = [new_entry]
            # append our new entry

for skill in skills:
    print (skill, "\n")
    for gig in skills[skill]:
        print (gig['title'] + ": \t" + str(gig['weight']))
    print ("\n\n")


#     print(y_test)
#
# for idx in range(0, len(entries)):
#     print (entries[idx] + ":\t" + y_test[idx])
