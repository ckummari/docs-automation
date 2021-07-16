#importing the regex module
import re

#defining the replace method
def requirements_replace(filePath, text, subs, flags=0):
    with open(file_path, "r+") as file:
        #read the file contents
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)

file_path="README.md"
text="## Requirements"
subs="<details><summary>## Requirements</summary>"
#calling the replace method
requirements_replace(file_path, text, subs)

#defining the replace method
def providers_replace(filePath, text, subs, flags=0):
    with open(file_path, "r+") as file:
        #read the file contents
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)

file_path="README.md"
text="## Providers"
subs="<details><summary>## Providers</summary>"
#calling the replace method
providers_replace(file_path, text, subs)

#defining the replace method
def modules_replace(filePath, text, subs, flags=0):
    with open(file_path, "r+") as file:
        #read the file contents
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)

file_path="README.md"
text="## Modules"
subs="<details><summary>## Modules</summary>"
#calling the replace method
modules_replace(file_path, text, subs)


#defining the replace method
def resources_replace(filePath, text, subs, flags=0):
    with open(file_path, "r+") as file:
        #read the file contents
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)

file_path="README.md"
text="## Resources"
subs="<details><summary>## Resources</summary>"
#calling the replace method
resources_replace(file_path, text, subs)


#defining the replace method
def inputs_replace(filePath, text, subs, flags=0):
    with open(file_path, "r+") as file:
        #read the file contents
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)

file_path="README.md"
text="## Inputs"
subs="<details><summary>## Inputs</summary>"
#calling the replace method
inputs_replace(file_path, text, subs)


#defining the replace method
def outputs_replace(filePath, text, subs, flags=0):
    with open(file_path, "r+") as file:
        #read the file contents
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)

file_path="README.md"
text="## Outputs"
subs="<details><summary>## Outputs</summary>"
#calling the replace method
outputs_replace(file_path, text, subs)
