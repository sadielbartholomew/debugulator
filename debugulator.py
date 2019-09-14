"""
Debugulator, created by Sadie Bartholomew, 2019.
"""

import sys
import difflib


DEBUGULATOR_COMMENT_MARK = "# <<<DBGL8R"


def insert_line_to_script(script_path, line_to_insert, append_at_line_number):
    with open(script_path, "r+") as script:
        script_contents = script.readlines()
        append_at_line_number = int(append_at_line_number)
        if append_at_line_number != 0:
            line_to_insert = "\n" + line_to_insert
        script_contents.insert(append_at_line_number, "%s\n" % line_to_insert)
        new_script_contents = "".join(script_contents)
        script.seek(0)
        script.write(new_script_contents)
        script.close()


def main():
    # Note debugulator comment marks must appear with all changes for tracing.
    
    # Check arguments are valid
    if len(sys.argv) < 3:
        print("Please provide: a script (arg1), line(s) to add to it (arg2)" +
              "and a line number at which to append them (arg3).")

    # Add the lines as requested by the user
    user_print_statement = ("print('" + sys.argv[2] + "') " +
                            DEBUGULATOR_COMMENT_MARK)
    insert_line_to_script(sys.argv[1], user_print_statement, sys.argv[3])
    
    # Add an general mark to indicate that debugulator has changed the script.
    # Note: do this after the above changes so it is always on very first line
    insert_line_to_script(sys.argv[1], DEBUGULATOR_COMMENT_MARK + ">>>", 0)

main()
