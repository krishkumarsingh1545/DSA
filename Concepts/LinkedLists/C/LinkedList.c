#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

typedef struct LinkedList
{
    int data;
    struct LinkedList* next;
}Node;

void traversal(Node* head) {
    if (head == NULL)
        printf("List is empty.");
        
        printf("%d", head);
        if (head->next == NULL)
            return;
        head = head->next;
    }
    
    Node insertion(Node* newNode, int o) {
        if (newNode = NULL) {
            newNode->data = o;
            newNode->next = NULL;
            return *newNode;
        }
        
    }
    
    Node* deletion(Node* head, int o){
    if (head == NULL)
        printf("List is empty.");
    return head;
    
}

int main() {
    char op = '0';
    Node* head;
    int n = 0;
    while (op != '1') {
        system("cls");
        printf("1. Create a linked list\n");
        printf("2. Exit.\n");
        printf("Choose option: ");
        op = getch();
        if (op == '1')
            head = NULL;
        else if (op == '2')
            return 0;
    }
    
    while (op == 1 || op == 2 || op == 3)
	{
		printf("\n1. Traversal\n");
		printf("2. Insertion\n");
		printf("3. Deletion\n");
		printf("Press any key and Enter to exit\n");
		printf("\n Enter option: ");
        op = getch();
		switch (op)
		{
		case '1':
			traversal(head);
			break;
		case 2:
            printf("Enter new node: ");
            scanf("%d", &n);
			*head = insertion(head, n);
			break;
        case '3':
            printf("Enter index to delete: ");
            scanf("%d", &n);
			*head = deletion(head, n);
			break;
		default:
			printf("\nUnknown input\n");
			break;
		}
		getch();
		system("cls");

    }
    
    return 0;
}