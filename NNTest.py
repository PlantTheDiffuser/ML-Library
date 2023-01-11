import Library


testNetworkLayerSizes = [2, 3, 2]
testNetworkData = [[0.2, 0.1, 0.6], [0.2, 0.5, 0.2], [0.3, 0.9, 0.2], [0.6, 0.2, 0.6, 1], [0.1, 0.8, 0.9, 0.3]]
testInputs = [0, 1]
Library.networkData = testNetworkData
testNetwork = Library.Network(testNetworkLayerSizes, testNetworkData)

print(testNetwork.exe(testInputs))