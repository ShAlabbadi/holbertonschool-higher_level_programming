#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:"""


def print_stats(total_size, status_codes):
    """Print the statistics"""
    sorted_keys = sorted(status_codes.keys())
    print('\n'.join(["{:d}: {:d}".format(k, status_codes[k])
                     for k in sorted_keys if status_codes[k] != 0]))


if __name__ == "__main__":

    import sys

    try:
        total = 0
        status_codes = \
            {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
        for n, line in enumerate(sys.stdin, 1):
            words = line.split()
            total += int(words[-1])
            status_codes[int(words[-2])] += 1
            if n % 10 == 0:
                print("File size: {:d}".format(total))
                print_dict_sorted_nonzero(status_codes)
    finally:
        print("File size: {:d}".format(total))
        print_dict_sorted_nonzero(status_codes)
