import pandas as pd
import requests


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

for pathway in career_pathways:
    try:
        onet_number = pathway.split(' -')[0]
        print (onet_number)
        try:
            link = "https://services.onetcenter.org/ws/online/occupations/"+str(onet_number)+"/summary/skills"
            print (link)
            # r = requests.get("https://services.onetcenter.org/ws/online/occupations/"+str(onet_number)+"/summary/skills")
            # r.json()
        except:
            print ("REQUEST PROBLEM:\t", onet_number)
            print ("REQUEST PROBLEM:\t", onet_number)

    except:
        print ("ERROR\t:", pathway)

    # if pathway.contains('nan'):
    #     continue
    # else:
    # print (pathway)


# print ("DICTS\n", dicts)
# # index = 0;
# for line in dicts:
#     # if index > 2:
#         # break
#     print ("LINE\n", line)
#     # for num in line:
#         # print (line[num])
    # index += 1
