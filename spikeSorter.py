import numpy as np
import rhd
from scipy.io import loadmat
# To keep memory usage down, use argument no_floats=True.
# Otherwise, data is loaded as floating point arrays
# (4x the space required).
import quickspikes as qs
np.set_printoptions(threshold=np.inf)

data = loadmat('./bp_freeform.mat')

samples=data['data'][:2000]
print(samples.shape)
binary_sample=np.zeros([200,84])
for i in range(len(samples[0])):
    sample=samples[:,i]
# print(samples[10:20,10:20])
    det = qs.detector(2000, 20)
    times = det.send(sample)
    # print(times)
    for j in range(len(times)):
        binary_sample[int(times[j]/10),i]=1
print(binary_sample)
# import matplotlib.pyplot as plt
# plt.plot(data['amplifier_data'][:,:1000].T)
# plt.show()

# data = rhd.read_data("E:/DATA/RHD/1_221219_151613.rhd", no_floats=True)
