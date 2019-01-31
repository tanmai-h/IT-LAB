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

void getsem(vector<vi> &dag,vi &count, vi &active) {
    int sem=0;
    vi s;
    for(int i=0;i<dag.size();i++)
        if(count[i]==0)
            s.push_back(i);
    sem=1;

    while(s.size()>0) {
        int tmpsize=s.size();
        cout << "sem " << sem << ": ";
        while(tmpsize--) {            
            int i=s.back(); s.pop_back();
            if(active[i]==0) continue;
            cout << i << ", ";
            active[i]=0;
            for(int j=0; j< dag[i].size();j++) {
                count[dag[i][j]]--;
                if(count[dag[i][j]]==0)
                    s.push_back(dag[i][j]);
            }
        }
        cout << endl;
        sem++;
    }
}

int main() {
    int v,e,x,y;
    cin >> v >> e;
    vector<vi> dag(v,vi());
    vi count(v,0),active(v,1);

    for(int i=0;i<e;i++) {
         cin >> x >> y;
         dag[x].push_back(y);
         count[y]++;
    }
    // cout << dag;
    // cout << count;
    getsem(dag,count, active);

    return 0;
}