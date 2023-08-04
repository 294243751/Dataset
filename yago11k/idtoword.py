import numpy as np
import pandas as pd

data = pd.read_table("all_data.txt", header=None)
data = np.array(data).tolist()
entity_df = pd.read_table("entity2id.txt", header=None)
entity_dict = dict(zip(entity_df[1], entity_df[0]))
relation_df = pd.read_table("relation2id.txt", header=None)
relation_dict = dict(zip(relation_df[1], relation_df[0]))

temp = []
for i in data:
    i[0] = entity_dict[i[0]]
    i[2] = entity_dict[i[2]]
    i[1] = relation_dict[i[1]]
    temp.append(i)

np.savetxt(r"original_data.txt", np.array(temp), encoding='utf-8',
           fmt='%s', delimiter='\t')
# np.savetxt(r"original_data.txt", encoding='utf-8',
#                    np.array(temp), fmt='%s', delimiter='\t')

