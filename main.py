def main():
	input_filename1 = "input1.txt"
	input_filename2 = "input2.txt"
	output_filename1 = "output1.txt"
	output_filename2 = "output2.txt"

	with open(input_filename1, 'r', encoding='utf-8') as file1, \
		open(input_filename2, 'r', encoding='utf-8') as file2, \
		open(output_filename1, 'w', encoding='utf-8') as out1, \
		open(output_filename2, 'w', encoding='utf-8') as out2:

		line1 = file1.readline().strip()
		line2 = file2.readline().strip()

		prev_line1 = None
		prev_line2 = None

		while line1 or line2:
			if line1 and line1 == prev_line1:
				line1 = file1.readline().strip()
				continue
			if line2 and line2 == prev_line2:
				line2 = file2.readline().strip()
				continue

			if not line2 or (line1 and line1 < line2):
				out1.write(line1 + "\n")
				prev_line1 = line1
				line1 = file1.readline().strip()

			elif not line1 or (line2 and line1 > line2):
				out2.write(line2 + "\n")
				prev_line2 = line2
				line2 = file2.readline().strip()

			else:  # line1 == line2 (совпадает в обоих файлах, не записываем)
				prev_line1 = line1
				prev_line2 = line2
				line1 = file1.readline().strip()
				line2 = file2.readline().strip()

if __name__ == "__main__":
	main()
