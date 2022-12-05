#  Created by Ikshul Bethur
#  Copyright © 2020 Ikshul Bethur. All rights reserved.

import json
import math
import random

class node:

    def __init__(self, numOfWeights):
        self.weights = []
        self.bias = 0
        self.size = numOfWeights
        self.buildNode()

    def buildNode(self):
        for i in range(self.size):
            self.weights.append(random.random())
        bias = random.random()

    #Activation funcion applied after each neuron calculation
    def sigmoid(self, x):
            return 1 / (1 + pow(math.e, -x))
    def ReLU(self, x):
        if x > 0:
            return x
        if x <= 0:
            return 0

    def exe(self, inPuts):
        if len(inPuts) != len(self.weights):
            return
        myProduct = 0
        
        for i in range(self.size):
            myProduct += self.weights[i] * inPuts[i]

        myProduct += self.bias

        return self.ReLU(myProduct)

class layer:

    #Constructor for a new hidden layer
    def __init__(self, size, inSize):
        self.size = size
        self.inSize = inSize
        self.nodes = []
        self.outputs = [0] * size
        self.buildLayer()
            
    def buildLayer(self):
        for i in range(self.size):
            self.nodes.append(node(self.inSize))
        
    def layerExe(self, inputs):
        for i in range(self.size):
            self.outputs[i] = self.nodes[i].exe(inputs)

class inputLayer(layer):

    #Constructor for an input layer
    def __init__(self, size):
        self.size = size

    def layerExe(self, inputs):
        self.outputs = inputs

class Network:
    #size #int - Number of layers | 3
    #layerSizes #[int] - Size of each layer | [2, 3, 2]
    #[layer] - holds each layer | [layer, layer, layer]

    #I/O
    #inputs
    #outputs

    def __init__(self, layerSizes):
        self.size = len(layerSizes)
        self.layerSizes = layerSizes
        self.layers = [inputLayer(layerSizes[0])]
        self.create()

    def create(self):
        for i in range(1, self.size):
            self.layers.append(layer(self.layerSizes[i], self.layerSizes[i-1]))
    
    def exe(self, inputs):
        if len(inputs) != self.layerSizes[0]:
            return
        
        self.layers[0].layerExe(inputs)
        for i in range(1, self.size):
            self.layers[i].layerExe(self.layers[i-1].outputs)
            
        return self.layers[self.size - 1].outputs

class Train:
    def __init__(self):
        return

testNetworkLayerSizes = [2, 3, 2]
testInputs = [2, 2]

testNetwork = Network(testNetworkLayerSizes)

print(testNetwork.exe(testInputs))

print("Break")