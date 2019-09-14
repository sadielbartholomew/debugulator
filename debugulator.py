"""
Debugulator, created by Sadie Bartholomew, 2019.
"""

# TODO: diffs:
# import difflib
import os.path
import sys


DEBUGULATOR_COMMENT_MARK = "# <<<DBGL8R"


def insert_line_to_script(
        script_path, line_to_insert, append_at_line_number, overwrite=False,
        prev_copy=False):
    """ DOCSTRING. """
    if prev_copy:
        script_name = (os.path.splitext(os.path.basename(script_path))[0] +
                       "_processed" +
                       os.path.splitext(os.path.basename(script_path))[1])
        script_path = os.path.join(
            os.path.dirname(script_path), script_name)
        overwrite = True  # as we overwrite the old copied file.
    with open(script_path, "r+") as script:
        script_contents = script.readlines()

        # Manage the line to insert.
        append_at_line_number = int(append_at_line_number)
        script_contents.insert(append_at_line_number, "%s\n" % line_to_insert)

        new_script_contents = "".join(script_contents)

        if overwrite:  # Warning: overwrites the file with some new lines. Care!
            script.seek(0)
            script.write(new_script_contents)
            script.close()  # needed because of seek?
            return

    # "else:" case as above: don't overwrite input file, instead use separate
    # one in the same directory, with same name but "processed_" appended.
    script_name = os.path.basename(script_path)
    if not prev_copy:
        script_name = (os.path.splitext(script_name)[0] + "_processed" +
                       os.path.splitext(script_name)[1])
    copied_script_path = os.path.join(os.path.dirname(script_path), script_name)
    with open(copied_script_path, "w") as copied_script:
        copied_script.seek(0)
        copied_script.write(new_script_contents)
        copied_script.close()
        return


def main():
    # Note debugulator comment marks will appear with all changes for tracing.
    
    # Check arguments are valid.
    if len(sys.argv) < 4:  # counted from 'python' here, so 4 not 3
        raise IndexError("Please provide: a script (argument 1), a clause to " +
                         "add in a print function within it (2) and a line " +
                         "number at which to append them (3).")

    # Add the lines as requested by the user, but without overwriting for now.
    user_print_statement = ("print('" + sys.argv[2] + "') " +
                            DEBUGULATOR_COMMENT_MARK)
    script = sys.argv[1]
    insert_line_to_script(script, user_print_statement, sys.argv[3])

    # Add an general mark to indicate that debugulator has changed the script.
    # Note: do this after the above changes so it is always on very first line.
    # 'prev_copy' option specifies that a copy has already been made, so we
    # know to continue with same copy to retain changes from previous calls.
    insert_line_to_script(
        script, DEBUGULATOR_COMMENT_MARK + ">>>", 0, prev_copy=True)


main()
