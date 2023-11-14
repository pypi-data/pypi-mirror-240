from jcopdl.snippet._utils import _copy_snippet


def standard_loop_acc():
    return _copy_snippet("""
        from tqdm.auto import tqdm
        from jcopdl.metrics import MiniBatchCost, MiniBatchAccuracy
        from jcopdl.visualization import visualize_prediction_batch


        def train_loop_fn(mode, dataloader, model, criterion, optimizer, callback, device):
            if mode == "train":
                model.train()
            elif mode == "test":
                model.eval()
            
            cost = MiniBatchCost()
            score = MiniBatchAccuracy()
            for feature, target in tqdm(dataloader, desc=mode.title(), leave=False):
                feature, target = feature.to(device), target.to(device)
                output = model(feature)
                loss = criterion(output, target)
                
                if mode == "train":
                    loss.backward()
                    optimizer.step()
                    optimizer.zero_grad()

                cost.add_batch(loss, feature.size(0))
                score.add_batch(output, target)
            callback.log(f"{mode}_cost", cost.compute())
            callback.log(f"{mode}_score", score.compute())
            
            if mode == "test":
                preds = output.argmax(1)
                classes = dataloader.dataset.classes
                image = visualize_prediction_batch(feature, target, preds, classes)
                callback.log_image("test_predict", image)
    """)

def standard_loop_f1():
    return _copy_snippet("""
        from tqdm.auto import tqdm
        from jcopdl.metrics import MiniBatchCost, MiniBatchBinaryF1


        def train_loop_fn(mode, dataloader, model, criterion, optimizer, callback, device):
            if mode == "train":
                model.train()
            elif mode == "test":
                model.eval()
            
            cost = MiniBatchCost()
            score = MiniBatchBinaryF1()
            for feature, target in tqdm(dataloader, desc=mode.title(), leave=False):
                feature, target = feature.to(device), target.to(device)
                output = model(feature)
                loss = criterion(output, target)
                
                if mode == "train":
                    loss.backward()
                    optimizer.step()
                    optimizer.zero_grad()

                cost.add_batch(loss, feature.size(0))
                score.add_batch(output, target)
            callback.log(f"{mode}_cost", cost.compute())
            callback.log(f"{mode}_score", score.compute(pos_label=1))
    """)

def rnn_loop():
    return _copy_snippet("""
        from tqdm.auto import tqdm
        from torch.nn.utils import clip_grad_norm_
        from jcopdl.metrics import MiniBatchCost, MiniBatchBinaryF1


        def train_loop_fn(mode, dataloader, model, criterion, optimizer, callback, device):
            if mode == "train":
                model.train()
            elif mode == "test":
                model.eval()
            
            cost = MiniBatchCost()
            score = MiniBatchBinaryF1()
            for feature, target in tqdm(dataloader, desc=mode.title(), leave=False):
                feature, target = feature.to(device), target.to(device)
                output, hidden = model(feature, None)
                loss = criterion(output, target)
                
                if mode == "train":
                    loss.backward()
                    clip_grad_norm_(model.parameters(), 2)
                    optimizer.step()
                    optimizer.zero_grad()

                cost.add_batch(loss, feature.size(0))
                score.add_batch(output, target)
            callback.log(f"{mode}_cost", cost.compute())
            callback.log(f"{mode}_score", score.compute(pos_label=1))
    """)

def rnn_tbptt_loop():
    return _copy_snippet("""
        from tqdm.auto import tqdm
        from torch.nn.utils import clip_grad_norm_
        from jcopdl.metrics import MiniBatchCost, MiniBatchBinaryF1


        def train_loop_fn(mode, dataloader, model, criterion, optimizer, callback, device):
            if mode == "train":
                model.train()
            elif mode == "test":
                model.eval()
            
            cost = MiniBatchCost()
            score = MiniBatchBinaryF1()
            for (prior, feature), target in tqdm(dataloader, desc=mode.title(), leave=False):
                prior, feature, target = prior.to(device), feature.to(device), target.to(device)
                with torch.no_grad():
                    output, hidden = model(prior, None)
                output, hidden = model(feature, hidden)
                loss = criterion(output, target)
                
                if mode == "train":
                    loss.backward()
                    clip_grad_norm_(model.parameters(), 2)
                    optimizer.step()
                    optimizer.zero_grad()

                cost.add_batch(loss, feature.size(0))
                score.add_batch(output, target)
            callback.log(f"{mode}_cost", cost.compute())
            callback.log(f"{mode}_score", score.compute(pos_label=1))
    """)
