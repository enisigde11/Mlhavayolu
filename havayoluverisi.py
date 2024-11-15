# -*- coding: utf-8 -*-
"""Havayoluverisi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JJj9yAbBEIEF_40ptSZM9pW2-KnuLp-k
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv('Havayoluverisi.csv')

df.drop(columns=['id'],inplace=True)

pd.get_dummies(df, columns=['Gender','Customer Type','Type of Travel','Class','satisfaction'],drop_first=True)

# Replace the problematic values with numerical representations before converting to integers.
# For example, you can use a dictionary to map the string values to integers.
class_mapping = {'Eco Plus': 1, 'Business': 2, 'Eco': 3}  # Add other mappings as needed
df['Class'] = df['Class'].map(class_mapping)

# Now, you should be able to convert the column to integers.
df['Class'] = df['Class'].astype('int')

# Replace string values in 'satisfaction' column with numerical representations.
satisfaction_mapping = {'satisfied': 1, 'neutral or dissatisfied': 0}
df['satisfaction'] = df['satisfaction'].map(satisfaction_mapping)

# Now, convert the column to integers.
df['satisfaction'] = df['satisfaction'].astype(int)

# Replace string values in 'Gender' column with numerical representations.
gender_mapping = {'Male': 1, 'Female': 0}  # Or any other mapping you prefer
df['Gender'] = df['Gender'].map(gender_mapping)

# Now, convert the column to integers.
df['Gender'] = df['Gender'].astype(int)

# Define mappings for 'Customer Type' and 'Type of Travel'
customer_type_mapping = {'Loyal Customer': 1, 'disloyal Customer': 0}  # Customize as needed
travel_type_mapping = {'Business travel': 1, 'Personal Travel': 0}  # Customize as needed

# Apply the mappings and convert to integers
df['Customer Type'] = df['Customer Type'].map(customer_type_mapping).astype(int)
df['Type of Travel'] = df['Type of Travel'].map(travel_type_mapping).astype(int)

df['Arrival Delay in Minutes']=pd.to_numeric(df['Arrival Delay in Minutes'])

y=df[['satisfaction']]
x=df.drop("satisfaction",axis=1)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

lm=LinearRegression()
model=lm.fit(x_train,y_train)
model.score(x_test,y_test)

#lm=LinearRegression()
#model=lm.fit(x,y)
#model.score(x,y)

df.head(3)

# ... (Kodunuzun önceki kısımları) ...

# Tahminleri yapın
tahminler = model.predict(x_test)

# İlk 5 tahmini yazdırın
print(tahminler[:5])

# Tahminleri yapın (eğer daha önce yapmadıysanız)
tahminler = model.predict(x_test)

# Tahminleri ve gerçek değerleri bir DataFrame'de birleştirin
sonuclar = pd.DataFrame({'Gerçek Değer': y_test['satisfaction'], 'Tahmin': tahminler.flatten()})

# Sonuçları yazdırın
print(sonuclar.head(50))