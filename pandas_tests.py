import pandas as pd

donnees_data_frame = pd.read_csv('donnees_titanic1.txt', delimiter="\t")
print(donnees_data_frame)
donnees_ensemble_total = donnees_data_frame.values
print(donnees_ensemble_total)