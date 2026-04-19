# How to make requirements
When the user requests for requirements for their code use the following method :

### 1. List the files
Use the `list` action to list the files in the project.
<action_list>
path=./
</action_list>

### 2. Read the target file or files
Use the `read` action to read the files in the project.
<action_read>
path=./path/to/file
</action_read>

### 3. Create the requirements.txt file
Use the `create` action to create the requirements.txt file.
<action_create>
path=./requirements.txt
contains=<content>
</action_create>

### Important
The user may specific a file or multiple files, make sure to read all of them.