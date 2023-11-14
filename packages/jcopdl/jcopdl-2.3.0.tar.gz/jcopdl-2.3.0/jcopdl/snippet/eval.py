from jcopdl.snippet._utils import _copy_snippet


def visualize_classification():
    return _copy_snippet("""
        from jcopdl.eval import evaluate_prediction

        configs = torch.load("______/configs.pth")

        train_set = datasets.ImageFolder("______", transform=configs["transform"])
        trainloader = DataLoader(train_set, batch_size=configs["batch_size"], shuffle=True)

        test_set = datasets.ImageFolder("______", transform=configs["transform"])
        testloader = DataLoader(test_set, batch_size=configs["batch_size"], shuffle=True)

        img_train = evaluate_prediction(trainloader, model, device)
        img_test = evaluate_prediction(testloader, model, device)
    """)

def evaluate_accuracy():
    return _copy_snippet("""
        from jcopdl.eval import evaluate_accuracy
        
        configs = torch.load("______/configs.pth")

        train_set = datasets.ImageFolder("______", transform=configs["transform"])
        trainloader = DataLoader(train_set, batch_size=configs["batch_size"], shuffle=False)

        test_set = datasets.ImageFolder("______", transform=configs["transform"])
        testloader = DataLoader(test_set, batch_size=configs["batch_size"], shuffle=False)
                         
        acc_train = evaluate_accuracy(trainloader, model, device)
        acc_test = evaluate_accuracy(testloader, model, device)
    """)

def evaluate_confusion_matrix():
    return _copy_snippet("""
        from jcopdl.eval import evaluate_confusion_matrix
        from jcopdl.visualization import plot_confusion_matrix

        configs = torch.load("______/configs.pth")

        train_set = datasets.ImageFolder("______", transform=configs["transform"])
        trainloader = DataLoader(train_set, batch_size=configs["batch_size"], shuffle=False)

        test_set = datasets.ImageFolder("______", transform=configs["transform"])
        testloader = DataLoader(test_set, batch_size=configs["batch_size"], shuffle=False)

        cm_train = evaluate_confusion_matrix(trainloader, model, device)
        cm_test = evaluate_confusion_matrix(testloader, model, device)

        fig = plot_confusion_matrix([cm_train, cm_test], configs["classes"])
    """)

def evaluate_misclassified():
    return _copy_snippet("""
        from jcopdl.eval import evaluate_misclassified

        configs = torch.load("______/configs.pth")

        test_set = datasets.ImageFolder("______", transform=configs["transform"])
        testloader = DataLoader(test_set, batch_size=configs["batch_size"], shuffle=False)

        images = evaluate_misclassified(testloader, model, device)
    """)