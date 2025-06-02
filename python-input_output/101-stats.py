#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    """Print the statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    status_codes = {
            200: 0, 301: 0, 400: 0, 401: 0,
            403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            # Extract file size
            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            # Extract status code
            try:
                status_code = int(parts[-2])
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except (IndexError, ValueError):
                pass

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Print stats on keyboard interrupt
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
