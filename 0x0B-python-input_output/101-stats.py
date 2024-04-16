#!/usr/bin/env python3
"""Unique Log Parser"""

import sys

# Initialize variables to store total size and counts of HTTP status codes
total_size_bytes = 0
status_code_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                      '403': 0, '404': 0, '405': 0, '500': 0}
line_number = 0  # Track the number of lines processed


def print_statistics():
    """Prints a summary of the statistics."""
    print("Total File Size: {} bytes".format(total_size_bytes))
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))


try:
    # Read input lines from standard input (e.g., piped log file)
    for line in sys.stdin:
        # Split the line into parts using whitespace
        parts = line.split()
        if len(parts) >= 2:
            # Extract HTTP status code and update count
            tmp = line_number
            if parts[-2] in status_code_counts:
                status_code_counts[parts[-2]] += 1
                line_number += 1

            try:
                # Extract and add size of the request to total size
                total_size_bytes += int(parts[-1])
                # If no status code was encountered, still consider the line processed
                if tmp == line_number:
                    line_number += 1
            except ValueError:
                # If unable to extract size, skip to next line
                if tmp == line_number:
                    continue

        # Print statistics every 10 lines
        if line_number % 10 == 0:
            print_statistics()

    # Print final statistics
    print_statistics()

except KeyboardInterrupt:
    # In case of keyboard interrupt, print final statistics
    print_statistics()
