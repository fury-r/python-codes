#include <iostream>
using namespace std;
struct Node
{
    int data;
    struct Node *next;
};

class abc
{
public:
    Node *head = NULL;
    Node *tail = NULL;
    head = new Node();
    tail = new Node();
    void insert(int d)
    {

        if (*head == NULL)
        {
            head->data = d;
            head->next = NULL;
            tail = head;
        }
        else
        {
            Node *tmp = new Node();
            tmp->data = d;
            tmp->next = NULL;
            tail->next = tmp;
            tail = tmp;
        }
    }
    void display()
    {
        Node *tmp = new Node();
        tmp = head;

            while (tmp != NULL)
        {
            cout << tmp->data << " ";
            tmp = tmp->next;
        }
        cout << endl;
    }
    void Delete()
    {
        Node *tmp = new Node();
        tmp = head;
        head = tmp->next;
        tmp->next = NULL;
    }
    void isEmpty()
    {
        if (head == NULL)
        {
            cout << "Empty\n";
        }
        else
            cout << "Not Empty\n";
    }
    void search(int s)
    {
        Node *tmp = new Node();
            tmp = head int count;
        while (tmp != NULL)
        {
            if (tmp->data == s)
            {
                cout << "At position " << count << endl;
                return 0;
            }
            count++;
        }
    }
};

int main()
{
    abc a;
    int x, d;
    while (x != 0)
    {
        cout << "1 Insert /n2 Display \n3 Delete /n4 IsEmpty \n5 search" << Endl;
        cin >> x;
        switch (x)
        {
        case 1:
            cout << "Enter Data" << endl;
            cin >> d;
            a.insert(d);
            break;
        case 2:
            a.display();
            break;
        case 3:
            a.Delete();
            break;
        case 4:
            a.isempty();
            break;
        case 5:
            cout << "Enter the value to be searched" cin >> d;
            a.search(d);
            break;
        case 0:
            break;
        }
    }
}