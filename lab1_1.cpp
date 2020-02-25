#include<bits/stdc++.h>
using namespace std;

struct twoStack
{
    int Size;
    int top1,top2;
    int *arr;
};
twoStack *st;

void createStack(int n)
{
    st->Size=n;
    st->top1=-1;
    st->top2=n;
}

void push(twoStack *st, int val)
{
    if(st->top==(st->Size)-1)
        cout<<"Stack Overflow!!";
    else{
        st->top++;
        st->s[st->top]=val;
    }
}

int pop(Stack *st)
{
    int x=-1;
    if(st->top==-1)
        cout<<"Stack Underflow";
    else{
        x=st->s[st->top];
        st->top--;
    }
    return x;
}

void display(Stack *st)
{
    for(int i=0;i<=st->top;i++) cout<<st->s[i]<<" ";
}


int main()
{
    int *a=new int[50];
    createStack(&a,10);
    push(st1,2);
    display(st1);
}
