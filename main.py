import os
import importlib.util
import unittest

# Import Array from the root directory
from Array import Array

def import_module_from_directory(base_path, module_name):
    # Construct the full path to the module
    module_path = os.path.join(base_path, module_name)
    # Create a module spec
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    # Create a module from the spec
    module = importlib.util.module_from_spec(spec)
    # Load the module
    spec.loader.exec_module(module)
    return module

# Define a class or a dictionary to hold modules
class TestModules:
    pass

test_modules = TestModules()

def main():
    # Path to the 'test' directory
    test_dir = './test'

    # List directories in the 'test' folder
    for dir_name in os.listdir(test_dir):
        dir_path = os.path.join(test_dir, dir_name)
        if os.path.isdir(dir_path) and not dir_name.startswith('__'):
            algorithm_name = dir_name[2:]  # Adjust slicing if needed based on actual dir names
            result_module_name = f"{algorithm_name}_result.py"
            try:
                # Import the *_result.py module from each subdirectory
                module = import_module_from_directory(dir_path, result_module_name)
                # Save the module to a variable with a sanitized name
                sanitized_name = dir_name.replace(" ", "_").replace("-", "_").lstrip("0123456789")
                setattr(test_modules, sanitized_name, module)
            except FileNotFoundError:
                print(f"No {result_module_name} in {dir_name}")

    # Print every module in the test_modules
    for module_name in dir(test_modules):
        # if not module_name.startswith("__"):
        print(module_name)
            
class TestOfCormens(unittest.TestCase):
    def test_insertionsort(self):
        print("-------------Insertion sort-------------")
        # The INSERTION_SORT function sorts an array A by iteratively taking each element 
        # and inserting it into its correct position within the sorted portion of the array.
        my_array = Array([5, 2, 4, 6, 1, 3])
        # Access and run the INSERTION_SORT function dynamically
        insertion_sort_module = getattr(test_modules, "InsertionSort")
        insertion_sort_module.INSERTION_SORT(my_array)
        self.assertEqual(my_array, Array([1, 2, 3, 4, 5, 6]))
        print(my_array)

    def test_optimalBST(self):
        print("-------------Optimal BST-------------")
        # The OPTIMAL_BST function calculates the minimum search cost and structure of an optimal binary search tree (BST) using dynamic programming.
        p = Array([0.0, 0.15, 0.1, 0.05, 0.1, 0.2])
        q = Array([0.05, 0.1, 0.05, 0.05, 0.05, 0.1])
        n = len(p) - 1
        # Access and run the OptimalBST function dynamically
        optimal_bst_module = getattr(test_modules, "Optimal_BST")
        e, root = optimal_bst_module.OPTIMAL_BST(p, q, n)

        # Print the results
        print("Optimal Expected Search Cost Matrix (e):")
        for row in e:
            print(row)

        print("\nRoot Matrix (root):")
        for row in root:
            print(row)

    def test_merge(self):
        print("-------------Merge-------------")
        # The MERGE function merges two sorted subarrays into a single sorted subarray in a given array A.
        # Example usage:
        # Define the input array and indices
        A = Array([3, 7, 12, 14, 18, 9, 11, 16, 21])
        p = 1
        q = 5
        r = 9
        # Print the sorted array
        # Access and run the Merge function dynamically
        merge_module = getattr(test_modules, "Merge")
        merge_module.MERGE(A, p, q, r)
        self.assertEqual(A, Array([3, 7, 9, 11, 12, 14, 16, 18, 21]))
        print("Sorted array after merging:", A)

    def test_memoizedMatrixChain(self):
        print("-------------Memoized Matrix Chain-------------")
        # The function computes the minimum cost of multiplying a chain of matrices using memoization.
        p = Array([30, 35, 15, 5, 10, 20, 25])
        # Access and run the MemoizedMatrixChain function dynamically
        memoized_matrix_chain_module = getattr(test_modules, "Memoized_Matrix_Chain")
        matrix = memoized_matrix_chain_module.MEMOIZED_MATRIX_CHAIN(p)
        self.assertEqual(matrix, 15125)
        
        print(matrix)

    def test_recursiveMatrixChain(self):
        print("-------------Recursive matrix chain-------------")
        # The RECURSIVE_MATRIX_CHAIN function calculates the minimum cost of multiplying a chain of matrices using a recursive approach.
        P = Array([4,10,3,12,20,7])  # Dimensions of matrices
        j = len(P) - 1  # Number of matrices
        m = Array([[0 for _ in range(j + 1)] for _ in range(j + 1)])  # Initialize the m matrix
        # Access and run the RecursiveMatrixChain function dynamically
        recursive_matrix_chain_module = getattr(test_modules, "Recursive_Matrix_Chain")
        result = recursive_matrix_chain_module.RECURSIVE_MATRIX_CHAIN(P, 1, j, m)
        print("RESULT HER:")
        print(result)
        self.assertEqual(result, 1344)
        print("Minimum number of multiplications:", result)

    # def test_matrixChainOrder(self):
    #     print("-------------Matrix chain order-------------")
    #     # The MATRIX_CHAIN_ORDER function calculates the minimum number of multiplications needed to multiply a chain of matrices.
    #     # Access and run the Matrix_Chain_Order function dynamically
    #     # Example usage:
    #     p = Array([30, 35, 15, 5, 10, 20, 25])  # Dimensions of matrices
    #     matrix_chain_order_module = getattr(test_modules, "Matrix_Chain_Order")
    #     m_result, s_result = matrix_chain_order_module.MATRIX_CHAIN_ORDER(p)
    #     print(m_result)
    #     print("Minimum number of multiplications:", m_result, s_result)
    #     self.assertEqual(m_result, Array([Array([1, 2, 3]), Array([4, 5, 6])]))
        

    def test_extendedBottomUpCutRod(self):
        print("-------------Extended bottom up cut rod-------------")
        # The EXTENDED_BOTTOM_UP_CUT_ROD function calculates the optimal revenue and cut positions for a rod of length n.
        # Access and run the ExtendedBottomUpCutRod function dynamically
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 10  # Desired rod length
        extended_bottom_up_cut_rod_module = getattr(test_modules, "Extended_Bottom_Up_Cut_Rod")
        r, s = extended_bottom_up_cut_rod_module.EXTENDED_BOTTOM_UP_CUT_ROD(prices , n)
        """Print how far apart to cut."""
        while n > 0:
            print(s[n], end=" ")  # cut location for length n
            self.assertEqual(s[n], 10)          
            n -= s[n]  # length of the remainder of the rod
        print()

    def test_bubbleSort(self):
        print("-------------Bubble sort-------------")
        # The BUBBLESORT function sorts an array A by repeatedly swapping adjacent elements if they are in the wrong order.
        # Access and run the BubbleSort function dynamically
        myArray = Array([5, 2, 4, 6, 1, 3])
        bubble_sort_module = getattr(test_modules, "BubbleSort")
        bubble_sort_module.BUBBLESORT(myArray)
        self.assertEqual(myArray, Array([1, 2, 3, 4, 5, 6]))
        print("Sorted array:", myArray)

    def test_squareMatrixMultiply(self): 
        print("-------------Square Matrix multiply-------------")
        # The SQUARE_MATRIX_MULTIPLY function multiplies two square matrices A and B.
        # Example usage:
        A = Array([Array([1, 2, 3]),
                Array([4, 5, 6]),
                Array([7, 8, 9])])

        B = Array([Array([9, 8, 7]),
                Array([6, 5, 4]),
                Array([3, 2, 1])])

        # Access and run the SquareMatrixMultiply function dynamically
        square_matrix_multiply_module = getattr(test_modules, "Square_Matrix_Multiply")
        result = square_matrix_multiply_module.SQUARE_MATRIX_MULTIPLY(A,B)
        self.assertEqual(result, Array([Array([30, 24, 18]),Array([84, 69, 54]),Array([138, 114, 90])]))
        print(result)

    # def test_squareMatrixMultiplyRecursive(self):
    #     print("-------------Square matrix multiply recursive-------------")
    #     # The SQUARE_MATRIX_MULTIPLY_RECURSIVE function multiplies two square matrices A and B using a recursive approach.
    #     # Access and run the SquareMatrixMultiplyRecursive function dynamically
    #     A = Array([Array([1, 2]),
    #             Array([4, 5])])

    #     B = Array([Array([9, 8]),
    #             Array([6, 5])])

    #     square_matrix_multiply_recursive_module = getattr(test_modules, "Square_Matrix_Multiply_Recursive")
    #     result = square_matrix_multiply_recursive_module.SQUARE_MATRIX_MULTIPLY_RECURSIVE(A,B)
    #     self.assertEqual(result, Array([Array([21, 18]),Array([66, 57])]))
    #     print(result)

    def test_heapIncreaseKey(self):
        print("-------------Heap increase key-------------")
        # The HEAP_INCREASE_KEY function increases the value of a key in a max heap and maintains the max-heap property.
        # Access and run the HeapIncreaseKey function dynamically
        A = Array([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        i = 5
        key = 15
        heap_increase_key_module = getattr(test_modules, "Heap_Increase_Key")
        heap_increase_key_module.HEAP_INCREASE_KEY(A,i,key)    
        self.assertEqual(A, Array([16, 14, 10, 8, 15, 9, 3, 2, 4, 1]))
        print(A)   

    def test_findMaxCrossingSubarray(self):
        print("-------------Find max crossing sub array-------------")
        # The FIND_MAX_CROSSING_SUBARRAY function finds the maximum subarray that crosses the midpoint of an array.
        # Access and run the FindMaxCrossingSubarray function dynamically
        A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        _low = 0
        _high = len(A) - 1
        mid = (_low + _high) // 2
        find_max_crossing_subarray_module = getattr(test_modules, "Find_Max_Crossing_Subarray")
        max_left, max_right, max_sum = find_max_crossing_subarray_module.FIND_MAX_CROSSING_SUBARRAY(A, _low, mid, _high)
        self.assertEqual(max_left, 7)
        self.assertEqual(max_right, 10)
        self.assertEqual(max_sum, 43)
        print(f"Max crossing subarray: from index {max_left} to {max_right} with sum {max_sum}")

    # The following functions are not implemented in the test modules as they use random values, where the expected output is unknown.
    # def test_randomizeInPlace():
    #     print("-------------Randomize in place-------------")
    #     # The RANDOMIZE_IN_PLACE function randomly shuffles the elements of an array in place.
    #     # Access and run the RandomizeInPlace function dynamically
    #     A = Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    #     randomize_in_place_module = getattr(test_modules, "Randomize_In_Place")
    #     randomize_in_place_module.Randomize_In_Place(A)
    #     print(A)

    # def test_randomSample():
    #     print("-------------random sample-------------")
    #     # The RANDOM_SAMPLE function randomly selects a sample of k elements from an array A.
    #     # Access and run the RandomSample function dynamically
    #     m = 5
    #     n = 10
    #     random_sample_module = getattr(test_modules, "Random_Sample")
    #     sample = random_sample_module.Random_Sample(m,n)
    #     print("Random sample:", sample)

    # def test_onLineMaximum():
    #     print("-------------On line maximum-------------")
    #     # The ON_LINE_MAXIMUM function calculates the maximum value of a sliding window of size k in an array A.
    #     # Access and run the OnLineMaximum function dynamically
    #     k = 5
    #     n = 10
    #     on_line_maximum_module = getattr(test_modules, "On_Line_Maximum")
    #     result = on_line_maximum_module.ON_LINE_MAXIMUM(5,10)
    #     print("Maximum values of the sliding window:", result)

    # def test_greedyActivitySelector(self):
    #     print("-------------Greedy activity selector-------------")
    #     # The GREEDY_ACTIVITY_SELECTOR function selects the maximum number of mutually compatible activities.
    #     # Access and run the GreedyActivitySelector function dynamically
    #     s = Array([1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12])
    #     f = Array([4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16])
    #     greedy_activity_selector_module = getattr(test_modules, "Greedy_Activity_Selector")
    #     result = greedy_activity_selector_module.Greedy_Activity_Selector(s,f)
    #     self.assertEqual(result, [1, 4, 8, 11])
    #     print("Selected activities:", result)

    # def test_printPath():
    #     print("-------------Print path-------------")
    #     # The PRINT_PATH function prints the path from the source to a given vertex in a graph.
    #     # Access and run the PrintPath function dynamically
    #     print_path_module = getattr(test_modules, "PrintPath")
    #     print_path_module.PrintPath()        

    def test_binarySearchTree(self):
        # Create a TreeNode class
        class TreeNode:
            def __init__(self, key):
                self.key = key
                self.left = None
                self.right = None

        # Create a binary search tree
        root = TreeNode(13)
        node7 = TreeNode(7)
        node15 = TreeNode(15)
        node3 = TreeNode(3)
        node8 = TreeNode(8)
        node14 = TreeNode(14)
        node19 = TreeNode(19)
        node18 = TreeNode(18)

        root.left = node7
        root.right = node15

        node7.left = node3
        node7.right = node8

        node15.left = node14
        node15.right = node19

        node19.left = node18
        print("-------------Binary Search Tree-------------")
        # The BinarySearchTree function implements the basic operations of a binary search tree.
        # Access and run the BinarySearchTree function dynamically
        binary_search_tree_module = getattr(test_modules, "BST")
        binary_search_tree_module.TREE_INSERT(root, TreeNode(10))
        self.assertEqual(binary_search_tree_module.TREE_SEARCH(root, 10).key, 10)
        print("Found the node with the value: ",binary_search_tree_module.TREE_SEARCH(root, 7).key)
        print("Highest value in the tree: ", binary_search_tree_module.TREE_MAXIMUM(root).key)
        print("Lowest value in the tree: ", binary_search_tree_module.TREE_MINUMUM(root).key)

if __name__ == "__main__":
    main()
    unittest.main()
