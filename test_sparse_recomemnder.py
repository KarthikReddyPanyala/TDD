import pytest
from sparse_recommender import SparseMatrix

# Test case for the 'set' method
def test_set():
    """Test case for the 'set' method of the SparseMatrix class.testcase verifies that the 'set' method """
    matrix = SparseMatrix()
    matrix.set(5,4 , 42)
    assert matrix.get(5, 4) == 42

# Test case for the 'get' method
def test_get():
    """Test case for the 'get' method of the SparseMatrix class.It checks if the 'get' method correctly retrieves values"""
    matrix = SparseMatrix()
    matrix.set(4, 3, 67)
    assert matrix.get(4, 3) == 67
    assert matrix.get(0, 0) == 0

# Test case for the 'recommend' method
def test_recommend():
    """Test case for the 'recommend' method of the SparseMatrix class.It tests whether the 'recommend' method correctly computes recommendations
    based on a given vector."""
    matrix = SparseMatrix()
    matrix.set(0, 0, 7)
    matrix.set(1, 0, 8)
    vector = [5, 5]
    recommendations = matrix.recommend(vector)
    assert recommendations == {0: 75}

# Test case for the 'add_movie' method
def test_add_movie():
    """Test case for the 'add_movie' method of the SparseMatrix class.It verifies that the 'add_movie' method correctly adds another sparse matrix
    to the current matrix."""
    mat1 = SparseMatrix()
    mat1.set(0, 0, 10)
    mat2 = SparseMatrix()
    mat2.set(1, 1, 20)
    testmat = mat1.add_movie(mat2)
    assert testmat.get(0, 0) == 10

# Test case for the 'to_dense' method
def test_to_dense():
    """Test case for the 'to_dense' method of the SparseMatrix class.It checks whether the 'to_dense' method correctly converts a sparse matrix
    into a dense representation."""
    mat1 = SparseMatrix()
    densemat = mat1.to_dense()
    assert densemat == []
