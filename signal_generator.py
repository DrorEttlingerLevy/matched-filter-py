import numpy as np

def generate_signal(noisy = False) -> np.ndarray:

    # Define parameters
    fs = 1000  # Sampling frequency
    f0 = 100   # Signal frequency
    snr = 10   # Signal-to-noise ratio
    duration = 1  # Signal duration in seconds

    # Generate a complex sinusoidal signal
    t = np.arange(0, duration, 1/fs)  # Time vector
    signal = np.exp(2j*np.pi*f0*t)

    if noisy:

        # Generate white noise
        noise = np.random.normal(scale=1, size=len(signal))

        # Compute the power of the signal
        signal_power = np.sum(np.abs(signal)**2) / len(signal)

        # Compute the power of the noise
        noise_power = np.sum(np.abs(noise)**2) / len(noise)

        # Compute the scaling factor for the noise to achieve the desired SNR
        scale_factor = np.sqrt(signal_power / noise_power / (10**(snr/10)))

        # Add the noise to the signal
        #noisy_signal = signal + noise * scale_factor

        # Add the signal to the noise at a certain point in time
        random_signal = np.random.normal(scale=1, size=len(t))
        signal_start_time = 0.5  # Time at which the signal starts
        signal_start_sample = int(signal_start_time * fs)  # Sample index at which the signal starts
        noisy_signal = np.concatenate((random_signal[:signal_start_sample], signal[:len(signal)-signal_start_sample] + noise[:len(signal)-signal_start_sample] * scale_factor, random_signal[signal_start_sample:]))

        return noisy_signal
    
    return signal
