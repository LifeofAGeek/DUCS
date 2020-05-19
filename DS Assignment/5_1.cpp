#include <bits/stdc++.h>
using namespace std;

//Postorder transversal from Inorder and Preorder

int find_value(int p, int in_order[], int n) {
   for (int i = 0; i < n; ++i) {
      if (in_order[i] == p) {
         return i;
      }
   }
   return -1;
}

int postorder(int pre_order[], int in_order[], int n) {
   int root = find_value(pre_order[0], in_order, n);
   if(root !=0 )
      postorder(pre_order+1, in_order, root);
   if (root != n-1)
      postorder(pre_order+root+1, in_order+root+1, n-root-1);
   cout<<pre_order[0]<<" ";
}

int main() 
{
   int pre_order[] = {1, 2, 4, 5, 3, 6};
   int in_order[] = {4, 2, 5, 1, 3, 6};
   int size = sizeof(pre_order)/sizeof(pre_order[0]);
   postorder(pre_order, in_order, size);
   return 0;
}
