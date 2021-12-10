import pandas as pd

df_edges = pd.read_csv("./txt-files/BIOGRID-PROJECT-glioblastoma_project-INTERACTIONS.tab3.txt", sep="\t", dtype='unicode')
print(df_edges.columns)
df_edges.to_csv("edges.csv", index=False)