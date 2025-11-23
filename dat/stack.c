#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/**
 * Stack implementation in C.
 * Operations: push, pop, empty
 */

#define MAX_CAPACITY 3
#define VERBOSE     (0)

typedef struct stack_t stack_t;
struct stack_t
{
    int a[MAX_CAPACITY];
    int top;
};

int handle_error(stack_t* st, char* error_msg)
{
    printf("Error: %s\n", error_msg);
    free(st);
    exit(1);
}

void init(stack_t* st)
{
    if(VERBOSE)
    {
        printf("Initialize stack\n");
    }
    st->top = -1;
}

bool is_empty(stack_t* st)
{
    return st->top == -1;
}

void push(stack_t* st, int x)
{
    if(VERBOSE)
    {
        printf("Push item %d to stack\n", x);
    }
    if(st->top + 1 == MAX_CAPACITY)
    {
        // overflow
        handle_error(st, "stack overflow");
    }
    st->top += 1;
    st->a[st->top] = x;
}

int pop(stack_t* st)
{
    if(VERBOSE)
    {
        printf("Pop item from stack\n");
    }
    if(is_empty(st))
    {
        // underflow
        handle_error(st, "stack underflow");
    }
    int x = st->a[st->top];
    st->top -= 1;
    return x;
}

void print(stack_t* st)
{
    if(is_empty(st))
    {
        printf("Stack is empty\n");
        return;
    }
    printf("Stack: ");
    for(int i = 0; i <= st->top; i++)
    {
        printf("%d ", st->a[i]);
    }
    printf("\n");
}

int main(int argc, char** argv)
{
    stack_t* st = calloc(1, sizeof(stack_t));

    // test
    init(st);
    print(st);
    push(st, 3);
    push(st, 1);
    push(st, 2);
    print(st);
    pop(st);
    int x = pop(st);
    printf("Removed item %d\n", x);
    print(st);

    //free
    free(st);
    return 0;
}
