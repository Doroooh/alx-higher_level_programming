#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - function, prints some basic info about python list
 * @p: PyObject
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int k;
	PyObject *v;
	PyListObject *list;
	Py_ssize_t len;

	if (PyList_Check(p))
		list = (PyListObject *)(p);

	len = PyList_Size(p);

	printf("[*] Size of the Python List = %zu\n", len);
	printf("[*] Allocated = %zu\n", list->allocated);

	for (k = 0; k < len; k++)
	{
		v = PyList_GET_ITEM(p, k);
		printf("Element %d: %s\n", k, (v->ob_type)->tp_name);
	}
}
