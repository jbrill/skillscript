import pandas as pd
import requests
import csv
import sys

# Read the CSV into a pandas data frame (df)
#   With a df you can do many things
#   most important: visualize data with Seaborn
df = pd.read_csv('jobs.csv', sep=',')
print(df)

# Or export it in many ways, e.g. a list of tuples
# tuples = [tuple(x) for x in df.values]

# or export it as a list of dicts
# dicts = df.to_dict().values()

career_pathways = df['Career Pathways (O*Net Data)']

# print ("CAREER PATHWAYS\t", saved_column)

master_pathways = {}

for pathway in career_pathways:
    if isinstance(pathway, float):
        continue
    onet_number = pathway.split(' -')[0]
    if onet_number in master_pathways:
        #already exists
        continue
    print (onet_number)
    try:
        link = "http://api.dataatwork.org/v1/jobs/" + str(onet_number)
        print (link)
        r = requests.get(link)
        json_val = (r.json())
        uuid = json_val['uuid']
        name = json_val['title']
        desc = json_val['description']

        try:
            master_pathways[onet_number] = {}
            master_pathways[onet_number]['name'] = name
            master_pathways[onet_number]['uuid'] = uuid
            master_pathways[onet_number]['description'] = desc
            master_pathways[onet_number]['skills'] = []
            link = "http://api.dataatwork.org/v1/jobs/" + str(uuid) + "/related_skills"
            r = requests.get(link)
            json_val = (r.json())
            if not 'skills' in json_val:
                continue
            for index in range(0,5):
                print (json_val['skills'][index]['skill_name'])


                master_pathways[onet_number]['skills'].append(json_val['skills'][index]['skill_name'])
            print (master_pathways)
            # break

        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print (e)
            sys.exit(1)


    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
        sys.exit(1)

with open('jobs copy.csv', 'w') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["Name", "Onet #", "Uuid", "Description", "Related Skills"])



    for onetnum in master_pathways:
        # print (onet/num)
        # print (master_pathways[onetnum]['name'])
        writer.writerow([master_pathways[onetnum]['name'], onetnum, master_pathways[onetnum]['uuid'], master_pathways[onetnum]['description'], ','.join(map(str, master_pathways[onetnum]['skills']))])
        # sys.exit(1)


# print ("DICTS\n", dicts)
# # index = 0;
# for line in dicts:
#     # if index > 2:
#         # break
#     print ("LINE\n", line)
#     # for num in line:
#         # print (line[num])
    # index += 1
