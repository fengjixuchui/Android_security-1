# Intro to Android Architecture and Security

* how do app actually run?
* what about security?
---------
a app

* Android is based on Linux
* Each app has its own Linux user ID*
* Each app lives in its own security sandbox
	- Standard Linux process isolation
	- Restricted file system permissions
---------

when app install 
-> Android framwork creates new Linux user
-> Each app is given a private directory(also called internal storage，no other app can access it)

----------

App Isolation
* Apps are run in separate processes
* Apps being in sandbox means that they can't
	- talk to each other
	- do anything security-sensitive
* Q: how can apps do anything interesting?
* This is when architecture & security get mixed up.

-----------
Example:Storing a File
{
	'''
	outputStreamWriter writer = new outputStreamWriter(...)
	writer.write(data);
	writer.close();
	'''
}

------------
How are syscalls actually invoked?
Each architecture has its own convention

x86 (ref)
syscall number in "eax", arguments in "ebx", "ecx", "edx", "esi", "edi", ...
execute instruction "int 0x80"
return value in "eax"

x86-64 (ref)
syscall number in "rax", args in "rdi", "rsi", "rdx", "rcx", "r8", "r9", ...
execute instruction "int 0x80" or "syscall"
return value in "rax"

ARM (ref)
execute instruction "swi" or "svc"
syscall number in "r7", args in "r0", "r1", "r2", ...
return value in "r0"

More architectures:
ref
"man syscall"

--------------

