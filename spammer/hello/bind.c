#include "libhello.h"

char helloworldfunc_docs[] = "This is my hello world function";
char greetingfunc_docs[] = "This is my greeting function";

PyMethodDef hello_funcs[] = {
	{	
        "helloworld",
		(PyCFunction)helloworld,
		METH_VARARGS,
		helloworldfunc_docs
    },
    {
        "greeting",
        (PyCFunction)greeting,
        METH_VARARGS,
        greetingfunc_docs
    },
	{	
        NULL
    }
};

char hellomod_docs[] = "This is a hello  module.";

PyModuleDef hellomod = {
	PyModuleDef_HEAD_INIT,
	"_hello",
	hellomod_docs,
	-1,
	hello_funcs,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC PyInit__hello(void) {
	return PyModule_Create(&hellomod);
}
