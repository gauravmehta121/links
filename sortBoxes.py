# Method to sort the junctions boxes
def sortBoxes(boxlist):
    l = len(boxlist)

    # Performing selection sort
    for i in range(l-1):
        pos = i
        for j in range(i+1, l):
            # Get version details of both ith and jth index
            s1 = boxlist[pos].split(maxsplit=1)[1]
            s2 = boxlist[j].split(maxsplit=1)[1]

            # If both are new junctions boxes, do nothing
            if s1.islower() == False and s2.islower() == False:
                continue
            if s2 < s1:
                pos = j
        if pos != i:
            boxlist[i], boxlist[pos] = boxlist[pos], boxlist[i]
    
    # At this point, the boxlist has new junctions boxes first and then old
    
    # Find index from where old junctions boxes start
    pos = -1
    for i in range(len(boxlist)):
        s = boxlist[i].split(maxsplit=1)[1]
        if s.islower():
            pos = i
            break
    
    # Swap new and old
    if pos != -1:
        boxlist = boxlist[pos:] + boxlist[:pos]
    return boxlist

# Driver code
def main():
    bx = ["ykc 82 01", "eo first qpx", "09z cat hamster", "06f 12 25 6",
          "az0 first qpx", "236 cat dog rabbit snake"]
    print("\nOriginal list:")
    for i in bx:
        print(i)
    b = sortBoxes(bx)

    print("\nSorted list:")
    for i in b:
        print(i)
    print()

main()



""" NOTE:

    I completed this Assessment during Amazon Hackerrank 1st Round 

    If you can figure out any other Approach to solve this problem, 
    feel free to share me the Code which will help other candidate.
    I would love to hear from you on the Mail ID I have Provided. 
    if you've cracked the Interview.

    beingactual@gmail.com
    
"""





#include<bits/stdc++.h>
using namespace std;

#define tests int t; cin >> t; while(t--)
#define int long long

int util(string s, int i, int count, int prev) {
    if(count==3) return 1;
    if(i==s.size()) return 0;

    int temp=0;

    if(prev==1) {
        if(s[i]=='0') temp+=util(s, i+1, count+1, 0);
    } else {
        if(s[i]=='1') temp+=util(s, i+1, count+1, 1);
    }
    temp+=util(s, i+1, count, prev);

    return temp;
}

void solve() {
    string s;
    cin >> s;

    cout << util(s, 0, 0, 0)+util(s, 0, 0, 1) << endl;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    tests{
        solve();
    }

    return 0;
}
