
#include<iostream> 
using namespace std; 
  

const int P = 5; 

int processes[] = {0, 3, 6, 7, 9};  

const int R = 3; 
  

void calculateNeed(int need[P][R], int maxm[P][R], 
                   int allot[P][R]) 
{ 
    
    for (int i = 0 ; i < P ; i++) 
        for (int j = 0 ; j < R ; j++) 
  
            
            
            need[i][j] = maxm[i][j] - allot[i][j]; 
} 
  

bool isSafe(int processes[], int avail[], int maxm[][R], 
            int allot[][R]) 
{ 
    int need[P][R]; 
  
    
    calculateNeed(need, maxm, allot); 
  
    
    bool finish[P] = {0}; 
  
    
    int safeSeq[P]; 
  
    
    int work[R]; 
    for (int i = 0; i < R ; i++) 
        work[i] = avail[i]; 
  
    
    
    int count = 0; 
    while (count < P) 
    { 
        
        
        
        bool found = false; 
        for (int p = 0; p < P; p++) 
        { 
            
            
            if (finish[p] == 0) 
            { 
                
                
                
                int j; 
                for (j = 0; j < R; j++) 
                    if (need[p][j] > work[j]) 
                        break; 
  
                
                if (j == R) 
                { 
                    
                    
                    
                    for (int k = 0 ; k < R ; k++) 
                        work[k] += allot[p][k]; 
  
                    
                    safeSeq[count++] = p; 
  
                    
                    finish[p] = 1; 
  
                    found = true; 
                } 
            } 
        } 
  
        
        
        if (found == false) 
        { 
            cout << "System is not in safe state"; 
            return false; 
        } 
    } 
  
    
    
    cout << "System is in safe state.\nSafe"
         " sequence is: "; 
    for (int i = 0; i < P ; i++) 
        cout << processes[safeSeq[i]] << " "; 
  
    return true; 
} 
  

int main() 
{ 
    int processes[] = {0, 3, 6, 7, 9}; 
  
    
    int avail[] = {5, 1, 6}; 
  
    
    
    int maxm[][R] = {{6, 4, 3}, 
                     {7, 8, 9}, 
                     {5, 6, 2}, 
                     {4, 6, 9}, 
                     {8, 9, 1}}; 
  
    
    int allot[][R] = {{2, 1, 0}, 
                      {5, 1, 2}, 
                      {4, 5, 0}, 
                      {0, 5, 8}, 
                      {7, 5, 0}}; 
  
    
    isSafe(processes, avail, maxm, allot); 
  
    return 0; 
} 