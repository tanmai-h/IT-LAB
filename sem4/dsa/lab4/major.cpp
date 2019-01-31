#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vi;

template <typename T> 
ostream& operator<<(ostream& os, const vector<T>& v) { 
    os << "["; 
    for (int i = 0; i < v.size(); ++i) { 
        os << v[i]; 
        if (i != v.size() - 1) 
            os << ", "; 
    } 
    os << "]\n"; 
    return os; 
}

int main() {
    
    return 0;
}