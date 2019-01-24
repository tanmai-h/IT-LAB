// inversions
#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vi;

int merge(vi &vec, int l, int m, int r) {
    vi a, b;
    for(int i = l; i <= m; i++) a.push_back(vec[i]);
    for(int i = m+1; i <= r; i++) b.push_back(vec[i]);

    int i=0,j=0,k=l,inv=0;
    while(i<a.size() && j<b.size()) {
        if(a[i]<=b[j]) {
            vec[k++] = a[i++];
        }
        else if(a[i]>b[j]) {
            inv += (m-i);
            vec[k++] = b[j++];
        }
    }
    while(i<a.size()) vec[k++] = a[i++];
    while(j<b.size()) vec[k++] = b[j++];

    return inv;
}

int sorter(vi&vec, int l, int r) {
    int m = (l+r)/2;
    if(l < r) {
        int a = sorter(vec,l,m); int b = sorter(vec,m+1,r);
        //cout << "l,r " << l << "," << r << ": " << "a,b " << a << "," << b << endl; 
        return merge(vec,l,m,r) + a + b;
    }

    else return 0;
}

int main(int argc, char const *argv[]) {
    vi vec = {10,12,8,4,-3,-15};
    int c = 0;
    //for(int i = 0; i < vec.size(); i++) for(int j = i+1; j < vec.size(); j++)
    //    if(vec[i]>vec[j]) c++;
    //cout << c << endl;
    cout << sorter(vec, 0, vec.size()-1) << endl;
    
    return 0;
}


