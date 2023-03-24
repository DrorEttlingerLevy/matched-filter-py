import numpy as np
import matplotlib.pyplot as plt

def generate_signals():

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
    print(f"noise power: {noise_power}")

    # Compute the scaling factor for the noise to achieve the desired SNR
    scale_factor = np.sqrt(signal_power / noise_power / (10**(snr/10)))

    # Add the noise to the signal
    noisy_signal = signal + noise * scale_factor

    # plt.figure()
    # plt.plot(t, noisy_signal)
    # plt.show()

    # random_signal = np.random.normal(scale=1, size=len(t))
    # random_signal = random_signal + noise * scale_factor

    return signal, noisy_signal, noise_power
    

def read_signal():
    with open('signal_4k.txt', 'r') as file:
        contents = file.read()
    
    signal = [float(x) for x in contents.split()]

    time = [t for t in range(len(signal))]

    # Close the file
    file.close()

    noise = np.random.normal(scale=1, size=len(signal))

    # Compute the power of the signal
    signal_power = np.sum(np.abs(signal)**2) / len(signal)

    # Compute the power of the noise
    noise_power = np.sum(np.abs(noise)**2) / len(noise)

    scale_factor = np.sqrt(signal_power / noise_power / (10**(10/10)))

    # Add the noise to the signal
    noisy_signal = signal + noise * scale_factor

    fig, (ax1, ax2) = plt.subplots(2, 1)

    ax1.plot(time, signal)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Clean Signal Amplitude')
    ax1.set_title('Clean Signal Plot')

    ax2.plot(time, noisy_signal)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Noisy Signal Amplitude')
    ax2.set_title('Noisy Signal Plot')

    plt.tight_layout()
    plt.show()