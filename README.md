# HelloActions-AndrewHaralambous

Andrew Haralambous | SWE 525, W1 | Lab 11

Repository: https://github.com/aharalam/HelloActions-AndrewHaralambous

This project demonstrates a Python program running inside GitHub Actions.
The workflow runs automatically on pushes to `main` and can also be started manually.

## Files

- `hello.py`: Reads `WHO_TO_GREET`, uses `GitHub Actions Student` when the variable is unavailable, and prints two messages.
- `.github/workflows/hello.yml`: Commented workflow that checks out the source, sets up Python 3.13, tests the program, and runs it.
- `test_hello.py`: Two standard-library tests that execute the actual script with a supplied name and with the variable missing.

## Run locally

Python 3.13 is used in the workflow. No external packages are needed.

```text
python hello.py
python -B -m unittest discover -v
```

With `WHO_TO_GREET` unset, the program prints:

```text
Hello GitHub Actions Student!
This program is running inside GitHub Actions.
```

To choose a different name in PowerShell:

```powershell
$env:WHO_TO_GREET = 'Andrew Haralambous'
python hello.py
Remove-Item Env:WHO_TO_GREET
```

The second line is the assignment's required message. Running the same script locally also prints that message.

## Automatic and manual execution

For automatic execution, change the source or this README, commit, and push to `main`.
Open **Actions → Hello World with Python**, select the latest push run, open
**Run the Python Hello World program**, and expand **Run the Python program**.
Confirm that both output lines appear and the run succeeds.

For manual execution, open **Actions → Hello World with Python → Run workflow**,
choose `main`, and select **Run workflow**. Open the resulting manual run and
inspect the same job and output step. GitHub documents manual execution
[here](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow).

## Workflow explanation

1. **What is the purpose of `on`?** 
	It specifies the events that trigger the workflow. In this project, those events are a push to `main` and manual execution.
	
2. **What does `workflow_dispatch` do?** 
	It allows manual, on-demand execution of the workflow using the **Run workflow** button.
	
3. **What does `runs-on` specify?** 
	It specifies the runner that executes the job. A runner is a server with the GitHub Actions runner application installed. Here, `ubuntu-latest` selects a GitHub-hosted Ubuntu virtual machine.
	
4. **Why is `actions/checkout` needed?** 
	It downloads the repository's source code into the runner's environment so the job can use our program and tests.
	
5. **What does the language setup action do?** 
	It prepares the environment for the selected programming language. Our workflow uses `actions/setup-python` to set up Python 3.13 before testing and running the program.
	
6. **What is the difference between compiling and running?** 
	Compiling translates source code into another form, such as the Java bytecode shown in class. Running executes the program. For our Python program, we use `python hello.py` without a separate compilation step.
	
7. **Where can you see the program output?** 
	Open the workflow run in the **Actions** tab, select the job, and expand the **Run the Python program** step to see its output in the workflow log.
	
8. **What is the difference between a workflow, a job, and a step?** 
	A workflow is a configurable automated process made up of one or more jobs. Each job contains steps and runs on a runner. A step performs a task by using an action with `uses` or running a shell command with `run`.

## Optional challenge: add a test step

The **Test the greeting program** step runs `python -B -m unittest discover -v`
before the program step. The tests verify both an environment-provided name and
the default when `WHO_TO_GREET` is unavailable. A failure fails the job and
prevents the following program step from running under the default step behavior.

## AI-use statement

I used AI assistance to help draft the Python program, and automated tests. Local verification was performed with automated tests. GitHub run results and screenshots are documented separately for submission evidence.