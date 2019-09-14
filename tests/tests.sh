# Simple tests for early debugulator functionality

# Note: run "alias debugulate='bash debugulate_wrapper'" for actual use

# relative to <root>/tests/, without standard ending '_input.py'
TEST_FILE_ARRAY=(
    "00_empty_file/empty_file"
    "01_comment_only/comment_only"
    "01_comment_only/comment_with_newline"
    "02_single_trivial_function/one_liner_to_return"
)

OVERALL_TEST_EXIT_STATUS=  # blank represents test not completed.
for INPUT_FILE in ${TEST_FILE_ARRAY[@]}
do
    INPUT_FILE_FULL_NAME="tests/${INPUT_FILE}_input.py"
    OUTPUT_FILE_FULL_NAME="tests/${INPUT_FILE}_input_processed.py"
    EXPECTED_OUTPUT="tests/${INPUT_FILE}_output.py"

    # Apply debugulator to the file:
    bash debugulate_wrapper ${INPUT_FILE_FULL_NAME} "Hello world" 10
    # TODO: add extra checking step to test output file is even generated.

    # Check the resulting output is the same as the expected one in each case:
    diff ${OUTPUT_FILE_FULL_NAME} ${EXPECTED_OUTPUT} >&2  # send to STDOUT
    DIFF_ON_OUTPUTS=$?
    if [ ${DIFF_ON_OUTPUTS} != 0 ]
    then
	echo "Test for file '${INPUT_FILE_FULL_NAME}' failed."
    fi
    # Add the exit statuses; if all sub-tests pass the sum is zero for an
    # overall pass:
    OVERALL_TEST_EXIT_STATUS=$(($OVERALL_TEST_EXIT_STATUS + $DIFF_ON_OUTPUTS))
done

if [ ${OVERALL_TEST_EXIT_STATUS} == 0 ]
then
    echo "Test battery passed."
else
    echo "Test battery failed."
fi
