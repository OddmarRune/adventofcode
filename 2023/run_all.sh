#!/bin/bash

# Function to execute scripts in the current directory
execute_scripts() {
    for script in *.py *.sh; do
        if [ -f "$script" ]; then
            echo "Executing script: $script"
            
            # Check the file extension and execute accordingly
            if [[ "$script" == *.py ]]; then
                python "$script"
            elif [[ "$script" == *.sh ]]; then
                bash "$script"
            fi
	    echo
        fi
    done
}

# Main function to traverse subdirectories
traverse_directories() {
    for dir in */; do
        if [ -d "$dir" ]; then
            echo "Entering directory: $dir"
            cd "$dir" || exit

            # Execute scripts in the current directory
            execute_scripts

            # Move back to the parent directory
            cd ..
        fi
    done
}

# Start traversal from the initial directory
traverse_directories

