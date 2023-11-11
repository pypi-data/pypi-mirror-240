import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from qiskit import Aer, QuantumCircuit
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes, ZFeatureMap
import qiskit_algorithms
from qiskit.algorithms.optimizers import COBYLA
from qiskit.primitives import Sampler
from matplotlib import pyplot as plt
from IPython.display import clear_output
from qiskit_machine_learning.algorithms.classifiers import NeuralNetworkClassifier
from qiskit_machine_learning.neural_networks import TwoLayerQNN
from qiskit.utils import algorithm_globals
import time
import warnings
warnings.simplefilter('ignore')
def suggested_dataset_QNN(random_state=1):
    """
    Generate a suggested dataset for Quantum Neural Networks (QNN).

    This function creates a synthetic dataset for binary classification suitable for training Quantum Neural Networks.
    It generates random input samples and assigns binary labels based on the sum of input features.

    Parameters:
    - random_state (int, optional): Seed for reproducibility of random data generation.

    Returns:
    tuple: A tuple containing:
        - X (numpy.ndarray): Input data of shape (num_samples, num_inputs), where each row represents a sample
          with `num_inputs` features.
        - y (numpy.ndarray): Binary labels corresponding to the input data, in {-1, +1} format.
    """
    num_inputs = 2
    num_samples = 100
    X = 2 * algorithm_globals.random.random([num_samples, num_inputs]) - 1
    y01 = 1 * (np.sum(X, axis=1) >= 0)  # in { 0,  1}
    y = 2 * y01 - 1  # in {-1, +1}
    return X, y
def load_dataset_qnn(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Load or generate a dataset for Quantum Neural Networks (QNN) training.

    This function allows loading a user-provided dataset or generating a suggested synthetic dataset
    for binary classification suitable for training Quantum Neural Networks.

    Parameters:
    - X (numpy.ndarray, optional): Input data. If None, the function attempts to generate or load suggested data.
    - y (numpy.ndarray, optional): Binary labels corresponding to the input data. If None, the function attempts
      to generate or load suggested data.
    - suggested_data (bool, optional): If True, generate and return a suggested synthetic dataset using the
      `suggested_dataset_QNN` function.
    - test_size (float, optional): Proportion of the dataset to include in the test split if generating suggested data.
    - random_state (int, optional): Seed for reproducibility of random data generation.

    Returns:
    tuple: A tuple containing:
        - X (numpy.ndarray): Input data of shape (num_samples, num_inputs), where each row represents a sample
          with `num_inputs` features.
        - y (numpy.ndarray): Binary labels corresponding to the input data, in {-1, +1} format.

    Note:
    If `suggested_data` is True, the function either generates a suggested dataset or loads a previously generated one.
    If `suggested_data` is False and `X` and `y` are provided, the function checks the validity of the input data and
    returns it if in the appropriate format. If there are issues with the provided data, the function prints an error
    message and returns None.
    """
    if suggested_data:
        X_suggested, y_suggested = suggested_dataset_QNN(random_state)
        return X_suggested, y_suggested

    if X is None or y is None:
        print("Data loading failed.")
        return None, None

    if len(X.shape) != 2 or len(y.shape) != 1:
        print("The provided data does not have the appropriate format.")
        return None, None

    return X, y

def QNN(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Train a Quantum Neural Network (QNN) classifier using the provided or suggested dataset.

    This function utilizes a Quantum Neural Network (QNN) to train a binary classifier. It can either use a
    user-provided dataset or generate a suggested synthetic dataset for training.

    Parameters:
    - X (numpy.ndarray, optional): Input data. If None, the function attempts to generate or load suggested data.
    - y (numpy.ndarray, optional): Binary labels corresponding to the input data. If None, the function attempts
      to generate or load suggested data.
    - suggested_data (bool, optional): If True, generate and use a suggested synthetic dataset using the
      `load_dataset_qnn` function.
    - test_size (float, optional): Proportion of the dataset to include in the test split if generating suggested data.
    - random_state (int, optional): Seed for reproducibility of random data generation.

    Returns:
    str: The classification report containing precision, recall, and F1-score for the test set.

    Note:
    If `suggested_data` is True, the function generates or loads a suggested dataset using the `load_dataset_qnn` function.
    If `suggested_data` is False and `X` and `y` are provided, the function checks the validity of the input data and
    proceeds with training the QNN classifier. If there are issues with the provided data, the function prints an error
    message and returns None.
    """
    if suggested_data:
        X, y = load_dataset_qnn(suggested_data=True)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    else:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    if X_train is None or y_train is None:
        print("Data loading failed.")
        return None

    if len(X_train.shape) != 2 or len(y_train.shape) != 1:
        print("The provided data does not have the appropriate format.")
        return None
    objective_func_vals = []
    def callback_graph(weights, obj_func_eval):
        clear_output(wait=True)
        objective_func_vals.append(obj_func_eval)
        plt.title("Live loss curve")
        plt.xlabel("Iteration")
        plt.ylabel("Loss value")
        plt.plot(range(len(objective_func_vals)), objective_func_vals,color='red')
        plt.show()
    qc = QuantumCircuit(X.shape[1])
    feature_map = ZZFeatureMap(X.shape[1],reps=4)
    ansatz = RealAmplitudes(X.shape[1])
    qc.compose(feature_map, inplace=True)
    qc.compose(ansatz, inplace=True)
    estimator_qnn = TwoLayerQNN(
        feature_map=feature_map,
        ansatz=ansatz,
        quantum_instance=Aer.get_backend('statevector_simulator'),
    )
    estimator_classifier = NeuralNetworkClassifier(
        estimator_qnn, optimizer=COBYLA(maxiter=200), callback=callback_graph
    )
    start = time.time()
    estimator_classifier.fit(X_train, y_train)
    elapsed = time.time() - start
    y_pred_test = estimator_classifier.predict(X_test)  
    test_score_qnn = np.mean(y_pred_test == y_test)
    #training_time_str = "The training time: {:.2f} s".format(elapsed)
    test_score_qnn = np.mean(y_pred_test == y_test)
    report = classification_report(y_test, y_pred_test)
    x=print("Classification Report:\n", report)  # Print the classification report
    return x
