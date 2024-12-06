[![codecov](https://codecov.io/github/rdchvd/py-practice/graph/badge.svg?token=F13LJO0BFX)](https://codecov.io/github/rdchvd/py-practice)
# Python Practice Tasks  

This repository contains my Python practice tasks, sourced from platforms like Codewars, LeetCode, and other problem-solving sites. It’s organized to make each task easily navigable, with solutions and tests for each challenge.  

## Features  

### 1. **Task Categorization**  
Each task resides in its own directory, containing:  
- A solution file (`solution.py`)  
- A test file (`test_task_name.py`)  
- A detailed README with the task description, examples, and test results  

### 2. **Automated Testing**  
- GitHub Actions ensures all tests are executed for every push or pull request.  
- `tox` is used for running tests and generating coverage reports.  


## Setup  

To set up the project locally:  

1. Clone the repository:  
   ```bash
   git clone https://github.com/rdchvd/py-practice.git
   cd py-practice
   ```
2. Activate a virtual environment:  
   ```bash
   python3 -m venv .venv  
   source .venv/bin/activate  # on Windows: .venv\Scripts\activate
   ```
3. Install the project dependencies:  
   ```bash
    pip install -r requirements.txt
    ```
4. Run the tests:
    ```bash
    tox
    ```
## Adding a New Task

To create a new task, use the manage.py script:
   ```bash
   make new-task task=some_task_name dir=some_dir
```
This will create a new folder under the specified category with boilerplate files:
 - `solution.py` - for the task solution code 
 - `test_solution.py` - for the task test code
 - `README.md` - for the task description, examples, and test results