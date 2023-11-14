from jcopdl.snippet._utils import _copy_snippet


def ann_regression():
    return _copy_snippet("""
        from torch import nn
        from jcopdl.layers import linear_block

        class ANN(nn.Module):
            def __init__(self, input_size, n1, n2, output_size, dropout):
                super().__init__()
                self.fc = nn.Sequential(
                    linear_block(input_size, n1, dropout=dropout),
                    linear_block(n1, n2, dropout=dropout),
                    linear_block(n2, output_size, activation="identity")
                ),
            
            def forward(self, x):
                return self.fc(x)
            

        configs["model"] = {
            "input_size": train_set.n_features,
            "n1": 128,
            "n2": 64,
            "output_size": 1,
            "dropout": 0
        }
    """)


def ann_multiclass_classification():
    return _copy_snippet("""
        from torch import nn
        from jcopdl.layers import linear_block

        class ANN(nn.Module):
            def __init__(self, input_size, n1, n2, output_size, dropout):
                super().__init__()
                self.fc = nn.Sequential(
                    linear_block(input_size, n1, dropout=dropout),
                    linear_block(n1, n2, dropout=dropout),
                    linear_block(n2, output_size, activation="lsoftmax")
                ),
            
            def forward(self, x):
                return self.fc(x)
            

        configs["model"] = {
            "input_size": train_set.n_features,
            "n1": 128,
            "n2": 64,
            "output_size": 1,
            "dropout": 0
        }
    """)

def cnn_multiclass_classification():
    return _copy_snippet("""
        from torch import nn
        from jcopdl.layers import linear_block, conv_block

        class CNN(nn.Module):
            def __init__(self, output_size, fc_dropout):
                super().__init__()
                self.conv = nn.Sequential(
                    conv_block("___", "___"),
                    conv_block("___", "___"),
                    nn.Flatten()
                )
                
                self.fc = nn.Sequential(
                    linear_block("_____", "_____", dropout=fc_dropout),
                    linear_block("_____", output_size, activation="lsoftmax")
                )
                
            def forward(self, x):
                return self.fc(self.conv(x))
            

        configs["model"] = {
            "output_size": len(train_set.classes),
            "fc_dropout": 0
        }
    """)

def rnn_many_to_many_regression():
    return _copy_snippet("""
        from torch import nn
        from jcopdl.layers import linear_block

        class ManytoManyRNN(nn.Module):
            def __init__(self, input_size, output_size, hidden_size, num_layers, dropout):
                super().__init__()
                self.rnn = nn.RNN(input_size, hidden_size, num_layers, dropout=dropout, batch_first=True)
                self.fc = linear_block(hidden_size, output_size, activation="identity")
                
            def forward(self, x, hidden):        
                x, hidden = self.rnn(x, hidden)
                x = self.fc(x)
                return x, hidden


        configs["model"] = {
            "input_size": ________,
            "output_size": ________,
            "hidden_size": 64,
            "num_layers": 2,
            "dropout": 0
        }    
    """)


def rnn_many_to_one_classification():
    return _copy_snippet("""
        from torch import nn
        from jcopdl.layers import linear_block

        class ManyToOneRNN(nn.Module):
            def __init__(self, input_size, output_size, hidden_size, num_layers, dropout):
                super().__init__()
                self.rnn = nn.RNN(input_size, hidden_size, num_layers, dropout=dropout, batch_first=True)
                self.fc = linear_block(num_layers*hidden_size, output_size, activation="lsoftmax")
                
            def forward(self, x, hidden):        
                x, hidden = self.rnn(x, hidden)
                n_layers, n_batch, n_hidden = hidden.shape
                last_state = hidden.permute(1, 0, 2).reshape(-1, n_layers*n_hidden) # LBH -> BLH -> BF
                x = self.fc(last_state)
                return x, hidden


        configs["model"] = {
            "input_size": ________,
            "output_size": ________,
            "hidden_size": 64,
            "num_layers": 2,
            "dropout": 0
        }
    """)


def lstm_many_to_many_regression():
    return _copy_snippet("""
        from torch import nn
        from jcopdl.layers import linear_block

        class ManytoManyLSTM(nn.Module):
            def __init__(self, input_size, output_size, hidden_size, num_layers, dropout):
                super().__init__()
                self.rnn = nn.LSTM(input_size, hidden_size, num_layers, dropout=dropout, batch_first=True)
                self.fc = linear_block(hidden_size, output_size, activation="identity")
                
            def forward(self, x, hidden):        
                x, hidden = self.rnn(x, hidden)
                x = self.fc(x)
                return x, hidden


        configs["model"] = {
            "input_size": ________,
            "output_size": ________,
            "hidden_size": 64,
            "num_layers": 2,
            "dropout": 0
        }
    """)


def lstm_many_to_one_classification():
    return _copy_snippet("""
        from torch import nn
        from jcopdl.layers import linear_block

        class ManyToOneLSTM(nn.Module):
            def __init__(self, input_size, output_size, hidden_size, num_layers, dropout):
                super().__init__()
                self.rnn = nn.LSTM(input_size, hidden_size, num_layers, dropout=dropout, batch_first=True)
                self.fc = linear_block(num_layers*2*hidden_size, output_size, activation="lsoftmax")
                
            def forward(self, x, hidden):        
                x, (h, c) = self.rnn(x, hidden)
                state = torch.cat([h, c], dim=2)
                n_layers, n_batch, n_2hidden = state.shape
                last_state = state.permute(1, 0, 2).reshape(-1, n_layers*n_2hidden) # LBH -> BLH -> BF
                x = self.fc(last_state)
                return x, (h, c)


        configs["model"] = {
            "input_size": ________,
            "output_size": ________,
            "hidden_size": 64,
            "num_layers": 2,
            "dropout": 0
        }
    """)


def gru_many_to_many_regression():
    return _copy_snippet("""
        from torch import nn
        from jcopdl.layers import linear_block

        class ManytoManyGRU(nn.Module):
            def __init__(self, input_size, output_size, hidden_size, num_layers, dropout):
                super().__init__()
                self.rnn = nn.GRU(input_size, hidden_size, num_layers, dropout=dropout, batch_first=True)
                self.fc = linear_block(hidden_size, output_size, activation="identity")
                
            def forward(self, x, hidden):        
                x, hidden = self.rnn(x, hidden)
                x = self.fc(x)
                return x, hidden


        configs["model"] = {
            "input_size": ________,
            "output_size": ________,
            "hidden_size": 64,
            "num_layers": 2,
            "dropout": 0
        }
    """)


def gru_many_to_one_classification():
    return _copy_snippet("""
        from torch import nn
        from jcopdl.layers import linear_block

        class ManyToOneGRU(nn.Module):
            def __init__(self, input_size, output_size, hidden_size, num_layers, dropout):
                super().__init__()
                self.rnn = nn.GRU(input_size, hidden_size, num_layers, dropout=dropout, batch_first=True)
                self.fc = linear_block(num_layers*hidden_size, output_size, activation="lsoftmax")
                
            def forward(self, x, hidden):        
                x, hidden = self.rnn(x, hidden)
                n_layers, n_batch, n_hidden = hidden.shape
                last_state = hidden.permute(1, 0, 2).reshape(-1, n_layers*n_hidden) # LBH -> BLH -> BF
                x = self.fc(last_state)
                return x, hidden


        configs["model"] = {
            "input_size": ________,
            "output_size": ________,
            "hidden_size": 64,
            "num_layers": 2,
            "dropout": 0
        }
    """)


def transfer_learning_template():
    return _copy_snippet("""
        class TLModel(nn.Module):
            def __init__(self):
                super().__init__()
                self.model = _______
                self.freeze()
                
            def freeze(self):
                for param in self.model.parameters():
                    param.requires_grad = False
                    
            def unfreeze(self):
                for param in self.model.parameters():
                    param.requires_grad = True
                    
            def forward(self, x):
                return self.model(x)
    """)