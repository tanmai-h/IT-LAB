#include<iostream>
using namespace std;

int abs(int x){
	if(x<0)
		return -1*x;
	return x;
}

int main()
{
	int n,sstf=0,fcfs=0,min=200,close,maximum=-1,minimum=200,curr=0,curr1=0;
	cout<<"Enter the number of requests: ";
	cin>>n;
	int A[n+1];
	A[0]=50;
	cout<<"Enter the request queue: ";
	for(int i=1;i<=n;i++)
		cin>>A[i];
	cout<<"Enter starting position: ";
	cin>>curr;
	curr1=curr;
	for(int i=0;i<n;i++)
{
		fcfs=fcfs+abs(curr-A[i+1]);
		curr=A[i+1];
}
	cout<<"Movements required by r/w head in FCFS is: "<<fcfs<<"\n";
	cout<<"Time required by r/w head in FCFS is: "<<fcfs<<"ns\n";
	curr=curr1;
	for(int i=1;i<=n;i++)
	{
		if(min>abs(curr-A[i]))
		{
			min = abs(curr-A[i]);
			close = i;
			curr=A[i];
		}
	}
	for(int i=0;i<=n;i++)
	{
		if(maximum<A[i])
			maximum=A[i];
		if(minimum>A[i])
			minimum=A[i];
	}
	cout<<maximum<<" "<<minimum<<"\n";
	if(curr1-A[close]>=0)
		sstf=maximum-2*minimum+curr1;
	else
		sstf=2*maximum-curr1-minimum;
	cout<<"Movements required by r/w head in SSTF is: "<<sstf<<"\n";
	cout<<"Time required by r/w head in SSTF is: "<<sstf<<"ns\n";
	if(sstf<fcfs)
		cout<<"SSTF is BETTER"<<endl;
	else
		cout<<"FCFS is BETTER"<<endl;
	return 0;
}