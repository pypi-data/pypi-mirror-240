import copy
import collections
from typing import Optional, Union, Dict, List, Sequence, Callable

def update_nested_dict(d: Dict, u: Dict) -> Dict:
    """
    Recursively updates nested dictionaries.

    Parameters
    ----------
    d : Dict
        The dictionary to be updated.
    u : Dict
        The dictionary containing updates.

    Returns
    -------
    Dict
        The updated dictionary.

    Notes
    -----
    If a key exists in `u` but not in `d`, the key-value pair from `u` is added to `d`.
    """
    for k, v in u.items():
        if isinstance(d.get(k, None), collections.abc.Mapping) and isinstance(v, collections.abc.Mapping):
            d[k] = update_nested_dict(d.get(k, {}), v)
        else:
            d[k] = v
    return d

def combine_dict(d: Optional[Dict] = None, u: Optional[Dict] = None) -> Dict:
    """
    Creates a deep copy of two dictionaries and combines their contents.

    Parameters
    ----------
    d : Dict, optional
        The primary dictionary. Default is None.
    u : Dict, optional
        The dictionary containing updates. If `None`, the function returns a 
        deep copy of `d`. Default is None.

    Returns
    -------
    Dict
        The combined dictionary.
    """
    d_copy = copy.deepcopy(d) if d is not None else {}
    if u is None:
        return d_copy

    u_copy = copy.deepcopy(u)
    return update_nested_dict(d_copy, u_copy)

def make_multiline_text(text:str, max_line_length:int, break_word:bool=True):
    if break_word:
        n = max_line_length
        return '\n'.join(text[i:i+n] for i in range(0, len(text), n))
    #accumulated line length
    acc_length = 0
    words = text.split(" ")
    formatted_text = ""
    for word in words:
        #if ACC_length + len(word) and a space is <= max_line_length 
        if acc_length + (len(word) + 1) <= max_line_length:
            #append the word and a space
            formatted_text = formatted_text + word + " "
            #length = length + length of word + length of space
            acc_length = acc_length + len(word) + 1
        else:
            #append a line break, then the word and a space
            formatted_text = formatted_text + "\n" + word + " "
            #reset counter of length to the length of a word and a space
            acc_length = len(word) + 1
    return formatted_text.lstrip("\n")

def add_newline_every_n_characters(input_string, n):
    """
    Adds a newline character every n characters in the input string.

    Args:
    input_string (str): The string to be processed.
    n (int): The number of characters after which a newline is added.

    Returns:
    str: The processed string with newlines added.
    """
    return 

def filter_dataframe_by_column_values(df:"pd.DataFrame", attributes:Dict):
    for attribute, value in attributes.items():
        if (value is None):
            continue
        if (attribute not in df.columns) or len(df) == 0:
            df = df.loc[[]]
            break
        if isinstance(value, (list, tuple)):
            df = df[df[attribute].isin(value)]
        elif isinstance(value, str):
            df = df[df[attribute].str.fullmatch(value)]
        elif isinstance(value, Callable):
            df = df[df[attribute].apply(value)]
        else:
            df = df[df[attribute] == value]
    df = df.reset_index(drop=True)
    return df