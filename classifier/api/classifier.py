from flask import *
import pandas as pd
import requests
import csv
import sys
import nltk
from sklearn.cross_validation import train_test_split

classifier = Blueprint('classifier', __name__)

def train(classifier, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

    classifier.fit(X_train, y_train)
    print ("Accuracy: \t", str(classifier.score(X_test, y_test)))
    return classifier

myjobs = {}

df = pd.read_csv('sheets/jobs.csv', sep=',')

jobs = {}
with open('sheets/All_Occupations.csv', 'r') as jobscsv:
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

with open('sheets/Occupation Data (1).csv', 'r') as newcsv:
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

with open('sheets/Alternate Titles.csv', 'r') as altcsv:
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

with open('sheets/Sample of Reported Titles.csv', 'r') as samplcsv:
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

with open('sheets/Tools and Technology.csv', 'r') as toolscsv:
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

with open('sheets/Task Statements.csv', 'r') as taskscsv:
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

with open('sheets/Emerging Tasks.csv', 'r') as emscsv:
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

with open('sheets/Tasks to DWAs.csv', 'r') as DWAscsv:
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


with open('sheets/jobs copy.csv', 'w') as outcsv:
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

print("WORKING ON IT")

def stemming_tokenizer(text):
    stemmer = PorterStemmer()
    return [stemmer.stem(w) for w in word_tokenize(text)]

trial5 = Pipeline([
    ('vectorizer', TfidfVectorizer(tokenizer=stemming_tokenizer,
                             stop_words=stopwords.words('english') + list(string.punctuation))),
    ('classifier', MultinomialNB(alpha=0.05)),
])

classifier = train(trial5, values, keys)

print("CLASSIFIER READY")
