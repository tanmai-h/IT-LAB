// inversions
#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vi;

int merge(vi &vec, int l, int m, int r) {
    vi a(vec.begin()+l,vec.begin()+(m-l)), b(vec.begin()+m+1,vec.begin()+r);
    int i=0,j=0,k=l,inv=0;
    while(i<a.size() && j<b.size()) {
        if(a[i]<=a[j]) {
            vec[k++] = vec[i++];
        }
        else if(a[i]>a[j]) {
            inv += (m-i+1);
            vec[k++] = vec[j++];
        }
    }
    while(i<a.size()) vec[k++] = vec[i++];
    while(j<b.size()) vec[k++] = vec[j++];

    return inv;
}

int sorter(vi&vec, int l, int r) {
    int m = (l-r)/2 + r;
    if(l < r) {
        int a = sorter(vec,l,m); int b = sorter(vec,m,r);
        return merge(vec,l,m,r) + a + b;
    }

    else return 0;
}

int main(int argc, char const *argv[]) {
    vi vec = {10,12,8,4,-3,-15};
    int c = 0;
    for(int i = 0; i < vec.size(); i++) for(int j = i+1; j < vec.size(); j++)
        if(vec[i]>vec[j]) c++;
    cout << c << endl;
    cout <<sorter(vec, 0, vec.size()-1);
    
    return 0;
}


