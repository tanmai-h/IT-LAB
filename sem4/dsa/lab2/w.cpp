// prob 2
#include <iostream>
#include <vector>

using namespace std;

int peak(vector<int> &vec, int l, int r) {
    int m = (r-l)/2 + l;

    if((vec[m]>vec[m-1]) && (vec[m]>vec[m+1]))
        return vec[m];
    else if((vec[m] > vec[m-1]) && (vec[m]<vec[m+1]))
        peak(vec, m, r);
    else
        peak(vec, l, m);
}

int main(int argc, char const *argv[])
{   
    vector <int> vec = {10, 12, 8, 4 , -3, -15};
    cout << peak(vec, 0, vec.size()-1) << endl;

    return 0;
}
