from scipy.signal import butter, sosfiltfilt
from sciprs import signal_sosfiltfilt
import numpy as np
import matplotlib.pyplot as plt

# Here is a small snippet of some raw data
raw = np.array([0.0, 0.09414586007215595, 0.18745540640340155, 0.27909975437050305, 0.3682648115914595])

# Butterworth sosfiltfilt the data
buttersos = butter(4, [10, 50], btype='bandpass', output='sos', fs=1666)
sciprs_filtered = signal_sosfiltfilt(buttersos, raw, 0)
scipy_filtered = sosfiltfilt(buttersos, raw)

# Plot the signal and the difference between the methods
fig, axs = plt.subplots(2, 1, sharex=True)
axs[0].plot(raw, label="raw", marker='o')
axs[0].plot(sciprs_filtered, label="python+rust", marker='^')
axs[0].plot(scipy_filtered, label="python+rust", marker='^')
axs[1].plot([a - b for (a, b) in zip(scipy_filtered, sciprs_filtered)], label = "Difference f64")
axs[0].legend()
axs[1].legend()
plt.show()

# Some rudamentary benchmarks
"""
>>> sciprs_time = timeit.timeit(lambda: sciprs.signal_sosfiltfilt(buttersos, asdf100, 0), number=1000)
>>> scipy_time = timeit.timeit(lambda: sosfiltfilt(buttersos, asdf100), number=1000)
>>> sciprs_time / scipy_time
0.450365636957239
>>> asdf1000 = np.repeat(asdf, 1000)
>>> sciprs_time = timeit.timeit(lambda: sciprs.signal_sosfiltfilt(buttersos, asdf1000, 0), number=100)
>>> scipy_time = timeit.timeit(lambda: sosfiltfilt(buttersos, asdf1000), number=100)
>>> sciprs_time / scipy_time
0.4961199499800506
>>> asdf.shape
(16660,)
"""