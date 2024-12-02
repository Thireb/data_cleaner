import pandas as pd
df = pd.read_csv('final_general.csv')
text = df['Abstract']
value = text[:1]
print(type(value))