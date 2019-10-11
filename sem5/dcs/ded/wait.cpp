#include<bits/stdc++.h>
using namespace std;

int main()
{
	int p1,p2,t1,t2;
	cout<<"2 process with id 1 and 2";
	cout<<"\nid which is currently holding,  pid which came first:\n";
	cin>>p1>>p2;

	if(p2==1){ 
			t1=1; t2=2;
		}
	else{ t1=2; t2=1;}

	if(p1==1){
		if(t2<t1){
			cout<<"Process 2 waits"<<endl;
		}
		else{
			cout<<"Process 2 is killed"<<endl;
		}
	}

	if(p1==2){
		if(t1<t2){
			cout<<"Process 1 waits"<<endl;
		}
		else{
			cout<<"Process 1 is killed"<<endl;
		}
	}



}