# main script entry point
import matched_filter.main as matf
import signal_generator as sg

def main():

    input_signal = sg.generate_signal(noisy = True)
    filter_impulse_response = sg.generate_signal()

    threshold = 0.9

    y = matf.matched_filter(input_signal, filter_impulse_response)

    peak = max(y)

    print(peak > threshold)


if __name__ == '__main__':
    main()