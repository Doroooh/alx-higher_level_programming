#include "custom_hash_tables.h"

/**
 * custom_hash_table_create - Creates a custom hash table.
 * @size: the desired size of the new hash table.
 *
 * Return: a pointer to the newly created hash table.
 */
custom_hash_table_t *custom_hash_table_create(unsigned long int size)
{
	unsigned int index = 0;
	custom_hash_table_t *htable = malloc(sizeof(custom_hash_table_t));

	if (htable == NULL)
	{
		fprintf(stderr, "Error: Unable to allocate memory for the hash table\n");
		return NULL;
	}

	htable->size = size;
	htable->buckets = malloc(sizeof(custom_hash_node_t *) * size);
	if (htable->buckets == NULL)
	{
		fprintf(stderr, "Error: Unable to allocate memory for the buckets\n");
		free(htable);
		return NULL;
	}

	for (; index < size; index++)
		htable->buckets[index] = NULL;

	return htable;
}
