#include <Python.h>
#include "libhello.h"

PyObject * helloworld(PyObject * self) {
	return PyUnicode_FromFormat("Hello World from C extension!");
};

PyObject * greeting(PyObject *self, PyObject *args) {
	char *name;
    int number;

	if(!PyArg_ParseTuple(args, "si", &name, &number))
		return NULL;

	return PyUnicode_FromFormat("Hello %s! You gave me the number %d.", name, number);
}
