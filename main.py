# main script entry point
import matched_filter.main as matf
import signal_generator as sg

def main():

    filter_impulse_response, input_signal, noise_power = sg.generate_signals()

    y = matf.matched_filter(input_signal, filter_impulse_response)

    threshold = matf.compute_threshold(noise_power)
    print(f"threshold: {threshold}")

    peak = max(y)
    print(f"output peak: {peak}")

    if peak > threshold:
        print("Reference signal detected in noisy input signal")
    else:
        print("Signal not detected")

    sg.read_signal()


if __name__ == '__main__':
    main()
    