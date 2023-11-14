# Try to alert that new messages were just written to the ERRORS file.
if [ $(wc -l < $FLASHTEST_BASE/ERROR) -ne 0 ]; then
	echo "WARNING: $FLASHTEST_BASE/ERROR appears to have some new messages."
	echo "         Here are the last two lines of them:"
	tail -n 2 "$FLASHTEST_BASE/ERROR"
fi

# Confirm output directory contains only one directory, which is the folder
# containing the FlashTest results
if [[ ! -d $RESULTS_DIR ]]; then
	echo "Expected results directory - $RESULTS_DIR - does not exist"
	exit 2
fi

NDIR=$(ls -d $RESULTS_DIR/$INVOCATION_DIR* | wc -l)
if [[ $NDIR -ne 1 ]]; then
	echo "Expected only one directory in $RESULTS_DIR"
	echo "Confirm that flashTest.py is only being called once"
	exit 3
fi

# An error occurred if this file is not empty
ERROR_LOG=$(ls -d $RESULTS_DIR/$INVOCATION_DIR*)/errors
echo
echo "--------------------------------------------------------------------------------"
echo "FlashTest Error Log = $ERROR_LOG"
if [[ ! -f $ERROR_LOG ]]; then
	echo "FlashTest error log not found"
	#echo "--------------------------------------------------------------------------------"
	echo
	exit 4
elif [[ -s $ERROR_LOG ]]; then
	echo "FlashTest reports FAILURE"
	echo
	cat $ERROR_LOG
	echo
	#echo "--------------------------------------------------------------------------------"
	echo
	exit 5
elif [ $EXITSTATUS -ne 0 ]; then
	echo "FlashTest returned exit status $EXITSTATUS"
	#echo "--------------------------------------------------------------------------------"
	echo
	exit 6
else
	echo "FlashTest reports SUCCESS"
fi
#echo "--------------------------------------------------------------------------------"
