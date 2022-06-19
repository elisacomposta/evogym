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


def get_stored_structure(structure_path):
    """
    Returns a structure previously stored at structure_path
    """
    structure_data = np.load(structure_path)
    structure = []
    for key, value in structure_data.items():
        structure.append(value)
    structure = tuple(structure)
    return structure
