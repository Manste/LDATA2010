import pandas as pd

read_file = pd.read_csv (r'.\instructions\data\BIOGRID-PROJECT-glioblastoma_project-CHEMICALS.chemtab.txt', sep='\t')
read_file.to_csv (r'.\data\edges.csv', index=None, header=True)

read_file = pd.read_csv (r'.\instructions\data\BIOGRID-PROJECT-glioblastoma_project-GENES.projectindex.txt', sep='\t')
read_file.to_csv (r'.\data\nodes.csv', index=None, header=True)