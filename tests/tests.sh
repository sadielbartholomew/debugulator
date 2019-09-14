# Simple tests for early debugulator functionality

## FIRST MAKE CASE WHERE CAN DO A 'DRY RUN' WHERE CHANGES TO ANOTHER FILE


# Whatever line specify, should give the same result (there are 0 lines here,
# but it will be appended to the final line if specify line number out of range
python debugulator.py tests/00_empty_file/empty_file_input.py "Hello world" 4
#python debugulator.py tests/00_empty_file/empty_file.py "Hello world" 4

### START

# relative to <root>/tests/, without standard ending '_input.py'
TEST_FILE_ARRAY=(
    "00_empty_file/empty_file"
    "01_comment_only/comment_only"
    "01_comment_only/comment_with_newline"
    "02_single_trivial_function/one_liner_to_return"
)


for INPUT_FILE in ${TEST_FILE_ARRAY[@]}
do
    INPUT_FILE_FULL_NAME="tests/${INPUT_FILE}_input.py"
    # python debugulator.py ${INPUT_FILE_FULL_NAME} "Hello world" 4
    # ...
done
