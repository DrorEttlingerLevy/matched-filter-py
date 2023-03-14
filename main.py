# main script entry point
import matched_filter.main as matf
import signal_generator as sg

def main():

    filter_impulse_response, input_signal = sg.generate_signals()

    y = matf.matched_filter(input_signal, filter_impulse_response)

    threshold = matf.compute_threshold(input_signal, len(filter_impulse_response))
    print(threshold)

    peak = max(y)
    print(peak)

    print(peak > threshold)


if __name__ == '__main__':
    main()
    