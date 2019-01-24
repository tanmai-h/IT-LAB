//max array sum suing div conquer
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef vector<int> vi;

vi cross(vi &vec, int l, int m, int r) {
    int lf = -1e5, rf = -1e5;
    int s=0,a=m,b=m+1;
    for(int i = m; i>=l;i--) {
        s += vec[i];
        if(s > lf) {
            lf = s;
            a = i;
        }
    }
    s = 0;
    for(int i = m+1; i<=r;i++) {
        s += vec[i];
        if(s > rf) {
            rf = s;
            b = i;
        }
    }

    return vi() = {a,b,lf+rf};
}
vi sum(vi &vec, int l, int r) {  
    int m = (l+r)/2;
    if(l == r) {
        return vi() = {l,l,vec[l]};
    }
    else if (l<r) {
        vi a = sum(vec,l,m),
           b = sum(vec,m+1,r),
           c = cross(vec,l,m,r);
        int mm = std::max(max(a[2],b[2]),c[2]);
        if(mm == a[2]) return a;
        else if(mm == b[2]) return b;
        else return c;
    }
}

vi linearsum(vi &vec) {
    int gmax = -1e5, cmax = 0;
    int s=0,e,c=0;
    //for(int i = 1; i < vec.size(); i++) {
    //    cmax = std::max(vec[i],cmax+vec[i]);
    //    gmax = std::max(gmax,cmax);
    //    cout << "i: " << cmax << ", " << gmax << endl;
    //}

    for(int i = 0; i < vec.size(); i++) {
        cmax += vec[i];
        if(cmax < 0) {
            s = i;
        }
        else if(gmax < cmax) {
            gmax = cmax;
            e = i;
        }
        else {
            c++;
        }
    }
    cout << gmax << ", " << s <<"," << e << endl;

    return vi()={};
} 
int main () {
    vi v = {-2, 10, -4, 12, -9};
    vi m = sum(v,0,v.size()-1); // (i,j,sum[i:j])
    linearsum(v);
    return 0;
}


//S(A) = max(S(L),S(R),S(L)+S(R))