import argparse
import os

from constants import SOLUTION_FILE_NAME


def create_file_path(task_dir, file_name):
    """
    Create a file path
    :param task_dir: Directory where the file is located
    :param file_name: Name of the file
    :return: str: File path
    """
    return os.path.join(task_dir, file_name)


def create_solution_file(task_name, task_dir):
    """
    Create a solution file with a function definition
    :param task_name: name of the task
    :param task_dir: directory where the task is located
    :return:
    """
    solution_file = create_file_path(task_dir, SOLUTION_FILE_NAME)

    solution_code = f"""def {task_name}(*args, **kwargs):
        \"\"\"{task_name}\"\"\"
        pass
    """

    with open(solution_file, "w") as f:
        f.write(solution_code)


def create_test_solution_file(task_name, task_dir):
    """
    Create a test file with a test cases
    :param task_name: name of the task
    :param task_dir: name of the directory where the task is located
    :return:
    """
    test_file = create_file_path(task_dir, f"test_{task_name}")
    test_case_name = "".join([word.capitalize() for word in task_name.split("_")])
    # content for test_is_palindrome.py
    test_code = f"""import unittest
    from .solution import {task_name}


    class Test{test_case_name}(unittest.TestCase):
        def test_{task_name}(self):
            # add actual test cases here
            self.assertTrue({task_name}(args, kwargs))
            self.assertFalse({task_name}(args, kwargs))


    if __name__ == "__main__":
        unittest.main()
    """

    with open(test_file, "w") as f:
        f.write(test_code)


def create_readme_file(task_name, task_dir):
    """
    Create a README file with a task description
    :param task_name: name of the task
    :param task_dir: directory where the task is located
    :return:
    """
    readme_file = create_file_path(task_dir, "README.md")

    readme_content = f"""# Task: {task_name}

    ## Description
    {task_name}

    ### Example:
    - Input: \"\"  
    - Output:  

    ### Solution
    The function uses 
    """

    with open(readme_file, "w") as f:
        f.write(readme_content)

def create_init_file(task_dir):
    """
    Create an __init__.py file in the task directory
    :param task_dir: directory where the task is located
    :return:
    """
    init_file = create_file_path(task_dir, "__init__.py")
    with open(init_file, "w") as f:
        f.write("")


def create_task(task_name, directory):

    task_dir = os.path.join(directory, f"task_{task_name}")
    os.makedirs(task_dir, exist_ok=True)
    create_solution_file(task_name, task_dir)
    create_test_solution_file(task_name, task_dir)
    create_readme_file(task_name, task_dir)
    create_init_file(task_dir)
    print(f"Task {task_name} created in {task_dir}.")


def main():
    parser = argparse.ArgumentParser(description="Manage tasks for Python challenges")
    subparsers = parser.add_subparsers(dest="command")

    # parser for the 'new-task' command
    task_parser = subparsers.add_parser("new-task", help="Create a new task")
    task_parser.add_argument("task_name", help="Name of the task to create")
    task_parser.add_argument("-d", "--directory", required=True, help="Directory where the task will be created")

    args = vars(parser.parse_args())
    command = args.pop("command")

    if command == "new-task":
        create_task(**args)
    else:
        print("Unknown command. Use 'new-task' to create a task.")


if __name__ == "__main__":
    main()
