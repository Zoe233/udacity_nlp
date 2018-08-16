# 1. 加载数据集
import pandas as pd

df = pd.read_table('./../smsspamcollection/SMSSpamCollection', sep='\t', names=['label','sms_message'])
print(df.head())


# 2. 文本预处理：标准化--小写化、正则去除标点符号
# 3. 词袋模型：分词-词频计数-矩阵化
# 4. 