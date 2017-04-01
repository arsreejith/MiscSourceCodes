#include <iostream>
using namespace std;
int MAX =12;

void Qsort(int* array, int start, int end)
{
     if(start > end)
              return;
     int i,j;
     i = start;j=end;
     int pivot = array[start];
     
     while(i <= j)
     {
         while( array[i]<=pivot)
            ++i;
            while( array[j] > pivot)
         
            --j;
            
         if(i<=j)
         {
             int temp = array[j];
             array[j] = array[i];
             array[i] = temp;  
       
         }
            
     }  

     if( i > j)
     {
        int temp = array[j];
        array[j] = pivot;
        array[start]=temp;
          
     }  
     
     Qsort(array,start,j-1);
     Qsort(array,i,end);
     
}

int main()
{
   int array[]={100,99,56,34,200,2,5,77,1,9,122,45};
   
   
   Qsort(array, 0,12);
   cout<<"\n"<<"\t"<<"After Sort.."<<"\n";
   for(int i=0;i<12;++i)
   {
       cout<<"\t"<<"\n"<<array[i];        
   }
     cout<<"\n";
}

