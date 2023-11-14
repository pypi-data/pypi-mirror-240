from jcopdl.snippet._utils import _copy_snippet


def import_common_packages():
    return _copy_snippet("""
        %load_ext autoreload
        %autoreload 2                         

        import torch
        from torch import nn, optim
        from jcopdl.callback import Callback

        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        device
    """)