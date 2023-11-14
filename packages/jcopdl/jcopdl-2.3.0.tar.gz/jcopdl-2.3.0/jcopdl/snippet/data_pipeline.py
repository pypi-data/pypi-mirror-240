from jcopdl.snippet._utils import _copy_snippet


def multiclass_image_classification():
    return _copy_snippet("""
        from torchvision import datasets, transforms
        from torch.utils.data import DataLoader

        bs = "______"

        train_transform = transforms.Compose([
            "____________",
            transforms.ToTensor()
        ])

        test_transform = transforms.Compose([
            "____________",
            transforms.ToTensor()
        ])

        train_set = datasets.ImageFolder("________", transform=train_transform)
        trainloader = DataLoader(train_set, batch_size=bs, shuffle=True)

        test_set = datasets.ImageFolder("________", transform=test_transform)
        testloader = DataLoader(test_set, batch_size=bs, shuffle="____")


        configs = {
            "batch_size": bs,
            'classes': train_set.classes,
            'transform': test_transform
        }
    """)


def char_rnn_text_classification():
    return _copy_snippet("""
        from jcopdl import transforms
        from jcopdl.utils.dataloader import CharRNNDataset, CharRNNDataloader

        train_set = CharRNNDataset("data / train.csv", text_col="_______", label_col="_______", max_len=_______)
        test_set = CharRNNDataset("data / test.csv", text_col="_______", label_col="_______", chars=train_set.chars, classes=train_set.classes, pad=train_set.pad, max_len=_______)

        bs = "______"
        transform = transforms.Compose([
            transforms.PadSequence(),
            transforms.OneHotEncode(train_set.n_chars),
            transforms.TruncateSequence(200)
        ])

        trainloader = CharRNNDataloader(train_set, batch_size=bs, batch_transform=transform, drop_last=True)
        testloader = CharRNNDataloader(test_set, batch_size=bs, batch_transform=transform, drop_last=True)


        configs = {
            "batch_size": bs,
            "chars": train_set.chars,
            "pad": train_set.pad,
            "classes": train_set.classes,
            "transform": transform
        }
    """)    