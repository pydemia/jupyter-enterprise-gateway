import queue
from jupyter_client.manager import start_new_kernel
from pprint import PrettyPrinter


class SimpleKernel():
    """
    ## Description
    **SimpleKernel**:
     A simplistic Jupyter kernel client wrapper.
    Additional information in [this GitHub issue]
    (
    )
    """

    def __init__(self):
        """
        ## Description
        Initializes the `kernel_manager` and `client` objects
        and starts the kernel. Also initializes the pretty printer
        for displaying object properties and execution result
        payloads.
        ## Parameters
        None.
        """
        ### Initialize kernel and client
        self.kernel_manager, self.client = start_new_kernel()

        ### Initialize pretty printer
        self.pp = PrettyPrinter(indent=2)

    ### end __init__ ####

    def execute(self, code, verbose=False, get_type=False):
        """
        ## Description
        **execute**:
        Executes a code string in the kernel. Can return either
        the full execution response payload, or just `stdout`. Also,
        there is a verbose mode that displays the execution process.
        ## Parameters
        code : string
            The code string to get passed to `stdin`.
        verbose : bool (default=False)
            Whether to display processing information.
        get_type : bool (default=False) NOT IMPLEMENTED
            When implemented, will return a dict including the output
            and the type. E.g.
            1+1 ==> {stdout: 2, type: int}
            "hello" ==> {stdout: "hello", type: str}
            print("hello") ==> {stdout: "hello", type: NoneType}
            a=10 ==> {stdout: None, type: None}
        ## Returns
        `stdout` or the full response payload.
        """
        debug = lambda x: print(x if verbose else '', end='')

        debug("----------------")
        debug("executing code: " + code)

        ### Execute the code
        msg_id = self.client.execute(code)

        ### Collect the response payload
        reply = self.client.get_shell_msg()
        # reply = self.client.get_shell_msg(msg_id)
        debug("reply content")
        debug(reply['content'])

        ### Get the execution status
        ### When the execution state is "idle" it is complete
        io_msg_content = self.client.get_iopub_msg(timeout=0)['content']

        ### We're going to catch this here before we start polling
        if 'execution_state' in io_msg_content and io_msg_content['execution_state'] == 'idle':
            return "no output"

        ### Continue polling for execution to complete
        ### which is indicated by having an execution state of "idle"
        while True:
            ### Save the last message content. This will hold the solution.
            ### The next one has the idle execution state indicating the execution
            ###is complete, but not the stdout output
            temp = io_msg_content

            ### Poll the message
            try:
                io_msg_content = self.client.get_iopub_msg(timeout=0)['content']
                debug("io_msg content")
                debug(io_msg_content)
                if 'execution_state' in io_msg_content and io_msg_content['execution_state'] == 'idle':
                    break
            except queue.Empty:
                debug("timeout get_iopub_msg")
                break

        debug("temp")
        debug(temp)

        ### Check the message for various possibilities

        if 'data' in temp: # Indicates completed operation
            debug('has data')
            out = temp['data']['text/plain']
        elif 'name' in temp and temp['name'] == "stdout": # indicates output
            debug('name is stdout')
            out = temp['text']
            debug("out is " + out)
        elif 'traceback' in temp: # Indicates error
            print("ERROR")
            out = '\n'.join(temp['traceback']) # Put error into nice format
        else:
            out = ''

        debug("----------------\n\n")

        debug("returning " + str(out))
        return out

    ### end execute ####

    def showManager(self):
        """
        ## Description
        **showManager**:
        Pretty Print kernel manager object.
        """

        self.pp(self.kernel_manager)


    def showClient(self):
        """
        ## Description
        **showClient**:
        Pretty Print client object.
        """

        self.pp(self.client)


    def prettyPrint(self, payload):
        """
        ## Description
        **prettyPrint**:
        A convenience method to pretty print the reply payload.
        ## example
        ```
        >>> reply = my_kernel.execute("1+1")
        >>> my_kernel.prettyPrint(reply)
        ```
        """


    def __del__(self):
        """
        ## Description
        Destructor. Shuts down kernel safely.
        """
        self.kernel_manager.shutdown_kernel()

        
 kernel_0 = SimpleKernel()
commands = [
    '1+1',
    'a=5',
    'b=0',
    'b',
    'print()',
    'print("hello there")',
    '10',
    'a*b',
    'a',
    'a+b',
    'print(a+b)',
    'print(a*10)',
    'c=1/b'
]

for command in commands:
    print(command)
    out = kernel.execute(command, verbose=False)
    if out: print(out)

code = """
import numpy as np
import logging

log = logging.getLogger("Code Execution")

print(np.__version__)

log.info('log test')
"""

cell_out = kernel_0.execute(code, verbose=False)
print(cell_out)

object_b = kernel_0.execute("print(b)", verbose=False)
print(object_b)

kernel_1 = SimpleKernel()
object_b = kernel_1.execute("print(b)", verbose=False)
print(object_b)
