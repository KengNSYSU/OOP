import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'PingFang TC', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

df_excel = [pd.read_excel('202403_cht.xlsx'), pd.read_excel('202404_cht.xlsx'), pd.read_excel('202405_cht.xlsx')]

selected_columns = [df['忠孝新生'] for df in df_excel]
selected_total = [df['忠孝新生'].sum() for df in df_excel]

categories = ['3月', '4月', '5月']

plt.bar(categories, selected_total)
plt.title('三個月份忠孝新生出站人數盒鬚圖')
plt.show()