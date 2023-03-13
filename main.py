# main script entry point
import matched_filter.main as matf
import signal_generator as sg

def main():

    noisy_signal = sg.generate_noisy_signal()

    print(noisy_signal)


if __name__ == '__main__':
    main()