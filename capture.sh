#!/bin/bash

PYTHON_FILE=./save_capture.py


while :
do
	echo "============= capture ============="
	printf "1: %-10s\n" "start capture program"
	echo "q: to quit"
	echo "==============================="
	echo "choose index number: "
	printf "> "
	read INDEX

	if [ "$INDEX" = "1" ]; then
		while :
		do
			echo "========== Scripts list =========="
	       		printf "1: %-10s\n" "CAPTURE PAGE"
        		printf "2: %-10s\n" "MODIFY PARAMETER"
		        echo "q: TO QUIT"
       			echo "==============================="
	       		echo "choose index number: "
	       		printf "> "
			read INDEX2
			
    			if [ "$INDEX2" = "1" ]; then
				echo "page: "
				printf "> "
				read PAGE
				python3 $PYTHON_FILE -p $PAGE

			elif [ "$INDEX2" = "2" ]; then
				echo "example -> -p {page} -c {0} -r {0}"
				echo "parameter: "
				printf "> " 
				read PARAMS
				python3 $PYTHON_FILE $PARAMS
       			else
               		 	break
        		fi
		done
		
	elif [ "$INDEX" = "q" ]; then
        	exit
	else
        	echo "Invalid input. Please enter a valid index or 'q' to quit."
		continue
	fi
done	

