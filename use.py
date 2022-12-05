import Library


testNetworkLayerSizes = [2, 3, 2]
testInputs = [2, 2]
testNetwork = Library.Network(testNetworkLayerSizes)
testNetwork.save()

print(Library.networkData)

print(testNetwork.exe(testInputs))

print("Break")