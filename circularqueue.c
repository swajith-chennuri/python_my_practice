#include<stdio.h>
#include<stdlib.h>
#define SIZE 5
int cq[SIZE];
int front=-1,rear=-1;
int isfull()
{
	if((front==rear+1)||(front==0&&rear==SIZE-1))
	   return 1;
	return 0;
}
int isempty()
{
	if(front==-1)
		return 1;
	return 0;
}
void enqueue(int ele)
{
	if(isfull)
	    printf("\n queue is full !!\n");
	else{
		if(front==-1)
			front=0;
		rear=(rear+1)%SIZE;
		cq[rear]=ele;
		printf("\n %d is inserted",ele);
	}
}
int dequeue()
{
	int ele;
	if(isempty){
		printf("\n queue is empty !!\n");
		return(-1);
	}
	else{
		ele=cq[front];
		if(front==rear){
			front=-1;
			rear=-1;
		}
		else
			front=(front+1)%SIZE;
		printf("\n deleted element = %d \n",ele);
		return(ele);
	}
}
void display()
{
	int i;
	if(isempty())
		print("\n empty queue \n");
	else{
		printf("\n front-> %d",front);
		printf("\n items->");
		for(i=front;i!=rear;i=(i+1)%SIZE)
			printf("%d",cq[i]);
		printf("%d",cq[i]);
		printf("\n rear->%d\n",rear);
	}
}
void main(){
	int ch,i;
	while(1){
		printf("\n CIRCULAR QUEUE");
		printf("\n 1-enqueue");
		printf("\n 2-dequeue");
		printf("\n 3-display");
		printf("\n 4-exit");
		printf("\n enter your choice");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1:
				printf("\n enter the value");
				scanf("%d",&i);
				enqueue(i);
				break;
			case 2:
				printf("\n delete item is");
				dequeue(i);
				break;
			case 3:	
				display();	
				break;
			case 4:
				exit(0);	
		}
	}
}