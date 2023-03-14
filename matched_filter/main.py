import numpy as np

def compute_threshold(input_signal, filter_length):
    print('Computing threshold...')
    print(len(input_signal), filter_length)
    portion = input_signal[:filter_length]
    std = np.std(portion)
    return std


def matched_filter(s, h):
    diff = len(s) - len(h) # We assume that len(s) >= len(h)

    # Zero-padding of the input signal
    h = np.pad(h, (0, diff), 'constant')

    # Compute the Fourier transform of padded_input and padded_filter
    S = np.fft.fft(s)
    H = np.fft.fft(h)

    # Compute the convolution of the two Fourier transforms
    Y = S * H

    # Compute the inverse Fourier transform of Y to obtain the time-domain output signal y
    y = np.fft.ifft(Y)

    return y
