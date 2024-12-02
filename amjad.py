import pandas as pd
df = pd.read_excel('work.xlsx')
df = df.drop(['Accredited'], axis=1)
ordered = df.sort_values(by=['First Name', 'Last Name'])
print(ordered)