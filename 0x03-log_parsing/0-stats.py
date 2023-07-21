#!/usr/bin/python3
import sys

def print_stats(total_file_size, status_codes):
    """
    Function to print the current statistics
    """
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))

def main():
    """
    Main function
    """
    total_file_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    try:
        for i, line in enumerate(sys.stdin, 1):
            # Parse the log line to extract file size and status code
            parts = line.split()
            if len(parts) >= 7:
                status_code = parts[-2]
                file_size = int(parts[-1])

                # Update statistics
                total_file_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            # Print statistics after every 10 lines
            if i % 10 == 0:
                print_stats(total_file_size, status_codes)

    except KeyboardInterrupt:
        # Print the statistics when a keyboard interrupt (CTRL+C) is received
        print_stats(total_file_size, status_codes)

if __name__ == "__main__":
    main()
