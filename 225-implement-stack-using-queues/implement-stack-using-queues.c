#include <stdbool.h>
#include <stdlib.h>
#define MAX 100
typedef struct {
    int q1[MAX];
    int q2[MAX];
    int front1, rear1;
    int front2, rear2;
} MyStack;

MyStack* myStackCreate() {
    MyStack* obj = (MyStack*)malloc(sizeof(MyStack));
    obj->front1 = obj->rear1 = -1;
    obj->front2 = obj->rear2 = -1;
    return obj;
}

void enqueue(int q[], int *front, int *rear, int x) {
    if(*rear == MAX-1) return;
    if(*front == -1) *front = 0;
    q[++(*rear)] = x;
}

int dequeue(int q[], int *front, int *rear) {
    int val = q[*front];
    if(*front == *rear)
        *front = *rear = -1;
    else
        (*front)++;
    return val;
}

bool isEmpty(int front) {
    return front == -1;
}

void myStackPush(MyStack* obj, int x) {

    enqueue(obj->q2, &obj->front2, &obj->rear2, x);

    while(!isEmpty(obj->front1)) {
        enqueue(obj->q2, &obj->front2, &obj->rear2,
                dequeue(obj->q1, &obj->front1, &obj->rear1));
    }

    int temp[MAX];
    int f = obj->front1, r = obj->rear1;

    obj->front1 = obj->front2;
    obj->rear1 = obj->rear2;
    obj->front2 = -1;
    obj->rear2 = -1;

    for(int i=0;i<=obj->rear1;i++)
        obj->q1[i] = obj->q2[i];
}

int myStackPop(MyStack* obj) {
    return dequeue(obj->q1, &obj->front1, &obj->rear1);
}

int myStackTop(MyStack* obj) {
    return obj->q1[obj->front1];
}

bool myStackEmpty(MyStack* obj) {
    return obj->front1 == -1;
}

void myStackFree(MyStack* obj) {
    free(obj);
}
