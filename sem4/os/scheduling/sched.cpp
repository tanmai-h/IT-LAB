#include<iostream> 
#include <algorithm>

using namespace std;

void fcfs_findWaitingTime(int processes[], int n, int bt[], int wt[]) { 
	wt[0] = 0; 
	
	for (int i = 1; i < n ; i++ ) 
		wt[i] = bt[i-1] + wt[i-1] ; 
} 

void fcfs_findTurnAroundTime( int processes[], int n, int bt[], int wt[], int tat[]) { 
	for (int i = 0; i < n ; i++) 
		tat[i] = bt[i] + wt[i]; 
} 

void fcfs_findavgTime( int processes[], int n, int bt[]) {
	int wt[n], tat[n], total_wt = 0, total_tat = 0; 
	fcfs_findWaitingTime(processes, n, bt, wt); 
	fcfs_findTurnAroundTime(processes, n, bt, wt, tat);	
	cout << "Processes "<< " Burst time "
		<< " Waiting time " << " Turn around time\n"; 
	for (int i=0; i<n; i++) { 
		total_wt = total_wt + wt[i]; 
		total_tat = total_tat + tat[i]; 
		cout << " " << i+1 << "\t\t" << bt[i] <<"\t "
			<< wt[i] <<"\t\t " << tat[i] <<endl; 
	} 

	cout << "Average waiting time = "		<< (float)total_wt / (float)n; 	cout << "\nAverage turn around time = "		<< (float)total_tat / (float)n; 
	} 
void rr_findWaitingTime(int processes[], int n, int bt[], int wt[], int quantum) { 	
	int rem_bt[n]; 
	for (int i = 0 ; i < n ; i++) 
		rem_bt[i] = bt[i]; 

	int t = 0; 
	
	while (1)	{ 
		bool done = true; 
		for (int i = 0 ; i < n; i++){ 	
			if (rem_bt[i] > 0){ 
				done = false; 
				if (rem_bt[i] > quantum) { 	
					t += quantum; 
					rem_bt[i] -= quantum; 
				} 
				else{ 
					
					t = t + rem_bt[i];					
					wt[i] = t - bt[i]; 
					rem_bt[i] = 0; 
				} 
			} 
		} 
		if (done == true) 
		break; 
	} 
} 

void rr_findTurnAroundTime(int processes[], int n, 	int bt[], int wt[], int tat[]) { 
	for (int i = 0; i < n ; i++) 
		tat[i] = bt[i] + wt[i]; 
} 
void rr_findavgTime(int processes[], int n, int bt[], int quantum) { 
	int wt[n], tat[n], total_wt = 0, total_tat = 0; 

	rr_findWaitingTime(processes, n, bt, wt, quantum); 	
	rr_findTurnAroundTime(processes, n, bt, wt, tat); 

	cout << "Processes "<< " Burst time "
		<< " Waiting time " << " Turn around time\n"; 
	
	for (int i=0; i<n; i++) { 
		total_wt = total_wt + wt[i]; 
		total_tat = total_tat + tat[i]; 
		cout << " " << i+1 << "\t\t" << bt[i] <<"\t "
			<< wt[i] <<"\t\t " << tat[i] <<endl; 
	} 

	cout << "Average waiting time = "
		<< (float)total_wt / (float)n; 
	cout << "\nAverage turn around time = "
		<< (float)total_tat / (float)n; 
} 
struct Process { 
	int pid; 
	int bt; 
}; 

bool comparison(Process a, Process b) { 
	return (a.bt < b.bt); 
} 

void sjf_findWaitingTime(Process proc[], int n, int wt[]) { 
	wt[0] = 0;
	for (int i = 1; i < n ; i++ ) 
		wt[i] = proc[i-1].bt + wt[i-1] ; 
} 

void sjf_findTurnAroundTime(Process proc[], int n, int wt[], int tat[]) { 	
	for (int i = 0; i < n ; i++) 
		tat[i] = proc[i].bt + wt[i]; 
} 

void sjf_findavgTime(Process proc[], int n) { 
	int wt[n], tat[n], total_wt = 0, total_tat = 0; 
	sjf_findWaitingTime(proc, n, wt); 

	sjf_findTurnAroundTime(proc, n, wt, tat); 
	
	cout << "\nProcesses "<< " Burst time "
		<< " Waiting time " << " Turn around time\n"; 
	
	for (int i = 0; i < n; i++) 
	{ 
		total_wt = total_wt + wt[i]; 
		total_tat = total_tat + tat[i]; 
		cout << " " << proc[i].pid << "\t\t"
			<< proc[i].bt << "\t " << wt[i] 
			<< "\t\t " << tat[i] <<endl; 
	} 

	cout << "Average waiting time = "
		<< (float)total_wt / (float)n; 
	cout << "\nAverage turn around time = "
		<< (float)total_tat / (float)n; 
} 


int main() { 
	int processes[] = { 1, 2, 3, 4, 5}; 
	int n = sizeof processes / sizeof processes[0]; 
    int quantum = 2;
	
	int burst_time[] = {10, 29, 3, 7, 12}; 

    printf("**********************FCFS***********************\n");
	fcfs_findavgTime(processes, n, burst_time); 

	int _processes[] = { 1, 2, 3, 4, 5}; 
	n = sizeof processes / sizeof processes[0]; 
    quantum = 2;
	int _burst_time[] = {10, 29, 3, 7, 12}; 
    printf("\n\n\n\n**********************RR***********************\n");
    rr_findavgTime(_processes, n, _burst_time, quantum);

	Process proc[] = {{1, 10}, {2, 29}, {3, 3}, {4, 7},{5,12}}; 
    sort(proc, proc + n, comparison); 

    printf("\n\n\n\n**********************SJF***********************\n");
	printf("Order in which process gets executed\n");
	for (int i = 0 ; i < n; i++) 
		cout << proc[i].pid <<" "; 

	sjf_findavgTime(proc, n); 
    
	cout << "\n\n\n\n\n\n\n";
	return 0; 
} 
