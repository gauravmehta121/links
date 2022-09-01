#include <iostream>
using namespace std;
//function
int getMinMoves(int arr[], int n)
{
    int i, j, k = 0;
    //starting nested loop here
    for (i = 0; i < n - 1; i++)
        for (j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
    //printing Correct Order            
    cout<<"Correct Order: ";
    for (k= 0; k < n; k++) //for loop
        cout << arr[k] << " ";
    cout << endl;
    return 0;
}
int main()
{
    int plates[5] = {4, 6, 3, 2, 5};
    //calling function
    getMinMoves(plates, 5);
    return 0;
}


// This is complete logic of a Program

/*
NOTE:

    I completed this Assessment during Amazon Hackerrank 1st Round 

    If you can figure out any other Approach to solve this problem,
    You can share me the code which will help other Candidates. 
    I would love to hear from you if you've cracked the Interview.
    beingactual@gmail.com
*/


public static int minMoves(int [] plates , int n){

        int min = Integer.MAX_VALUE;
        int minIndex= 0 , maxIndex = 0;
        int max = Integer.MIN_VALUE;
        for(int i = 0 ; i< n  ; i++ ){
            if(min > plates[i]){
                min= plates[i];
                minIndex = i; 
            }
            if(max < plates[i]){
                max = plates[i];
                maxIndex = i;
            }
        }
       
        if(minIndex<maxIndex){     // simply we calculate the distance for both the points--> for min swaps would be (min - 0) + and for max (length-1-max)
            return (minIndex + n-1 - maxIndex);
        }
        else{
            return ( n-1- maxIndex + minIndex -1 );     
        }
       
        }
