#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - prints information about a Python string object
 *
 * @p: the PyObject representing the string
 */

void print_python_string(PyObject *p)
{
    fflush(stdout);

    printf("[.] string object info\n");
    if (PyUnicode_CheckExact(p))
    {
        printf("  type: ");
        if (PyUnicode_IS_COMPACT_ASCII(p))
            printf("compact ascii\n");
        else
            printf("compact unicode object\n");
        printf("  length: %zd\n", PyUnicode_GetLength(p));
        printf("  value: ");
        PyObject_Print(p, stdout, Py_PRINT_RAW);
        printf("\n");
    }
    else
        printf("  [ERROR] Invalid String Object\n");
}
