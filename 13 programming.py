#QUESTION 1
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Data_Penduduk_EN.xlsx')

occupation_counts = df['Profesi'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(occupation_counts, labels=occupation_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Occupations in Desa Cibodas')
plt.axis('equal')  
plt.show()


#QUESTION2
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Data_Penduduk_EN.xlsx')
df.columns = df.columns.str.strip()  
edu_gender = df.groupby(['last education', 'sex']).size().unstack()

edu_gender.plot(kind='bar', figsize=(10, 6))
plt.title('Education Level Comparison by Sex')
plt.xlabel('Last Education')
plt.ylabel('Number of Citizens')
plt.xticks(rotation=45)
plt.legend(title='Sex')
plt.tight_layout()
plt.show()


#QUESTION 3
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Data_Penduduk_EN.xlsx'
df = pd.read_excel(file_path)

def categorize_income(income):
    if income < 1000000:
        return 'Very Low'
    elif income < 2000000:
        return 'Low'
    elif income < 4000000:
        return 'Middle'
    else:
        return 'High'

df['Income_Category'] = df['Monthly Income'].apply(categorize_income)

category_counts = df['Income_Category'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Income Distribution in Desa Cibodas')
plt.axis('equal')
plt.show()






