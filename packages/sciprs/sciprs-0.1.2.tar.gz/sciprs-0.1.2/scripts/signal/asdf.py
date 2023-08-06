from sciprs.signal import sosfiltfilt
import numpy as np

print(sosfiltfilt(np.zeros((1, 6), dtype='f8'), np.zeros((50,2)), axis = 0))