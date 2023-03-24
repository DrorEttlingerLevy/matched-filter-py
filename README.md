# matched-filter-py

This simple project feaetures a Python implementation of a matched filter for signal detection in the domain of frequency.
A matched filter is a signal processing filter used to detect the presence of a specific known signal (or pattern) in a noisy signal. It is called a "matched" filter because it is designed to match the expected signal pattern, so it is sensitive to the signal and insensitive to other noise-like signals. If the input signal contains the same waveform as the template, the output will be maximized. If the input signal contains a different waveform, the output will be minimized.

In this project, the matched filter is designed by computing the convolution of the two Fourier transforms of the input signal and the filter impulse response (the signal we wish to detect in the input noisy signal); the result of the convolution is then converted back in the time domain by computing its  inverse Fourier transform.

The matched filter maximized the output if the desider waveform is present in the input signal. That said, to determine if the desired waveform is present, the peak of the output of the matched filter is obtained and is compared to a given threshold: if the peak is greater than the threshold, it is assumed that the waveform is present.

For reference: [Matched Filter](https://en.wikipedia.org/wiki/Matched_filter)

# Usage
The program can be simply executed with:
```
python main.py -f [path to input file]
```
from the main folder. Here some example input files are provided in the `/signal` folder.

For testing the case of unsuccesful detection, uncomment the following lines in `signal_generator.py`:
```
    # random_signal = np.random.normal(scale=1, size=len(time))
    # random_signal = random_signal + noise * scale_factor
```
and then make the function return `random_signal` instead of `noisy_signal`.

# Output
The program plots the reference signal and its noisy version, then outputs a message of succesful or unsuccesful detection.
