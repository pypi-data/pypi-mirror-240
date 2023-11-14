from jcopdl.snippet._utils import _copy_snippet


def training_preparation():
    return _copy_snippet("""
        configs["optimizer"] = {"lr": 0.001}                         

        model = _______(**configs["model"]).to(device)
        criterion = _______
        optimizer = optim.AdamW(model.parameters(), **configs["optimizer"])
        callback = Callback(model, configs, optimizer, outdir="_______")
                         
        # Plot Loss
        callback.add_plot(["train_cost", "test_cost"], scale="semilogy")
        # Plot Score
        callback.add_plot(["train_score", "test_score"], scale="linear_positive")
        # Plot Image
        callback.add_image("test_predict")
    """)


def training_preparation_with_onecyclelr():
    return _copy_snippet("""
        configs["scheduler"] = {
            "pct_start": 0.2,
            "max_lr": 1e-3,
            "div_factor": 10,
            "final_div_factor": 1000,
            "steps_per_epoch": len(train_set) // bs + 1,
            "epochs": 100
        }                      

        model = _______(**configs["model"]).to(device)
        criterion = _______
        optimizer = optim.AdamW(model.parameters())
        scheduler = optim.lr_scheduler.OneCycleLR(optimizer, **configs["scheduler"])
        callback = Callback(model, configs, optimizer, scheduler, max_epoch=100, outdir="_______")
                         
        # Plot Loss
        callback.add_plot(["train_cost", "test_cost"], scale="semilogy")
        # Plot Score
        callback.add_plot(["train_score", "test_score"], scale="linear_positive")
        # Plot Image
        callback.add_image("test_predict")
    """)


def minimize_cost():
    return _copy_snippet("""
        while True:
            train_loop_fn("train", trainloader, model, criterion, optimizer, callback, device)
            with torch.no_grad():
                train_loop_fn("test", testloader, model, criterion, optimizer, callback, device)
            
            if callback.early_stopping("minimize", "test_cost"):
                model = callback.load_best_state()
                break
    """)


def maximize_score():
    return _copy_snippet("""
        while True:
            train_loop_fn("train", trainloader, model, criterion, optimizer, callback, device)
            with torch.no_grad():
                train_loop_fn("test", testloader, model, criterion, optimizer, callback, device)
            
            if callback.early_stopping("maximize", "test_score"):
                model = callback.load_best_state()                         
                break
    """)


def transfer_learning_with_unfreezing():
    return _copy_snippet("""
        phase = 1
        while True:
            train_loop_fn("train", trainloader, model, criterion, optimizer, callback, device)
            with torch.no_grad():
                train_loop_fn("test", testloader, model, criterion, optimizer, callback, device)

            if callback.early_stopping("maximize", "test_score"):
                phase += 1
                match phase:
                    case 2: # Phase 2: Fine-tuning
                        model.unfreeze()
                        callback.early_stop_patience = _____
                        configs["optimizer"] = {"lr": _____}
                        optimizer = optim.AdamW(model.parameters(), **configs["optimizer"])  
                    case 3: # Phase 3: 2nd Fine-tuning
                        model = callback.load_best_state()
                        callback.early_stop_patience = _____
                        configs["optimizer"] = {"lr": _____}
                        optimizer = optim.AdamW(model.parameters(), **configs["optimizer"])
                    case 4:
                        model = callback.load_best_state()
                        break
    """)


def multiphase_training():
    return _copy_snippet("""
        phase = 1
        while True:
            train_loop_fn("train", trainloader, model, criterion, optimizer, callback, device)
            with torch.no_grad():
                train_loop_fn("test", testloader, model, criterion, optimizer, callback, device)

            if callback.early_stopping("maximize", "test_score"):
                phase += 1
                match phase:
                    case 2: # Phase 2: Fine-tuning
                        callback.early_stop_patience = 25
                        configs["optimizer"] = {"lr": 1e-4}
                        optimizer = optim.AdamW(model.parameters(), **configs["optimizer"])  
                    case 3: # Phase 3: 2nd Fine-tuning
                        model = callback.load_best_state()
                        callback.early_stop_patience = 20
                        configs["optimizer"] = {"lr": 1e-5}
                        optimizer = optim.AdamW(model.parameters(), **configs["optimizer"])
                    case 4:
                        model = callback.load_best_state()
                        break                
    """)
