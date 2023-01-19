# Responses from `jupyter`

See: https://jupyter-client.readthedocs.io/en/stable/messaging.html


* Status: `execution_state`
> When the kernel starts to handle a message, it will enter the 'busy'
> state and when it finishes, it will enter the 'idle' state.
> The kernel will publish state 'starting' exactly once at process startup.

```python
execution_state : ('busy', 'idle', 'starting')
```

* Status: `execution_count`
> The counter for this execution is also provided so that clients can
> display it, since IPython automatically creates variables called _iN
> (for input prompt In[N]).

```python
execution_state : ('busy', 'idle', 'starting')
```


* Status: `execution_count`
> The counter for this execution is also provided so that clients can
> display it, since IPython automatically creates variables called _iN
> (for input prompt In[N]).

```python
execution_state : ('busy', 'idle', 'starting')
```
