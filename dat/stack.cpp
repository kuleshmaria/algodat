#include <iostream>
#include <stdexcept>
#include <string>

#define VERBOSE  1

/**
 * Stack implementation in C++ with templates.
 * T - data type, C - maximal capacity of the stack
 */

template <class T, int C = 3>
class Stack {
    T a[C];
    int top = -1;
    public:
        Stack();
        ~Stack();
        void push(T x);
        T pop();
        bool is_empty();
        void print();
};

template <class T, int C>
Stack<T, C>::Stack()
{
    if(VERBOSE)
    {
        std::cout << "Create Stack\n";
    }
}

template <class T, int C>
Stack<T, C>::~Stack()
{
    if(VERBOSE)
    {
        std::cout << "Destroy Stack\n";
    }
}

template <class T, int C>
bool Stack<T, C>::is_empty()
{
    return top == -1;
}

template <class T, int C>
void Stack<T, C>::push(T x)
{
    if(VERBOSE)
    {
        std::cout << "Push item "<<x<<" to stack\n";
    }
    if(top + 1 == C)
    {
        throw std::overflow_error("Stack overflow");
    }
    top += 1;
    a[top] = x;
}

template <class T, int C>
T Stack<T, C>::pop()
{
    if(VERBOSE)
    {
        std::cout << "Pop item from stack\n";
    }
    if(is_empty())
    {
        throw std::underflow_error("Stack underflow");
    }
    T x = a[top];
    top -= 1;
    return x;
}

template <class T, int C>
void Stack<T, C>::print()
{
    if(is_empty())
    {
        std::cout << "Stack is empty\n";
        return;
    }
    std::cout << "Stack: ";
    for(int i = 0; i <= top; i++)
    {
        std::cout << a[i] << " ";
    }
    std::cout << "\n";
}

int main()
{
    try
    {
        // test
        Stack<std::string> st;
        st.print();
        st.push("hello");
        st.push("world");
        st.print();
        std::string s = st.pop();
        std::cout << "Removed " << s << "\n";
        st.print();
    }
    catch(const std::exception& e)
    {
        std::cerr << "ERROR: " << e.what() << '\n';
    }

    return 0;
}
