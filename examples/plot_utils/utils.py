import os
import numpy as np


def store_plot_data(data, path, file_name):
    """
    Store data to .npy file

    Args:
        data:       data to store
        path:       the file will be stored at <path>/plot_data
        file_name:  name of the file to store ( no extension )
    """
    
    try:
        os.makedirs(os.path.join(path, 'plot_data'))
    except:
        pass

    np.save(os.path.join(path, 'plot_data', file_name), data)
