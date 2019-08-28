echo "Calc fib upto which number: "
read n

echo "-------------------------- Fib Serial --------------------------"
g++ fib-serial.cpp -fopenmp
echo $n | ./a.out
echo "-------------------------- Fib Parallel (wrong ans will be obtained) --------------------------"
g++ fib-par.cpp -fopenmp
echo $n | ./a.out
echo "-------------------------- Fib Parallel Data scoping,Taskwait--------------------------"
g++ fib-par-taskwait.cpp -fopenmp
echo $n | ./a.out