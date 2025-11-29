#include <iostream>
#include <stdexcept>
#include <string>

/**
 * Queue implementation in C++ with templates.
 * Operations: enqueue, dequeue
 */

#define VERBOSE  (1)

template <class T, int C = 3>
class Queue
{
    T q[C];
    int head = 0;
    int tail = 0;
    public:
      void enqueue(T x);
      T dequeue();
};

template <class T, int C>
void Queue<T, C>::enqueue(T x)
{
    if(VERBOSE)
    {
        std::cout << "Add item "<<x<<" to queue\n";
    }
    if((head == 0 && tail == C) || tail + 1 == head)
    {
        // full queue
        throw std::overflow_error("The queue is full");
    }
    q[tail] = x;
    if(tail == C)
    {
        tail = 0;
    } else {
        tail = tail + 1;
    }
}

template <class T, int C>
T Queue<T, C>::dequeue()
{
    if(VERBOSE)
    {
        std::cout << "Remove item from queue\n";
    }
    if(head == tail)
    {
        // empty queue
        throw std::underflow_error("The queue is empty");
    }
    T x = q[head];
    if(head == C)
    {
        head = 0;
    } else {
        head = head + 1;
    }
    return x;
}

int main()
{
    try
    {
        const int n = 3;
        Queue<std::string, n> q;
        for(int i = 0; i < n; i++)
        {
            q.enqueue(std::to_string(i));
        }
        for(int i = 0; i < n; i++)
        {
            auto x = q.dequeue();
            std::cout<<"Removed item " << x << "\n";
        }
    }
    catch(const std::exception& e)
    {
        std::cerr << "ERROR: " << e.what() << '\n';
    }

    return 0;
}
