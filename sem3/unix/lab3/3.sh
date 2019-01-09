echo " input 2 strings, one per line"
read str1
read str2
echo " 1. Empty Checker"
echo " 2. is Equal"
echo " 3. is palindrome"
read op
case $op in
	1)
		if [ ! -s ${str1} ]; then
			echo " 1st str is not empty"
		else
			echo " 1st str is empty"
		fi
		if [ ! -s ${str2}  ]; then
			echo " second str is not empty"
		else
			echo " 1st str is empty"
		fi
		;;
	2)
		if [ ${str1} == ${str2} ];then
			echo "both are equal"
		else
			echo " not equal"
		fi 
		
		;;

	3)	str=$(echo "${str1}" | rev) 
		if [ ${str} == ${str1} ] ; then
			echo "1st palindrome"
		else
			echo "1st not palindrome"
		fi
		fil=$(echo "${str2}" | rev) 
		if [ ${fil} == ${str2} ] ; then
			echo "2ndpalindrome"
		else
			echo "2nd not palindrome"
		fi
		;;	

	*)
		echo "wrong option"
		;;
  esac






