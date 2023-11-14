import numpy as np
import pandas as pd
import random,pdb
import torch
from torch.utils.data import Dataset,DataLoader
from accelerate import Accelerator

# 生成卷积操作时需要的两列数据的组合的列表

## N 矩阵行数
def generate_combination(N):
    col = []
    col_rev = []
    for i in range(1, N):
        for j in range(0, i):
            col.append([i, j])
            col_rev.append([j, i])
    return col, col_rev

## N矩阵行数,M样本数
def sample_combination(N, M): 
    col = []
    col_rev = []
    sample = [i for i in range(0, M)]
    sample = random.sample(sample, N)
    for i in range(1, N):
        for j in range(0, i):
            col.append([sample[i],sample[j]])
            col_rev.append([sample[j],sample[i]])
    return col, col_rev

# 根据输入的矩阵和卷积操作的步长, 计算卷积操作的索引
def get_index_list(matrix, stride):
    W = matrix.shape[3]
    if W % stride == 0:
        index_list = list(np.arange(0, W + stride, stride))
    else:
        mod = W % stride
        index_list = list(np.arange(0, W + stride - mod, stride)) + [W]
    return index_list


class AlphaData(Dataset):

    def __init__(self, train_x, train_y):
        self.len = len(train_x)
        self.x_data = train_x
        self.y_data = train_y

    def __getitem__(self, index):
        """
        指定读取数据的方式: 根据索引index返回dataset[index]

        """
        return self.x_data[index].float(), self.y_data[index].float()

    def __len__(self):
        return self.len
    
def siblings(data_raw, features, target, window):
    raw = data_raw[features]
    names = []
    res = []
    for i in range(0, window):
        names += ["{0}_{1}d".format(c,i) for c in features]
        res.append(raw.unstack().shift(i).stack())
    dt = pd.concat(res,axis=1)
    dt.columns = names
    dt = pd.concat([dt, data_raw[target]],axis=1)
    dt = dt.dropna()
    x_array = [mv.T.reshape(len(features),-1) for mv in dt[names].values]
    x_array = np.array(x_array)
    y_array = [mv for mv in dt[target].values]
    y_array = np.array(y_array)
    return x_array,y_array.reshape(-1)

def create_data(data_raw, features, target, window, 
                batch_size, slicing=0.2, shuffle=False):
    pos = int(len(data_raw) * (1 - slicing))
    train_data = data_raw.iloc[:pos]
    test_data = data_raw.iloc[pos:]
    train_loader = data_loader(train_data, features=features, 
                               target=target, window=window, 
                               batch_size=batch_size, 
                               shuffle=shuffle)
    
    test_loader = data_loader(test_data, features=features, 
                               target=target, window=window, 
                               batch_size=batch_size, 
                               shuffle=shuffle)
    return train_loader, test_loader


def data_loader(data_raw, features, target, window, 
                batch_size, shuffle=False):
    accelerator = Accelerator()
    x_array,y_array = siblings(
        data_raw=data_raw, features=features,
        target=target, window=window)
    
    x_array = torch.from_numpy(np.array(x_array)).reshape(len(x_array), 1, len(features), window)
    y_array = torch.from_numpy(np.array(y_array)).reshape(len(y_array), 1)

    dataset = AlphaData(x_array, y_array)
    data_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=shuffle)
    return data_loader#accelerator.prepare(data_loader)
    
