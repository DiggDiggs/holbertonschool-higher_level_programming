#ifndef LIST_H
#define LIST_H

#include <stdlib.h>

/**
 * struct listint_s
 * @n: interger
 * @next: points to the next node 
 *
 * discription: singly linked list nide structure 
 *
 */
typedef strut listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list 
#endif 