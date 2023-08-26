import numpy as np
from matplotlib import pyplot as plt

np.random.seed(0)

train_data_path = "data/train/train-images-idx3-ubyte"
train_labels_path = "data/train/train-labels-idx1-ubyte"

test_data_path = "data/test/t10k-images-idx3-ubyte"
test_labels_path = "data/test/t10k-labels-idx1-ubyte"

bytestring = b''

block_size_map = {
    0x08: 1,
    0x09: 1,
    0x0B: 2,
    0x0C: 4,
    0x0D: 4,
    0x0E: 8,
}

def convert_idx_to_arr(file_path):
    output = None
    with open(file_path, "rb") as f:
        # skip the first two bytes
        f.read(2)

        # read data type and num of dimensions
        block_size = block_size_map[int.from_bytes(f.read(1), "big")]
        dimensions = int.from_bytes(f.read(1), "big")
        shape = []
        for i in range(dimensions):
            shape.append(int.from_bytes(f.read(4), "big"))
        print(f"Reading {file_path} with shape {shape} and block size {block_size}")
        output = np.zeros(np.prod(shape))
        i = 0
        while (byte := f.read(block_size)):
            output[i] = int.from_bytes(byte, "big")
            i += 1
    return output.reshape(shape).astype(np.float128)

train_labels = convert_idx_to_arr(train_labels_path)
train_data = convert_idx_to_arr(train_data_path)

test_labels = convert_idx_to_arr(test_labels_path)
test_data = convert_idx_to_arr(test_data_path)

m,l,w = train_data.shape
X = np.reshape(train_data, (m, l * w)).transpose() / 255
X_test = np.reshape(test_data, (test_data.shape[0], l * w)).transpose() / 255

W1 = np.random.randn(10, 784)
B1 = np.random.randn(10, 1)

W2 = np.random.randn(10, 10)
B2 = np.random.randn(10, 1)

fp_i = 0

def forward_propagate(A):
    global fp_i
    Z1 = np.dot(W1, A) + B1
    A1 = np.maximum(0, Z1)
    Z2 = np.dot(W2, A1) + B2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

def softmax(z):
    assert len(z.shape) == 2
    s = np.max(z, axis=1)
    s = s[:, np.newaxis] # necessary step to do broadcasting
    e_x = np.exp(z - s)
    div = np.sum(e_x, axis=1)
    div = div[:, np.newaxis] # dito
    return e_x / div

def predict(A):
    _, _, _, A2 = forward_propagate(A)
    return A2

def one_hot_encode(labels):
    one_hot = np.zeros((labels.shape[0], 10))
    for i in range(labels.shape[0]):
        one_hot[i][int(labels[i])] = 1
    return one_hot

def back_propagate(A1, Z1, A2, Y):
    dZ2 = A2 - Y
    dW2 = np.dot(dZ2, A1.transpose()) / m
    dB2 = np.sum(dZ2, axis=1, keepdims=True) / m
    dZ1 = np.dot(W2.transpose(), dZ2) * (Z1 > 0)
    dW1 = np.dot(dZ1, X.transpose()) / m
    dB1 = np.sum(dZ1, axis=1, keepdims=True) / m
    return dW1, dB1, dW2, dB2

def adjust_weights(dW1, dB1, dW2, dB2, alpha):
    global W1, B1, W2, B2
    print(W1,B1,W2)
    W1 -= alpha * dW1
    B1 -= alpha * dB1
    W2 -= alpha * dW2
    B2 -= alpha * dB2

epochs = 1000
for i in range(epochs):
    print(f"Epoch {i}")
    Z1, A1, Z2, A2 = forward_propagate(X)
    Y = one_hot_encode(train_labels).transpose()
    print(f"Loss: {np.average(np.sum(np.square((A2 - Y)), axis=0)/m)}")
    dW1, dB1, dW2, dB2 = back_propagate(A1, A2, Z1, Y)
    adjust_weights(dW1, dB1, dW2, dB2, 0.1)
    pred = predict(X_test)
    print(f"Accuracy: {np.sum(np.argmax(pred, axis=0) == test_labels) / test_labels.shape[0]}")