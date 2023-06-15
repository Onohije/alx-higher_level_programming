#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;


size_t print_dlistint(const listint_t *h);
size_t dlistint_len(const listint_t *h);
listint_t *add_dnodeint(listint_t **head, const int n);
listint_t *add_dnodeint_end(listint_t **head, const int n);
void free_dlistint(listint_t *head);
listint_t *get_dnodeint_at_index(listint_t *head, unsigned int index);
int sum_dlistint(listint_t *head);
listint_t *insert_dnodeint_at_index(listint_t **h, unsigned int idx, int n);
int delete_dnodeint_at_index(listint_t **head, unsigned int index);

#endif /* LISTS_H */
