import pandas as pd

# Read the CSV into a pandas data frame (df)
#   With a df you can do many things
#   most important: visualize data with Seaborn
df = pd.read_csv('jobs.csv', sep=',')
print(df)

# Or export it in many ways, e.g. a list of tuples
tuples = [tuple(x) for x in df.values]

# or export it as a list of dicts
dicts = df.to_dict().values()
