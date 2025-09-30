import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'PingFang TC', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

df_excel = pd.read_excel('202403_cht.xlsx')
stations = ['亞東醫院', '頂溪', '忠孝新生', '南京三民']
selected_columns = df_excel[stations]

plt.figure(figsize=(12, 8))

for station in stations:
    plt.plot([i+1 for i in range(31)], selected_columns[station], marker='o', label=station, linewidth=2, markersize=4)

plt.title('各捷運站3月份出站人數折線圖', fontsize=16, fontweight='bold')
plt.xlabel('日期', fontsize=12)
plt.ylabel('出站人數', fontsize=12)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()