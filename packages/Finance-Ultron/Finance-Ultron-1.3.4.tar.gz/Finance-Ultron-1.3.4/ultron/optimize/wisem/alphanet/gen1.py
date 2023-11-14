import numpy as np
import torch,importlib
import torch.nn as nn
from accelerate import Accelerator
from ultron.optimize.wisem.alphanet.utilz import *

class GRU(nn.Module):

    def __init__(self,input_size, hidden_size=30,
                 num_layers=2,
                 batch_first=True,
                 bidirectional=False):
        super(GRU, self).__init__()
        self.gru = nn.GRU(input_size=input_size,
                          hidden_size=hidden_size,
                          num_layers=num_layers,
                          batch_first=batch_first,
                          bidirectional=bidirectional)

    def forward(self, data):
        output, hn = self.gru(data)
        h = hn[-1:]  #  h: torch.Size([1, 1000, 30])
        data = h.squeeze(0)  # torch.Size([1000, 30])
        return data  # torch.Size([1000, 30])

class Inception(nn.Module):
    """
    Inception, 用于提取时间序列的特征, 具体操作包括：
    """

    def __init__(self, combination, combination_rev, feature_size, hidden_size,
                 index_list):
        """
        combination: 卷积操作时需要的两列数据的组合
        combination_rev: 卷积操作时需要的两列数据的组合, 与combination相反
        index_list: 卷积操作时需要的时间索引
        
        """

        super(Inception, self).__init__()
        #self.name = name
        # 卷积操作时需要的两列数据的组合
        self.combination = combination
        self.combination_rev = combination_rev

        # 卷积操作时需要的时间索引
        self.index_list = index_list

        self.convt = nn.Conv2d(
            in_channels=1, out_channels=1, 
            kernel_size=1, bias=True)

        self.feature_size = feature_size
        # 卷积操作后 Normalization层
        self.bc1 = nn.BatchNorm2d(1)
        self.bc2 = nn.BatchNorm2d(1)
        self.bc3 = nn.BatchNorm2d(1)
        self.bc4 = nn.BatchNorm2d(1)
        self.bc5 = nn.BatchNorm2d(1)
        self.bc6 = nn.BatchNorm2d(1)
        self.bc7 = nn.BatchNorm2d(1)
        self.bc8 = nn.BatchNorm2d(1)
        self.bc9 = nn.BatchNorm2d(1)
        self.bc10 = nn.BatchNorm2d(1)
        self.bc11 = nn.BatchNorm2d(1)
        self.bc12 = nn.BatchNorm2d(1)
        self.bc13 = nn.BatchNorm2d(1)
        self.bc14 = nn.BatchNorm2d(1)

        self.GRU = GRU(input_size= 2 * len(self.combination) + 12 * self.feature_size,
                       hidden_size=hidden_size)

    # batch_size*1*9*30
    def forward(self, data):
        # 本层 在训练时不需要反向传播, 因此可以使用detach()函数
        data = data.detach().cpu().numpy()
        combination = self.combination
        combination_rev = self.combination_rev
        # 卷积
        conv1 = self.ts_corr4d(data, combination,
                               combination_rev).to(torch.float).to('cuda')
        conv2 = self.ts_cov4d(data, combination,
                              combination_rev).to(torch.float).to('cuda')
        
        conv3 = self.ts_stddev4d(data).to(torch.float).to('cuda')
        conv4 = self.ts_zscore4d(data).to(torch.float).to('cuda')
        conv5 = self.ts_return4d(data).to(torch.float).to('cuda')
        conv6 = self.ts_decaylinear4d(data).to(torch.float).to('cuda')
        conv7 = self.ts_mean4d(data).to(torch.float).to('cuda')

        conv8 = self.ts_min4d(data).to(torch.float).to('cuda')
        conv9 = self.ts_var4d(data).to(torch.float).to('cuda')
        conv10 = self.ts_sum4d(data).to(torch.float).to('cuda')

        conv11 = self.ts_median4d(data).to(torch.float).to('cuda')
        conv12 = self.ts_skew4d(data).to(torch.float).to('cuda')
        conv13 = self.ts_kurtosis4d(data).to(torch.float).to('cuda')
        conv14 = self.ts_sum4d(data).to(torch.float).to('cuda')

        conv1 = self.convt(conv1).to(torch.float)
        conv2 = self.convt(conv2).to(torch.float)
        conv3 = self.convt(conv3).to(torch.float)
        conv4 = self.convt(conv4).to(torch.float)
        conv5 = self.convt(conv5).to(torch.float)
        conv6 = self.convt(conv6).to(torch.float)
        conv7 = self.convt(conv7).to(torch.float)
        conv8 = self.convt(conv8).to(torch.float)
        conv9 = self.convt(conv9).to(torch.float)
        conv10 = self.convt(conv10).to(torch.float)
        conv11 = self.convt(conv11).to(torch.float)
        conv12 = self.convt(conv12).to(torch.float)
        conv13 = self.convt(conv13).to(torch.float)
        conv14 = self.convt(conv14).to(torch.float)
        
        
        #  Normalization
        batch1 = self.bc1(conv1)  # combination * combination_rev
        batch2 = self.bc2(conv2)  # combination * combination_rev
        batch3 = self.bc3(conv3)  # feature_size
        batch4 = self.bc4(conv4)  # feature_size
        batch5 = self.bc5(conv5)  # feature_size
        batch6 = self.bc6(conv6)  # feature_size
        batch7 = self.bc7(conv7)  # feature_size
        batch8 = self.bc8(conv8)  # feature_size
        batch9 = self.bc9(conv9)  # feature_size
        batch10 = self.bc10(conv10)  # feature_size
        batch11 = self.bc11(conv11)  # feature_size
        batch12 = self.bc12(conv12)  # feature_size
        batch13 = self.bc13(conv13)  # feature_size
        batch14 = self.bc14(conv14)  # feature_size

        feature = torch.cat(
            [batch1, batch2, batch3, batch4, batch5, batch6, batch7,
             batch8,batch9,batch10,batch11,batch12,batch13,
             batch14],
            axis=2)  # f_size = (2*combination * combination_rev+feature_size* 12)
                    # N*1*f_size*3 = N*1*f_size*3
        # GRU层
        feature = feature.squeeze(1)  # N*1*f_size*3 -> N*f_size*3
        feature = feature.permute(0, 2, 1)  # N*f_size*3 -> N*3*f_size
        feature = self.GRU(feature)  # N*3*f_size -> N*30

        return feature


    def ts_cov4d(self, Matrix, combination, combination_rev):
        new_H = len(combination)
        index_list = self.index_list
        list = []
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]

            data = Matrix[:, :, combination,
                          start_index:end_index]  # N*1*new_H*2*d
            data2 = Matrix[:, :, combination_rev,
                           start_index:end_index]  # N*1*new_H*2*d

            mean1 = data.mean(axis=4, keepdims=True)  # N*1*new_H*2*1, 在时序上求均值
            mean2 = data2.mean(axis=4, keepdims=True)  # N*1*new_H*2*1, 在时序上求均值
            spread1 = data - mean1  # N*1*new_H*2*d, 在时序上求偏差
            spread2 = data2 - mean2  # N*1*new_H*2*d, 在时序上求偏差
            cov = ((spread1 * spread2).sum(axis=4, keepdims=True) /
                   (data.shape[4] - 1)).mean(axis=3,
                                             keepdims=True)  # N*1*new_H*1*1
            list.append(cov)
        cov = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) - 1)  # N*1*new_H*len(index_list)-1
        return torch.from_numpy(cov)

    def ts_corr4d(self, Matrix, combination, combination_rev):
        new_H = len(combination)
        index_list = self.index_list
        list = []
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]

            data = Matrix[:, :, combination,
                          start_index:end_index]  # N*1*new_H*2*d

            data2 = Matrix[:, :, combination_rev,
                           start_index:end_index]  # N*1*new_H*2*d

            std1 = data.std(axis=4, keepdims=True)  # N*1*new_H*2*1, 在时序上求标准差
            std2 = data2.std(axis=4, keepdims=True)  # N*1*new_H*2*1, 在时序上求标准差

            std = (std1 * std2).mean(axis=3, keepdims=True)  # N*1*new_H*1*1

            list.append(std)
        std = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) -
            1) + 0.01  # N*1*new_H*len(index_list)-1 # 加上0.01, 防止除0
        # N*1*new_H*len(index_list)-1
        cov = self.ts_cov4d(Matrix, combination, combination_rev)
        corr = cov / std  # N*1*new_H*len(index_list)-1
        return corr

    def ts_stddev4d(self, Matrix):
        new_H = Matrix.shape[2]
        index_list = self.index_list
        list = []  # 存放长度为len(index_list)-1的标准差
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]

            data = Matrix[:, :, :, start_index:end_index]  # N*1*H*d

            std = data.std(axis=3, keepdims=True)  # N*1*H*1

            list.append(std)

        std4d = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) - 1)

        return torch.from_numpy(std4d)

    def ts_zscore4d(self, Matrix):
        new_H = Matrix.shape[2]
        index_list = self.index_list
        list = []
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]
            data = Matrix[:, :, :, start_index:end_index]  # N*1*H*d
            mean = data.mean(axis=3, keepdims=True)  # N*1*H*1
            std = data.std(axis=3, keepdims=True) + \
                0.01  # N*1*H*1, 加上0.01, 防止除以0
            list.append(mean / std)
        zscore = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) - 1)  # N*1*new_H*len(index_list)-1
        return torch.from_numpy(zscore)

    def ts_return4d(self, Matrix):
        new_H = Matrix.shape[2]
        index_list = self.index_list
        list = []
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]
            data = Matrix[:, :, :, start_index:end_index]  # N*1*H*d
            # N*1*H*1, 在分母加上0.01, 防止除以0
            return_ = data[:, :, :, -1] / (data[:, :, :, 0] + 0.01) - 1
            list.append(return_)
        ts_return = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) - 1)  # N*1*new_H*len(index_list)-1
        return torch.from_numpy(ts_return)

    def ts_decaylinear4d(self, Matrix):
        new_H = Matrix.shape[2]
        index_list = self.index_list
        list = []
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]
            range_ = end_index - start_index
            weight = np.arange(1, range_ + 1)
            weight = weight / weight.sum()  # 权重向量
            data = Matrix[:, :, :, start_index:end_index]  # N*1*H*d
            wd = (data * weight).sum(axis=3, keepdims=True)  # N*1*H*1
            list.append(wd)
        ts_decaylinear = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) - 1)  # N*1*new_H*len(index_list)-1
        return torch.from_numpy(ts_decaylinear)

    def ts_mean4d(self, Matrix):
        new_H = Matrix.shape[2]
        index_list = self.index_list
        list = []  # 存放长度为len(index_list)-1的平均值
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]
            data = Matrix[:, :, :, start_index:end_index]  # N*1*H*d
            mean_ = data.mean(axis=3, keepdims=True)  # N*1*H*1
            list.append(mean_)
        ts_mean = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) - 1)  # N*1*new_H*len(index_list)-1
        return torch.from_numpy(ts_mean)
    
    def ts_median4d(self, Matrix):
        new_H = Matrix.shape[2]
        index_list = self.index_list
        list = []  # 存放长度为len(index_list)-1的平均值
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]
            data = Matrix[:, :, :, start_index:end_index]  # N*1*H*d
            median_ = np.median(data,axis=3,keepdims=True)  # N*1*H*1
            list.append(median_)
        ts_median = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) - 1)  # N*1*new_H*len(index_list)-1
        return torch.from_numpy(ts_median)
    
    def ts_var4d(self, Matrix):
        new_H = Matrix.shape[2]
        index_list = self.index_list
        list = []
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]
            data = Matrix[:, :, :, start_index:end_index]  # N*1*H*d
            mean_ = data.mean(axis=3, keepdims=True)  # N*1*H*1
            spread = data - mean_  # N*1*new_H*d, 在时序上求偏差
            var_ = ((spread * spread).sum(axis=3, keepdims=True) /
                   (data.shape[3] - 1)).mean(axis=3,
                                             keepdims=True)
            list.append(var_)
        ts_var = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) - 1)  # N*1*new_H*len(index_list)-1
        return torch.from_numpy(ts_var)


    def ts_min4d(self, Matrix):
        new_H = Matrix.shape[2]
        index_list = self.index_list
        list = []
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]
            data = Matrix[:, :, :, start_index:end_index]  # N*1*H*d
            min_ = data.min(axis=3, keepdims=True)
            list.append(min_)
        ts_min = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) - 1)  # N*1*new_H*len(index_list)-1
        return torch.from_numpy(ts_min)
    
    def ts_max4d(self, Matrix):
        new_H = Matrix.shape[2]
        index_list = self.index_list
        list = []
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]
            data = Matrix[:, :, :, start_index:end_index]  # N*1*H*d
            max_ = data.max(axis=3, keepdims=True)
            list.append(max_)
        ts_max = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) - 1)  # N*1*new_H*len(index_list)-1
        return torch.from_numpy(ts_max)
    
    def ts_sum4d(self, Matrix):
        new_H = Matrix.shape[2]
        index_list = self.index_list
        list = []
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]
            data = Matrix[:, :, :, start_index:end_index]  # N*1*H*d
            sum_ = data.sum(axis=3, keepdims=True)
            list.append(sum_)
        ts_sum = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) - 1)  # N*1*new_H*len(index_list)-1
        return torch.from_numpy(ts_sum)

    def ts_skew4d(self, Matrix):
        new_H = Matrix.shape[2]
        index_list = self.index_list
        list = []
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]
            data = Matrix[:, :, :, start_index:end_index]  # N*1*H*d
            # 在时序上求均值、偏差、标准差
            mean = np.mean(data, axis=3, keepdims=True)
            spread = data - mean
            std_dev = np.std(data, axis=3, keepdims=True)
            skew_ = np.mean(np.power(spread / std_dev, 3), axis=3, keepdims=True)
            list.append(skew_)
        ts_skew = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) - 1)  # N*1*new_H*len(index_list)-1
        return torch.from_numpy(ts_skew)
    
    def ts_kurtosis4d(self, Matrix):
        new_H = Matrix.shape[2]
        index_list = self.index_list
        list = []
        for i in range(len(index_list) - 1):
            start_index = index_list[i]
            end_index = index_list[i + 1]
            data = Matrix[:, :, :, start_index:end_index]  # N*1*H*d
            # 在时序上求均值、偏差、标准差
            mean = np.mean(data, axis=3, keepdims=True)
            spread = data - mean
            std_dev = np.std(data, axis=3, keepdims=True)
            kurtosis_ = np.mean(np.power(spread / std_dev, 4), axis=3, keepdims=True) - 3
            list.append(kurtosis_)
        ts_kurtosis = np.squeeze(np.array(list)).transpose(1, 2, 0).reshape(
            -1, 1, new_H,
            len(index_list) - 1)  # N*1*new_H*len(index_list)-1
        return torch.from_numpy(ts_kurtosis)
    

class AlphaNet(nn.Module):

    def __init__(self, sample, features_size, window,
                 long_stride, short_stride,
                 hidden_size):
        
        super(AlphaNet, self).__init__()

        self._init_external(sample=sample, features_size=features_size,
                            window=window, long_stride=long_stride,
                            short_stride=short_stride)

        self.Inception_1 = Inception(self.combination, 
                                     self.combination_rev,
                                     features_size,
                                     hidden_size,
                                     self.index_list_1)

        self.Inception_2 = Inception(self.combination, 
                                     self.combination_rev,
                                     features_size,
                                     hidden_size,
                                     self.index_list_2)
        # 输出层
        self.fc = nn.Linear(hidden_size * 2, 1)

        # 初始化权重
        self._init_weights()

    def _init_external(self, sample, features_size, window, long_stride, short_stride):
        self.combination, self.combination_rev = sample_combination(
            N=sample, M=features_size)

        self.index_list_1 = get_index_list(np.zeros((1, 1, features_size, window)), long_stride)
        self.index_list_2 = get_index_list(np.zeros((1, 1, features_size, window)), short_stride)

    def _init_weights(self):
        # 使用xavier的均匀分布对weights进行初始化
        nn.init.xavier_uniform_(self.fc.weight)
        # 使用正态分布对bias进行初始化
        nn.init.normal_(self.fc.bias, std=1e-6)

    def forward(self, data):
        data_1 = self.Inception_1(data)  # N
        data_2 = self.Inception_2(data)  # N
        pool_cat = torch.cat([data_1, data_2], axis=1)  # N*60
        # 输出层
        data = self.fc(pool_cat)
        data = data.to(torch.float)
        return data
    

def create_optimizer(alphanet, optim_name, **kwargs):
    ##  L2 正则
    accelerator = Accelerator()
    weight_list, bias_list = [], []
    for name, p in alphanet.named_parameters():
        if 'bias' in name:
            bias_list += [p]
        else:
            weight_list += [p]
    optim = importlib.import_module('torch.optim')
    optimizer = getattr(optim,optim_name)([{
        'params': weight_list,
        'weight_decay': 1e-5
        }, {'params': bias_list,
            'weight_decay': 0
            }],**kwargs)
    return accelerator.prepare(alphanet, optimizer)
