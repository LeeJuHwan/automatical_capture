#!/bin/bash

PROJECTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_FILE=$PROJECTDIR/src/save_capture.py

echo PTYHON FILE PATH: "[ $PYTHON_FILE ]" file excution

OS="`uname`"
case $OS in
	"Linux")
		OS="Linux"
		;;
  	"MINGW32")
    	OS="Windows"
    	;;
  	"MINGW64")
		OS="Windows"
    	;;
	"Darwin") 
    	OS="Mac"
    	;;
esac

echo "user OS: $OS"

while :
do
	echo "============= [$OS OS] capture ============="
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
	       		printf "1: %-10s\n" "PROGRAM EXECUTE"
        		printf "2: %-10s\n" "MODIFY PARAMETER"
		        echo "q: TO QUIT"
       			echo "==============================="
	       		echo "choose index number: "
	       		printf "> "
			read INDEX2
			
    			if [ "$INDEX2" = "1" ]; then
				echo "get start program"
				python3 $PYTHON_FILE

			elif [ "$INDEX2" = "2" ]; then
				echo "example -> -t {1} -c {0} -r {0}"
				echo "c: 프로그램을 실행 한 후 설정한 시간 만큼 대기 하며 초를 기준으로 합니다. 기본 값은 1초입니다."
				echo "c: 캡쳐한 이미지를 PDF로 변환 할지 결정합니다. 기본값은 1이며 자동 변환 됩니다."
				echo "r 캡쳐한 이미지들을 삭제할지 결정합니다. 기본값은 1이며 모두 삭제 됩니다."
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
