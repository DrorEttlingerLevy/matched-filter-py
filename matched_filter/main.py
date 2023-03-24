import numpy as np

def compute_threshold(s, h):
    print('Computing threshold...')

    s_energy = np.sum(np.square(s))
    h_energy = np.sum(np.square(h))

    inner_product = np.dot(s, h)

    s_1 = s_energy - inner_product
    h_1 = inner_product - h_energy

    print(s_1, h_1)

    sum = s_1 + h_1

    threshold = sum / 2

    return threshold



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
