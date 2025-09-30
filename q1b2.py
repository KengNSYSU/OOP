import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'PingFang TC', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

df_excel = [pd.read_excel('202403_cht.xlsx'), pd.read_excel('202404_cht.xlsx'), pd.read_excel('202405_cht.xlsx')]

selected_columns = [df['忠孝新生'] for df in df_excel]

plt.figure(figsize=(12, 8))

colors = ['red', 'blue', 'green']
labels = ['3月', '4月', '5月']
alpha = 0.7

plt.hist(selected_columns, bins=30, edgecolor='black', color=colors, label=labels, alpha=alpha)

plt.title('三個連續月份忠孝新生站進出人數直方圖')
plt.xlabel('進出人數')
plt.ylabel('天數')
plt.legend(loc='upper right')

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()