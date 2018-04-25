from sys import stdin
import pickle

def main():
	amrs = {}

	for line in stdin:
		if line[0:5] == "# AMR":
			corpus = line.split()[4]
			section = line.split()[6]
		elif not line.split():
			new


if __name__ == '__main__':
	main()