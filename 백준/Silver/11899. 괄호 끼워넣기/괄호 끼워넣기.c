#include <stdio.h>
#include <string.h>
#define True 1
#define False 0
typedef struct _sstt{
    char arr[50];
    int topindex;
}stack;
typedef stack Stack;
void Stackinit(Stack *pstack){
    pstack->topindex = 0;
}
int Empty(Stack *pstack){
    if(pstack->topindex == -1){
        return True;
    }
    else
    {
        return False;
    }
}
char return_top(Stack *pstack){
    return pstack->arr[pstack->topindex];
}
int return_topindex(Stack *pstack){
    return pstack->topindex;
}
void Push(Stack *pstack,char data){
    pstack->topindex = pstack->topindex + 1;
    pstack->arr[pstack->topindex] = data;
}
void Pop(Stack *pstack){
    pstack->arr[pstack->topindex] = '\0';
    pstack->topindex = pstack->topindex - 1;

}
int main(void){
    Stack stack;
    Stackinit(&stack);
    char array[51];
    scanf("%s",array);
    int size = strlen(array);
    for(int i = 0;i<size;i++){
        if(i == 0){
            Push(&stack,array[i]);
        }
        else
        {
            if(return_top(&stack) == '(' && array[i] == ')'){
                Pop(&stack);
            }
            else
            {
                Push(&stack,array[i]);
            }
        }
    }
    int i = return_topindex(&stack);
    printf("%d",i);
}