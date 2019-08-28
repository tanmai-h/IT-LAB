echo "Enter size of array: "
read n

echo "-------------------------- Quicksort Serial --------------------------"
g++ quick-serial.cpp -fopenmp
echo $n | ./a.out
echo "-------------------------- Quicksort Parallel --------------------------"
g++ quick-par.cpp -fopenmp
echo $n | ./a.out