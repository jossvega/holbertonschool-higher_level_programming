#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int n_elements = element_list(aux);

	int *arr, index;
	int i = 0;

	arr = malloc(sizeof(int) * n_elements);
	if (!arr)
		return (1);

	for (index = 0; aux; index++)
	{
		arr[index] = aux->n;
		aux = aux->next;
	}

	while (i < n_elements / 2)
	{
		if (arr[i] == arr[index - 1])
		{
			i++;
			index--;
			continue;
		}
		break;
	}
	if (i == n_elements / 2)
	{
		free(arr);
		return (1);
	}
	free(arr);
	return (0);
}
