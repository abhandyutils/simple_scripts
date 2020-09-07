#!/usr/bin/python3
"""This script simply helps to inspect the SHA256 checksum of downloaded files."""

import sys, os, re, argparse, subprocess

def inspect_checksum(file_path, provided_checksum, print_details=True):
	if not os.path.isfile(file_path):
		quit("\n*** ERROR: '" + file_path + "' is not a valid file path.\n")
	result = subprocess.run(["sha256sum", file_path], stdout=subprocess.PIPE)
	checksum_output = result.stdout.decode('ascii')
	file_checksum = checksum_output.split("\n")[0].split()[0]
	if print_details:
		valid_checksum_provided = provided_checksum == file_checksum
		print("FILEPATH: " + file_path)
		print("SHA256SUM (USER): " + str(provided_checksum))
		print("SHA256SUM (TOOL): " + file_checksum)
		print("USER CHECKSUM CORRECT?: " + str(valid_checksum_provided))
	return(file_checksum)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('file', type=str, help="Download Checksum Inspection")
	parser.add_argument('checksum', type=str, help="SHA256 checksum provided in website/source")
	args = parser.parse_args()

	inspect_checksum(args.file, args.checksum)
