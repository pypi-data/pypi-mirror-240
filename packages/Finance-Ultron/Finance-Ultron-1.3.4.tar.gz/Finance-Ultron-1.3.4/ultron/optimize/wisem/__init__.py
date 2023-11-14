import numpy as np
import torch
from ultron.kdutils.progress import Progress
from torchsummary import summary
from ultron.optimize.wisem.alphanet.gen1 import AlphaNet as AlphaNetGen1
from ultron.optimize.wisem.alphanet.gen1 import create_optimizer,create_data
from ultron.optimize.wisem.loss import MSELoss,CCCLoss


def to_device(item):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    return item.to(device=device)




def train(model, loss_fn, optimizer, epoch_num, train_loader, val_loader):
    train_loss_list = []
    test_loss_list = []
    best_test_epoch, best_test_loss = 0, np.inf
    with Progress(epoch_num, 0, label='start model') as pg:
        for epoch in range(1, epoch_num + 1):
            pg.show(epoch + 1)
            train_loss, test_loss = 0, 0
            model.train()
            train_batch_num = 0
            with Progress(len(train_loader), 0, label="epoch{0}:train model".format(epoch)) as pg:
                train_batch_num = 0
                for data, label in train_loader:
                    train_batch_num += 1
                    data = to_device(data)
                    label = to_device(label)

                    out_put = model(data)
                    loss = loss_fn(out_put, label.to('cuda'))


                    train_loss += loss.item()
                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()

                    pg.show(train_batch_num + 1)
            model.eval()

            test_batch_num = 0
            with Progress(len(val_loader), 0, label="epoch{0}:test model".format(epoch)) as pg:
                with torch.no_grad():
                    for data, label in val_loader:
                        test_batch_num += 1
                        data = to_device(data)
                        label = to_device(label)

                        out_put = model(data)
                        loss = loss_fn(out_put, label.to('cuda'))
                        test_loss += loss.item()

                        pg.show(test_batch_num + 1)

            train_loss_list.append(train_loss/train_batch_num)
            test_loss_list.append(test_loss/test_batch_num)

    return train_loss_list, test_loss_list


__all__ = ['summary','train',
            'AlphaNetGen1','create_optimizer','create_data',
           'MSELoss','CCCLoss']