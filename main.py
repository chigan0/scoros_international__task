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
	
		while line1 or line2:
			if not line2 or (line1 and line1 < line2):
				out1.write(line1 + "\n")  # Write down in output1.txt
				line1 = file1.readline().strip()
			
			elif not line1 or (line2 and line1 > line2):
				out2.write(line2 + "\n")  # Write down in output2.txt
				line2 = file2.readline().strip()
			
			else:  # line1 == line2
				line1 = file1.readline().strip()
				line2 = file2.readline().strip()

if __name__ == "__main__":
	main()
