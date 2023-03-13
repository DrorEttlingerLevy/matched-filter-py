import numpy as np

def generate_noisy_signal() -> np.ndarray:

    # Define parameters
    fs = 1000  # Sampling frequency
    f0 = 100   # Signal frequency
    snr = 10   # Signal-to-noise ratio
    duration = 1  # Signal duration in seconds

    # Generate a complex sinusoidal signal
    t = np.arange(0, duration, 1/fs)  # Time vector
    signal = np.exp(2j*np.pi*f0*t)

    # Generate white noise
    noise = np.random.normal(scale=1, size=len(signal))

    # Compute the power of the signal
    signal_power = np.sum(np.abs(signal)**2) / len(signal)

    # Compute the power of the noise
    noise_power = np.sum(np.abs(noise)**2) / len(noise)

    # Compute the scaling factor for the noise to achieve the desired SNR
    scale_factor = np.sqrt(signal_power / noise_power / (10**(snr/10)))

    # Add the noise to the signal
    noisy_signal = signal + noise * scale_factor

    return noisy_signal
