"""tensor.py libscientific python binding

Copyright (C) <2023>  Giuseppe Marco Randazzo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import ctypes
from libscientific.loadlibrary import load_libscientific_library
from libscientific import misc
from libscientific import matrix as mx
from libscientific import vector as vect

lsci = load_libscientific_library()

class TENSOR(ctypes.Structure):
    """
    tensor data structure
    """
    _fields_ = [
        ("m", ctypes.POINTER(ctypes.POINTER(mx.MATRIX))),
        ("order", ctypes.c_size_t)]

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return self.__class__.__name__

lsci.initTensor.argtypes = [ctypes.POINTER(ctypes.POINTER(TENSOR))]
lsci.initTensor.restype = None

def init_tensor():
    """
    initTensor: Allocate in memory an empty libscientific tensor
    """
    tns = ctypes.POINTER(TENSOR)()
    lsci.initTensor(ctypes.pointer(tns))
    return tns


lsci.NewTensorMatrix.argtypes = [ctypes.POINTER(TENSOR),
                                 ctypes.c_size_t,
                                 ctypes.c_size_t,
                                 ctypes.c_size_t]
lsci.NewTensorMatrix.restype = None

def new_tensor_matrix(tns, k_indx, num_row, num_col):
    """
    Create a new matrix on tensor tns at index k_indx
    """
    lsci.NewTensorMatrix(tns, k_indx, num_row, num_col)


lsci.AddTensorMatrix.argtypes = [ctypes.POINTER(TENSOR),
                                 ctypes.c_size_t,
                                 ctypes.c_size_t]
lsci.AddTensorMatrix.restype = None

def add_tensor_matrix(tns, num_row, num_col):
    """
    Add a new matrix to the tensor tns
    """
    lsci.AddTensorMatrix(tns, num_row, num_col)


lsci.NewTensor.argtypes = [ctypes.POINTER(ctypes.POINTER(TENSOR)),
                           ctypes.c_size_t]
lsci.NewTensor.restype = None

def new_tensor(tns_input_):
    """
    NewTensor: Allocate in memory a libscientific tensor
    from a list of lists of lists
    """
    tns_input = None
    if "numpy" in str(type(tns_input_)):
        tns_input = tns_input_.tolist()
    else:
        tns_input = tns_input_
    order = len(tns_input)
    tns = ctypes.POINTER(TENSOR)()
    lsci.NewTensor(ctypes.pointer(tns), order)
    for k in range(order):
        nrows = len(tns_input[k])
        ncols = len(tns_input[k][0])
        lsci.NewTensorMatrix(tns, k, nrows, ncols)
        for i in range(nrows):
            for j in range(ncols):
                val = None
                try:
                    val = float(tns_input[k][i][j])
                except ValueError:
                    val = None

                if val is None:
                    tns.contents.m[k].contents.data[i][j] = misc.missing_value()
                else:
                    tns.contents.m[k].contents.data[i][j] = val
    return tns


lsci.DelTensor.argtypes = [ctypes.POINTER(ctypes.POINTER(TENSOR))]
lsci.DelTensor.restype = None

def del_tensor(tns):
    """
    Delete the moemory allocated tensor
    """
    lsci.DelTensor(ctypes.pointer(tns))


lsci.PrintTensor.argtypes = [ctypes.POINTER(TENSOR)]
lsci.PrintTensor.restype = None

def print_tensor(tns):
    """
    Debug the tensor content
    """
    lsci.PrintTensor(tns)


lsci.setTensorValue.argtypes = [ctypes.POINTER(TENSOR)]
lsci.setTensorValue.restype = None

def set_tensor_value(tns, k_indx, i_indx, j_indx, val):
    """
    Set the tensor value at indexes k_indx, i_indx, j_indx
    """
    lsci.setTensorValue(tns, k_indx, i_indx, j_indx, val)


lsci.TensorAppendColumn.argtypes = [ctypes.POINTER(TENSOR),
                                    ctypes.c_size_t,
                                    ctypes.POINTER(vect.DVECTOR)]
lsci.TensorAppendColumn.restype = None

def tensor_append_column(tns, k_indx, dvect):
    """
    Append a colum to the matrix at index k_indx inside the tensor tns
    """
    lsci.TensorAppendColumn(tns, k_indx, dvect)


lsci.TensorAppendRow.argtypes = [ctypes.POINTER(TENSOR),
                                 ctypes.c_size_t,
                                 ctypes.POINTER(vect.DVECTOR)]
lsci.TensorAppendRow.restype = None

def tensor_append_row(tns, k_indx, dvect):
    """
    Append a row to the matrix at index k_indx inside the tensor tns
    """
    lsci.TensorAppendRow(tns, k_indx, dvect)


lsci.TensorSet.argtypes = [ctypes.POINTER(TENSOR),
                           ctypes.c_double]
lsci.TensorSet.restype = None

def tensor_set(tns, val):
    """
    Set all the tensor values to a given value val
    """
    lsci.TensorSet(tns, val)


lsci.TensorCopy.argtypes = [ctypes.POINTER(TENSOR),
                           ctypes.POINTER(ctypes.POINTER(TENSOR))]
lsci.TensorCopy.restype = None

def tensor_copy(src_tns, dst_tns):
    """
    Copy a source tensor to a destination tensor
    """
    lsci.TensorCopy(src_tns, ctypes.pointer(dst_tns))


def tensor_tolist(tns):
    """
    Convert a tensor to list
    """
    tns_lst = []
    for k in range(tns.contents.order):
        tns_lst.append(mx.matrix_to_list(tns.contents.m[k]))
    return tns_lst


class Tensor:
    """
    Tensor Class

    This class provides methods for creating and manipulating tensors using libscientific.

    Attributes:
        tns (CDataType): The tensor data.

    Methods:
        __init__(self, tns_)
        __del__(self)
        __getitem__(self, keys)
        __setitem__(self, keys, value)
        order(self)
        nrow(self, k)
        ncol(self, k)
        data_ptr(self)
        tolist(self)
        fromlist(self, tns_)
        fromnumpy(self, npt)
        debug(self)
    """

    def __init__(self, tns_):
        """
        Initialize a Tensor instance.

        Args:
            tns_ : list of list of list or None
                The tensor data. If None, initializes an empty tensor.
        """
        if tns_ is None:
            self.tns = init_tensor()
        else:
            self.tns = new_tensor(tns_)

    def __del__(self):
        """
        Clean up resources associated with the Tensor instance.
        """
        del_tensor(self.tns)
        del self.tns
        self.tns = None

    def __getitem__(self, keys):
        """
        Get the value at the specified indices in the tensor.

        Args:
            keys : tuple
                Tuple of indices (k, i, j).

        Returns:
            float : The value at the specified indices.
        """
        k, i, j = keys
        return self.data_ptr().m[k].contents.data[i][j]

    def __setitem__(self, keys, value):
        """
        Set the value at the specified indices in the tensor.

        Args:
            keys : tuple
                Tuple of indices (k, i, j).
            value : float
                The value to set at the specified indices.
        """
        k, i, j = keys
        self.data_ptr().m[k].contents.data[i][j] = value

    def order(self):
        """
        Get the order of the tensor, i.e., the number of matrices constituting the tensor.

        Returns:
            int : The order of the tensor.
        """
        return self.data_ptr().order

    def nrow(self, k):
        """
        Get the number of rows in the specified matrix (k) of the tensor.

        Args:
            k : int
                Index of the matrix in the tensor.

        Returns:
            int : Number of rows in the specified matrix.
        """
        return self.data_ptr().m[k].contents.row

    def ncol(self, k):
        """
        Get the number of columns in the specified matrix (k) of the tensor.

        Args:
            k : int
                Index of the matrix in the tensor.

        Returns:
            int : Number of columns in the specified matrix.
        """
        return self.data_ptr().m[k].contents.col

    def data_ptr(self):
        """
        Get the tensor data pointer.

        Returns:
            CDataType : The tensor data pointer.
        """
        return self.tns.contents

    def tolist(self):
        """
        Convert the tensor to a nested list.

        Returns:
            list : The tensor as a nested list.
        """
        return tensor_tolist(self.tns)

    def fromlist(self, tns_):
        """
        Initialize the tensor from a nested list.

        Args:
            tns_ : list of list of list
                The tensor data as a nested list.
        """
        del_tensor(self.tns)
        del self.tns
        self.tns = new_tensor(tns_)

    def fromnumpy(self, npt):
        """
        Initialize the tensor from a NumPy array.

        Args:
            npt : numpy.ndarray
                The NumPy array to initialize the tensor from.
        """
        tns_ = npt.tolist()
        del_tensor(self.tns)
        del self.tns
        self.tns = new_tensor(tns_)

    def debug(self):
        """
        Print the tensor for debugging purposes.
        """
        print_tensor(self.tns)
