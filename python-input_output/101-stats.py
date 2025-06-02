#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:"""
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
            try:
                parts = line.split()
                # File size is last element
                total_size += int(parts[-1])
                # Status code is second to last
                status_code = int(parts[-2])
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except (IndexError, ValueError):
                continue

            # Print stats every 10 lines or at end
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        # Print final stats if not on a 10-line boundary
        if line_count % 10 != 0:
            print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
