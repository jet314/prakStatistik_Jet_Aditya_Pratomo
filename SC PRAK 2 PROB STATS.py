#!/usr/bin/env python
# coding: utf-8

# In[3]:


a = [1, 2, -5, 0.3, 6, -2, 4] # numeric vector
b = ["one", "two", "three"] # character vector
c = [True, True, True, False, True] # logical vector
print(a)
print(b)
print(c)


# In[38]:


#MATRIKS
import numpy as np
cells = [3, 15, -27, 38]
r_jett = ["R1", "R2"]
c_jett = ["C1", "C2"]
nama_matrix = np.matrix(cells).reshape(2, 2)
print(nama_matrix)


# In[37]:


import pandas as pd
import numpy as np

jett1 = [1, 2, 3, 4]
jett2 = ["red", "white", "red", np.nan]  # Menggunakan np.nan untuk merepresentasikan NA
jett3 = [True, True, True, False]

dataku = pd.DataFrame({'ID': jett1, 'Color': jett2, 'Passed': jett3})
print(dataku)



# In[39]:


import pandas as pd

data_jett = pd.DataFrame({'id': list('abcdefghij'), 'x': list(range(1, 11)), 'y': list(range(11, 21))})
print(data_jett)


# In[8]:


pip install mysql-connector-python


# In[28]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="houseprices1"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM jett_houseprices;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
  


# In[30]:


import pandas as pd

# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

#Filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[df['Brick'] == 'No']

# Menampilkan hasiL fiLter
print("\nHasil Filter:")
print(df_filtered)


# In[36]:


import pandas as pd

# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

#Filter data berdasarkan kondisi yg kompleks
df_filtered = df[(df['Brick'] == 'No') | (df['Neighborhood'] == 'East')]

# Menampilkan hasiL fiLter
print(df_filtered)


# In[40]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ps2[jett]"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM data_jet;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
  


# In[42]:


import pandas as pd

# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

#Filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[df['COL 2'] == 'L']

# Menampilkan hasiL fiLter
print("\nHasil Filter:")
print(df_filtered)


# In[ ]:




