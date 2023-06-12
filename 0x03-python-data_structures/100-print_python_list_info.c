#include <Python.h>

/**
* print_python_list_info - To Print basic info about Python lists
* @p: A PyObject list.
*/
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, alloc, num;
    PyObject *obj;

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);

    for (num = 0; num < size; num++)
    {
        printf("Element %d: ", num);

        obj = PyList_GetItem(p, num);
        printf("%s\n", Py_TYPE(obj)->tp_name);
    }
}
