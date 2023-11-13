with open("Python100daycode/Day26/Data_overlap/file1.txt") as File:
    file1 = File.readlines()
    file1 = [int(num.strip()) for num in file1]

with open("Python100daycode/Day26/Data_overlap/file2.txt") as File:
    file2 = File.readlines()
    file2 = [int(num.strip()) for num in file2]

common_numbers = [num for num in file1 if num in file2]
print(common_numbers)