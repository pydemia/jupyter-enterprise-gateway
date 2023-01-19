# Useful Functions or APIs to execute codes in remote

## Execution steps

### Kernels

1. Prepare a kernel running
   1. Get lists of available kernels & its specs; which is called `kernelspec`.
      * The following details should be pre-defined:
        * language (ex. python, r, scala, etc.)
        * env (ex. language version, installed packages, gpu, etc.)
   2. Specify a kernelspec: by user, using the name of a kernel
   3. Start a kernel if there is no process running or a new process is needed  
      1. Create a remote process using the kernelspec
      2. Wait until ready
2. Execute a code against the kernel
   1. Select a running kernel to execute
   2. Send the code and run (in blocking or asynchronous way)
   3. Wait and receive the result
      * Wait until the execution finished: 
      * Interrupt the former request before finished: Get stdout and stderr(mostly common: `Traceback: KeyboardInterrupt`)
    4. 
3. Shutdown the kernel
   1. Check if idle