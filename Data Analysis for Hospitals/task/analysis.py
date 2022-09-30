# write your code here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 8)

# ----------------MAKE DF Reports Viewable----------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', None)

general_df = pd.read_csv('test/general.csv')
prenatal_df = pd.read_csv('test/prenatal.csv')
sports_df = pd.read_csv('test/sports.csv')
columns = ['Unnamed: 0', 'hospital', 'gender', 'age', 'height', 'weight',
           'bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound',
           'mri', 'xray', 'children', 'months']
prenatal_df.columns = columns
sports_df.columns = columns

df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)

df.drop(columns='Unnamed: 0', inplace=True)

df.dropna(axis=0, how='all', inplace=True)

df.gender.replace(['female', 'woman'], 'f', inplace=True)
df.gender.replace(['male', 'man'], 'm', inplace=True)

df.gender.fillna('f', inplace=True)

columns = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
df[columns] = df[columns].fillna(0)
x = df[df['hospital'] == 'general']
result = x.diagnosis.value_counts().loc['stomach'] / x.diagnosis.shape[0]
x = df[df['hospital'] == 'sports']
result_b = x.diagnosis.value_counts().loc['dislocation']/ x.diagnosis.shape[0]
median_general = df.age[df.hospital == 'general'].agg('median')
medial_sports = df.age[df.hospital == 'sports'].agg('median')

x = df.groupby(['hospital', 'blood_test']).agg({"blood_test" : 'count'})
# print(x)
print(f"The answer to the 1st question: 15-35")
print("The answer to the 2nd question: pregnancy")
print("The answer to the 3rd question: It's because...")

plt.hist(x=df.age, bins=5)
plt.show()
data = df.diagnosis.value_counts(sort=False)
plt.pie(data, labels = df.diagnosis.unique())
plt.show()
ax = sns.violinplot(x="hospital", y="height", data=df)
plt.show()



