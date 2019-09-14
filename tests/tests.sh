# Simple tests for early debugulator functionality

## FIRST MAKE CASE WHERE CAN DO A 'DRY RUN' WHERE CHANGES TO ANOTHER FILE

# Tests files list:
#
# 00_empty_file/empty_file_input.py
# 01_comment_only/comment_only.py
# 01_comment_only/comment_with_newline_only.py
# 02_single_trivial_function/one_liner_to_return.py

# test that 00_empty_file returns marker then comment...

# Whatever line specify, should give the same result (there are 0 lines here,
# but it will be appended to the final line if specify line number out of range
python debugulator.py tests/00_empty_file/empty_file_input.py "Hello world" 4
#python debugulator.py tests/00_empty_file/empty_file.py "Hello world" 4

for input_file in file1 file2 file3
do
	command1 on $VARIABLE
	command2
	commandN
done
