import torch.nn as nn

class CCCLoss(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.mse = nn.MSELoss()

    def forward(self, y_predict, y_true):
        sigma = ((y_predict - y_predict.mean())*(y_true - y_true.mean())).mean()
        return -2*sigma/(self.mse(y_predict, y_true) + 2*sigma) # CCC越大越好，取相反数