import itertools
from itertools import product

import numpy as np

from .tensor import Tensor
from .log_formats import colorized_logger
logger = colorized_logger(__name__)


class TensorOperator:
    """
    A data structure for an endomorphism of tensors, a linear transformation, an
    element of End(V⊗...⊗V).
    """
    def __init__(self,
        number_of_factors: int=None,
        dimension: int=None,
        identity: bool=False,
        permutation_inverse=None,
        data=None,
    ):
        """
        :param number_of_factors: Number of tensor factors for the background tensor
            product vector space.
        :type number_of_factors: int

        :param dimension: The dimension of the base vector space.
        :type dimension: int

        :param identity: If True, initializes the TensorOperator to the identity
            operator.
        :type identity: bool

        :param permutation_inverse: If provided, initializes the
            :py:class:`TensorOperator` to be the operation of permutation of the
            tensor factors, for the inverse of the permutation indicated by this list of
            positive integers (e.g. ``[2, 1, 3]``).
        :type permutation_inverse: list

        :param data: If provided, initialized with exactly the given data array.
        :type data: numpy.array
        """
        self.number_of_factors = number_of_factors
        self.dimension = dimension
        if not data is None:
            if identity or (not permutation_inverse is None):
                logger.error(
                    'If specifying exact data array, do not provide identity flag or permutation!'
                )
            else:
                self.data = data
            return

        self.data = np.zeros(
            [dimension] * (number_of_factors * 2)
        )

        if identity and not permutation_inverse is None:
            logger.error('Provide identity=True or permutation_inverse, not both.')
            return

        n = self.number_of_factors
        if identity:
            iterator = np.nditer(self.data, flags = ['multi_index'])
            for entry in iterator:
                index = iterator.multi_index
                in_index = [index[i] for i in range(n)]
                out_index = [index[i+n] for i in range(n)]
                if in_index == out_index :
                    self.data[index] = 1.0
        if not permutation_inverse is None:
            iterator = np.nditer(self.data, flags = ['multi_index'])
            for entry in iterator:
                index = iterator.multi_index
                in_index = [index[i] for i in range(n)]
                out_index = [index[i+n] for i in range(n)]
                permuted_in_index = [index[permutation_inverse[i]-1] for i in range(n)]
                if permuted_in_index == out_index :
                    self.data[index] = 1.0

    def apply(self,
        input_tensor: Tensor=None,
    ):
        """
        :param input_tensor: The input to which to apply the :py:class:`TensorOperator`.
        :type input_tensor: Tensor

        :return: Result of application of the :py:class:`TensorOperator` linear map.
        :rtype: :py:class:`.tensor.Tensor`
        """
        if (
            input_tensor.number_of_factors != self.number_of_factors or
            input_tensor.dimension != self.dimension
        ):
            logger.error(
                ''.join([
                    'input_tensor type (number_of_factors, dimension)=(%s,%s) ',
                    'is not compatible with this operator, expected (%s, %s).',
                ]),
                str(input_tensor.number_of_factors),
                str(input_tensor.dimension),
                str(self.number_of_factors),
                str(self.dimension),
            )
            return None
        join_range_left = [i + self.number_of_factors for i in range(self.number_of_factors)]
        join_range_right = [i for i in range(self.number_of_factors)]
        output_data = np.tensordot(
            self.data,
            input_tensor.data,
            axes=(join_range_left, join_range_right),
        )
        output_tensor = Tensor(
            number_of_factors=self.number_of_factors,
            dimension=self.dimension,
            data=output_data,
        )
        return output_tensor

    def add(self,
        other_operator,
        inplace: bool=False,
    ):
        """
        :param other_operator: Another operator to add in-place.
        :type other_operator: TensorOperator

        :param inplace: If True, adds the other operator in place (so that a new
            :py:class:`TensorOperator` is not returned).
        :type inplace: bool

        :return: The sum (unless ``inplace=True``, then returns None).
        :rtype: TensorOperator
        """
        if inplace:
            self.data = self.data + other_operator.data
            return None

        tensor_operator = TensorOperator(
            number_of_factors=self.number_of_factors,
            dimension=self.dimension,
        )
        tensor_operator.data = self.data + other_operator.data
        return tensor_operator

    def scale_by(self,
        amount: float=None,
        inplace: bool=False,
    ):
        """
        Scalar multiplication, entrywise.

        :param amount: The scalar to multiply by.
        :type amount: float

        :param inplace: If True, returns None and modifies this
            :py:class:`TensorOperator` object in-place. Otherwise returns a new
            :py:class:`TensorOperator`, scaled.
        :type inplace: bool

        :return: The scaled operator (unless ``inplace=True``, then returns None).
        :rtype: TensorOperator
        """
        if inplace:
            self.data = self.data * amount
            return None

        tensor_operator = TensorOperator(self.number_of_factors, self.dimension)
        tensor_operator.data = self.data * amount
        return tensor_operator

    def __repr__(self):
        return OperatorPrinter.repr_of_tensor_operator(self.data)


class OperatorPrinter:
    @staticmethod
    def value_on_basis_element(operator, element):
        number_factors = int(len(operator.shape) / 2)
        dimension = operator.shape[0]
        tensor_element = np.zeros([dimension] * number_factors)
        tensor_element[tuple(element)] = 1
        join_range_left = [i + number_factors for i in range(number_factors)]
        join_range_right = [i for i in range(number_factors)]
        output_data = np.tensordot(
            operator,
            tensor_element,
            axes=(join_range_left, join_range_right),
        )
        indices = list(product(list(range(dimension)), repeat=3))
        return [
            (output_data[tuple(index)], index)
            for index in indices
            if output_data[index] != 0
        ]

    @staticmethod
    def polynomial(index, dual=False):
        base = '\u2297'.join(['e' + str(i) for i in index])
        if dual:
            base = '(' + base + ')*'
        return base

    @staticmethod
    def repr_of_tensor_operator(operator):
        number_factors = int(len(operator.shape) / 2)
        dimension = operator.shape[0]
        indices = list(product(list(range(dimension)), repeat=3))
        values = [(index, OperatorPrinter.value_on_basis_element(operator, index)) for index in indices]
        return '\n + '.join([
            '( ' +
            ' + '.join([
                str(coefficient) + ' ' + OperatorPrinter.polynomial(inner_index)
                for coefficient, inner_index in sparse_value
            ]) + ' ) ' + OperatorPrinter.polynomial(index, dual=True)
            for index, sparse_value in values
            if len(sparse_value) > 0
        ])
