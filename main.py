
# Import the necessary packages
import matplotlib.pyplot as plt
import numpy as np

# For replicability
np.random.seed(101)

# Exercise 1_1
# Our goal is to generate and analyse spike times using a Poisson spike generator with a
# constant rate of 100 Hz. In other words, a homogeneous Poisson point process. We
# additionally need to obtain the inter-spike interval distribution and then calculate the
# Fano factor and the coefficient of variation

T = 100  # total time, seconds
r = 100  # firing rate, Hz
time_step = 0.001  # seconds
time_vector_max = int(T/time_step)
time_vector = np.arange(0, time_vector_max)
rt = time_step*r

# Generate the spikes using the native Poisson pdf function
spikes = np.random.poisson(lam=rt, size=time_vector_max)
spikes[spikes > 1] = 1

# Obtain the spike times
spike_times = time_vector[spikes == 1]

# Generate the inter-spike interval data
t_isi = np.diff(spike_times)

# Plot the inter-spike interval data
plt.hist(t_isi, bins=30)
plt.xlim(left=0)
plt.title("Inter-spike interval data")
plt.xlabel("Time [ms]")
plt.ylabel("Count")

mean_t_isi = np.mean(t_isi)
std_t_isi = np.std(t_isi)
var_t_isi = std_t_isi**2
C_v = std_t_isi/mean_t_isi

# Calculate the Fano for 1 ms window
Fano_1ms = (np.std(spikes)**2)/np.mean(spikes)

k = 100
counts = []
for i in range(1, int(len(spikes)/k+1)):
    counts.append(sum(spikes[(i-1)*k:(i*k)]))

# Calculate the Fano for 100 ms window
Fano_100ms = np.var(counts)/np.mean(counts)


print(f"The coefficient of variation of the inter-spike intervals is {C_v:.3f} and "
      f"the Fano factors of the spike counts when the bin size is 1 ms is {Fano_1ms:.3f} and "
      f"{Fano_100ms:.3f} for when it is 100 ms")
plt.show()


