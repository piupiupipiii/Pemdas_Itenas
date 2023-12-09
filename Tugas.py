#pertanyaan no 1
import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)
#pertanyaan no 1
print("gaji sesudah peningkatan 5%: ")
bonus_persentase = 0.05
for index, row in df.iterrows():
    df.at[index, 'Persentase Bonus'] = bonus_persentase
    df.at[index, 'Bonus'] = row['Gaji'] * df.at[index, 'Persentase Bonus']

df['Total Gaji'] = df.apply(lambda row: row['Gaji'] + row['Bonus'], axis='columns')
print(df[['Nama', 'Usia', 'Total Gaji']])
print()

#pertanyaan no 2
print("rincian gaji dengan bonus tambahan 5% : ")
df['Total Gaji'] = df.apply(lambda row: row['Gaji'] + row['Bonus'], axis='columns')
print(df)
print()

#pertanyaan no 3
bonus_tambahan = 0.02
for index, row in df.iterrows():
    df.at[index, 'Bonus Tambahan'] = bonus_tambahan if row['Usia'] > 30 else 0
    df.at[index, 'dapat tambahan'] = 'Ya' if row['Usia'] > 30 else 'Tidak'

print("bonus tambahan untuk usia diatas 30 : ")
df['Bonus Tambahan'] = df.apply(lambda row: bonus_tambahan if row['dapat tambahan'] == 'Ya' else 0, axis='columns')
df['Tambahan'] = df.apply(lambda row: row['Bonus Tambahan'] * row['Total Gaji'], axis='columns')
df['Total Gaji Tambahan'] = df.apply(lambda row: row['Total Gaji'] + row['Tambahan'], axis='columns')
print(df[['Nama', 'Usia', 'Total Gaji', 'Tambahan', 'dapat tambahan','Total Gaji Tambahan']])
print()


#pertanyaan no 4
print("rincian semua total gaji dengan bonus dan tambahannya :")
df['Total Gaji Tambahan'] = df.apply(lambda row: row['Total Gaji'] + row['Tambahan'], axis='columns')
print(df)