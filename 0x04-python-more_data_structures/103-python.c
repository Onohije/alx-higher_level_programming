#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - It Prints bytes information
 *
 * @p: Python Object
 * Return: no return.
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, num, limit;

	printf("[.] bytes list info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes list\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (num = 0; num < limit; num++)
		if (string[num] >= 0)
			printf(" %02x", string[num]);
		else
			printf(" %02x", 256 + string[num]);

	printf("\n");
}

/**
 * print_python_list - It Prints list information
 *
 * @p: Python Object
 * Return: no return.
 */
void print_python_list(PyObject *p)
{
	long int size, num;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (num = 0; num < size; num++)
	{
		obj = ((PyListObject *)p)->ob_item[num];
		printf("Element %ld: %s\n", num, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
