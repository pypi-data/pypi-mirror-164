
import numpy as np
import pandas as pd
from sparse import COO


def numpy_aggregate(a, axes, index_names=None, value_name='value', aggfunc='mean', as_frame=True):
    """
    Aggregate numpy array with an arbitrary number of axes.

    Parameters
    ----------
    a : numpy.ndarray
    axes : list-like
        New axis values for axes of `a`. Must be one for each axis. If set to None, axis will be ignored.
    index_names : list-like
        Axes names.
    value_name : str
        Value column name.
    aggfunc : str
        How to pivot the data. Follows the pandas convention.
    as_frame : bool

    Returns
    -------
    pandas.DataFrame or numpy.ndarray
    """

    # Make sure `a` is a numpy array
    if not isinstance(a, np.ndarray):
        raise AttributeError('`a` must be a numpy array')

    # Set index_names
    if index_names is None:
        index_names = [f'axis{i}' for i in range(len(axes))]

    # Make sure index_names and axes are same length
    if len(axes) != len(index_names):
        raise AttributeError('`axes` and `index_names` must be same length')

    # Get sparse representation of `a`
    a_sparse = COO(a)

    # Update axis IDs if necessary
    for i, axis in zip(range(len(axes)), axes):
        if axis is not None:
            a_sparse.coords[i] = pd.Series(dict(zip(range(a.shape[i]), axis)))[a_sparse.coords[i]].to_numpy()

    # Create DataFrame
    data = dict(zip(index_names, a_sparse.coords))  # axes
    data.update({value_name: a_sparse.data})  # add value
    df = pd.DataFrame(data)

    # Aggregate
    df_agg = df.pivot_table(index=index_names, values=value_name, aggfunc=aggfunc)

    # What to return?
    if as_frame:
        return df_agg
    else:
        # TODO Is there a possibility that, with ND bins, you might have incomplete representation of bins?
        # TODO For instance, 0: {0, 1}, 1: {0, 1, 2} would break the code below. I don't think this can happen though.
        return df_agg.to_numpy().reshape(*[len(np.unique(axis)) for axis in axes])


# Unpack
def unpack(a):
    """
    Unpack a higher dimensional structure into a few variables. For instance, a dataframe with an index and a single
    column could be unpacked into the variable "x" for the index and "y" for the first column.

    Parameters
    ----------
    a : pd.DataFrame

    Returns
    -------
    np.ndarray
        Unpacked data
    """
    if isinstance(a, pd.DataFrame):
        return a.reset_index().T.to_numpy()
    else:
        raise AttributeError


def wherein(a, b):
    return pd.Series(np.arange(len(b)), index=b)[a].to_numpy()


# Convenience zfill function
def zfill(a, width=None):
    if width is None:
        return a
    elif hasattr(a, '__getitem__'):
        return np.char.zfill(list(map(str, a)), width)
    else:
        return str(a).zfill(width)


# Convenience zfill range function
def zfillr(n, width=None):
    return zfill(range(n), width)


if __name__ == '__main__':
    a = np.random.rand(3, 6, 100)
    x = [0, 0, 1]
    y = [0, 1, 2, 0, 1, 2]
    ap = numpy_pivot(a, axes=[x, y])

