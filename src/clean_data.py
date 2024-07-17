import json
import pandas as pd

# 加载数据
with open('/Users/lizzie/Desktop/ChatBot-For-Stardew-Valley/data/raw/villagers.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 转换为DataFrame进行分析
df = pd.DataFrame(data)
print(df.head())

# 检查缺失值
print(df.isnull().sum())


print(df.dtypes)