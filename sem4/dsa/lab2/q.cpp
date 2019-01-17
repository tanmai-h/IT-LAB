// Hanoi
#include <iostream>
#include <string>

using namespace std;

void hanoi(int n, char *s,char *i,char *t) {
    if (n == 1) 
        cout << "Move disc " << n << "from " << s << " to  " << t << endl;
    else {
        hanoi(n-1, s, t, i);
        cout << "Move disc " << n << "from " << s << " to  " << t << endl;
        hanoi(n-1, i, s, t);
    }
}

int main(int argc, char const *argv[])
{
    int n;    cin >> n;
    hanoi(n, "S","I","T"); // source intermediate terminal

    return 0;
}
