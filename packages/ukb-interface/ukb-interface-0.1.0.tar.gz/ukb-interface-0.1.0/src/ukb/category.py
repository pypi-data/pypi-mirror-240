from enum import Enum

def available_category(

):
    """ 
    Available categories for UK Biobank dataset.

    Return
    ------
    categ_list: list
        list of all categories available.
    """
    return [categ.val for categ in Category]



class Category(Enum):

    GMV = 'gmv'
    SCV = 'scv'