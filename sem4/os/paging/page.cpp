#include <iostream>
#include<stdio.h>

using namespace std;

int n = 20,nf=3;
int in[100] = {9, 2, 1, 2, 0, 5, 0, 4, 2, 3, 0, 3, 1, 2, 9, 0, 5, 3, 4, 0};
int p[50];
int hit=0;
int i,j,k;
int pgfaultcnt=0;
 
void getData()
{
    printf("\nlength of pagesequence:");
    scanf("%d",&n);
    printf("\nsequence:");
    for(i=0; i<n; i++)
        scanf("%d",&in[i]);
    printf("\nno of frames:");
    scanf("%d",&nf);
}
 
void initialize()
{
    pgfaultcnt=0;
    for(i=0; i<nf; i++)
        p[i]=9999;
}
 
int isHit(int data)
{
    hit=0;
    for(j=0; j<nf; j++)
    {
        if(p[j]==data)
        {
            hit=1;
            break;
        }
 
    }
 
    return hit;
}
 
int getHitIndex(int data)
{
    int hitind;
    for(k=0; k<nf; k++)
    {
        if(p[k]==data)
        {
            hitind=k;
            break;
        }
    }
    return hitind;
}
 
void dispPages()
{
    for (k=0; k<nf; k++)
    {
        if(p[k]!=9999)
            printf(" %d",p[k]);
    }
 
}
 
void dispPgFaultCnt()
{
    printf("\nTotal no of page faults:%d",pgfaultcnt);
    cout << "\nmiss ratio: " << (float) pgfaultcnt / n;
    cout << "\nHit ratio: " << (float) (n-pgfaultcnt)/n;
    cout << "\n\n";
}
 
void fifo()
{
    initialize();
    for(i=0; i<n; i++)
    {
        //printf("\nFor %d :",in[i]);
 
        if(isHit(in[i])==0)
        {
 
            for(k=0; k<nf-1; k++)
                p[k]=p[k+1];
 
            p[k]=in[i];
            pgfaultcnt++;
            //dispPages();
        }
        else
            continue;
            //printf("No page fault");
    }
    dispPgFaultCnt();
}
 
 
void optimal()
{
    initialize();
    int near[50];
    for(i=0; i<n; i++)
    {
 
        //printf("\nFor %d :",in[i]);
 
        if(isHit(in[i])==0)
        {
 
            for(j=0; j<nf; j++)
            {
                int pg=p[j];
                int found=0;
                for(k=i; k<n; k++)
                {
                    if(pg==in[k])
                    {
                        near[j]=k;
                        found=1;
                        break;
                    }
                    else
                        found=0;
                }
                if(!found)
                    near[j]=9999;
            }
            int max=-9999;
            int repindex;
            for(j=0; j<nf; j++)
            {
                if(near[j]>max)
                {
                    max=near[j];
                    repindex=j;
                }
            }
            p[repindex]=in[i];
            pgfaultcnt++;
 
            //dispPages();
        }
        else
            continue; //printf("No page fault");
    }
    dispPgFaultCnt();
}
 
void lru()
{
    initialize();
 
    int least[50];
    for(i=0; i<n; i++)
    {
 
        //printf("\nFor %d :",in[i]);
 
        if(isHit(in[i])==0)
        {
 
            for(j=0; j<nf; j++)
            {
                int pg=p[j];
                int found=0;
                for(k=i-1; k>=0; k--)
                {
                    if(pg==in[k])
                    {
                        least[j]=k;
                        found=1;
                        break;
                    }
                    else
                        found=0;
                }
                if(!found)
                    least[j]=-9999;
            }
            int min=9999;
            int repindex;
            for(j=0; j<nf; j++)
            {
                if(least[j]<min)
                {
                    min=least[j];
                    repindex=j;
                }
            }
            p[repindex]=in[i];
            pgfaultcnt++;
 
            //dispPages();
        }
        else
            continue; //printf("No page fault!");
    }
    dispPgFaultCnt();
}
 
 

 
int main() {
    cout << "Pagr replacement \n";
    cout << "******************* FIFO **********************\n\n";
    fifo();

    cout << "****************** OPtimal ********************\n\n";
    optimal();

    cout << "****************** LRU ************************\n\n";
    lru();

    cout << "\noptimal is the best\n";
}