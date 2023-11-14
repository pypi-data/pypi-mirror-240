from jcopdl.snippet._utils import _copy_snippet


def visualize_batch():
    return _copy_snippet("""
        from jcopdl.visualization import visualize_image_batch

        feature, target = next(iter(trainloader))
        visualize_image_batch(feature, n_col=8)
    """)    
