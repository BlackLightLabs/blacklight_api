#!/bin/bash

# Find all python files recursively in the current directory and its subdirectories
python_files=$(find . -name "*.py")

# Find all docker files recursively in the current directory and its subdirectories
docker_files=$(find . -name "Dockerfile" -o -name "docker-compose.yml")

# Find all .env files recursively in the current directory and its subdirectories
env_files=$(find . -name ".env")

# Find all .dockerignore files recursively in the current directory and its subdirectories
dockerignore_files=$(find . -name ".dockerignore")

# Create a new file called "prompt.txt"
touch prompt.txt

# Loop through each python file and append its contents to "prompt.txt" with a header
for file in $python_files
do
    echo "$file" >> prompt.txt
    echo "==========" >> prompt.txt
    cat "$file" >> prompt.txt
    echo "" >> prompt.txt
done

# Loop through each docker file and append its contents to "prompt.txt" with a header
for file in $docker_files
do
    echo "$file" >> prompt.txt
    echo "==============" >> prompt.txt
    cat "$file" >> prompt.txt
    echo "" >> prompt.txt
done

# Loop through each .env file and append its contents to "prompt.txt" with a header
for file in $env_files
do
    echo "$file" >> prompt.txt
    echo "==============" >> prompt.txt
    cat "$file" >> prompt.txt
    echo "" >> prompt.txt
done

# Loop through each .dockerignore file and append its contents to "prompt.txt" with a header
for file in $dockerignore_files
do
    echo "$file" >> prompt.txt
    echo "==============" >> prompt.txt
    cat "$file" >> prompt.txt
    echo "" >> prompt.txt
done

# Ask the user for a question to append to the end of the file
read -p "Enter a question to append to the end of the file: " question

# Add the question to the end of the file
echo "" >> prompt.txt
echo "Given the python project above as context code, $question" >> prompt.txt