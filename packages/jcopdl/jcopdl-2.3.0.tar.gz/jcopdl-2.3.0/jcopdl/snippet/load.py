from jcopdl.snippet._utils import _copy_snippet


def load_from_checkpoint():
    return _copy_snippet("""
        from jcopdl.io import load_from_checkpoint

        checkpoint = load_from_checkpoint("_______/checkpoint/_________.pth")
        model, optimizer, scheduler, callback = checkpoint.model, checkpoint.optimizer, checkpoint.scheduler, checkpoint
        criterion = _______
    """)


def load_best_model():
    return _copy_snippet("""
        import torch
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        model = torch.load("______/model_best.pth", map_location="cpu").to(device)
    """)


def load_config():
    return _copy_snippet("""
        import torch

        configs = torch.load("______/configs.pth")
    """)
