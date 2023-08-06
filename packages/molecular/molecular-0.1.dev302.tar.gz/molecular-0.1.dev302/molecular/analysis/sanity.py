
from molecular.analysis import contacts
from molecular.simulations import generate_images

import numpy as np


def has_cross_interactions(a, cutoff=4.5):
    # Move `a` to the unit cell
    am = a.to_origin(a, inplace=False)

    # Get a copy of `a`
    b = a.copy()

    # Go through all images and find cross interactions
    is_crossed = np.zeros(am.n_structures, dtype='bool')
    for image in generate_images():
        if image == (0, 0, 0):  # skip the origin
            continue
        bm = b.to_image(*image, inplace=False)
        is_crossed = is_crossed | np.max(contacts(a, b, cutoff=cutoff, include_images=False), axis=(1, 2))

    # Return
    return is_crossed
    

