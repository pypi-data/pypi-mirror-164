<!-- #region -->
# `debuglater`: Store Python traceback for later debugging


<p align="center">
  <a href="https://ploomber.io/community">Community</a>
  |
  <a href="https://www.getrevue.co/profile/ploomber">Newsletter</a>
  |
  <a href="https://twitter.com/ploomber">Twitter</a>
  |
  <a href="https://www.linkedin.com/company/ploomber/">LinkedIn</a>
  |
  <a href="https://ploomber.io/">Blog</a>
  |
  <a href="https://www.ploomber.io">Website</a>
  |
  <a href="https://www.youtube.com/channel/UCaIS5BMlmeNQE4-Gn0xTDXQ">YouTube</a>
</p>

- `debuglater` writes the traceback object so you can use it later for debugging
- Works with `pdb`, `pudb`, `ipdb` and `pdbpp`
- You can use it to debug on a different machine, no need to have access to the source code

For support, feature requests, and product updates: [join our community](https://ploomber.io/community), subscribe to our [newsletter](https://www.getrevue.co/profile/ploomber) or follow us on [Twitter](https://twitter.com/ploomber)/[LinkedIn](https://www.linkedin.com/company/ploomber/).

![demo](https://ploomber.io/images/doc/debuglater-demo/debug.gif)


[Click here to tell your friends on Twitter!](https://twitter.com/intent/tweet?text=I%20just%20discovered%20debuglater%20on%20GitHub%3A%20serialize%20Python%20tracebacks%20for%20later%20debugging%21%20%F0%9F%A4%AF&url=https://github.com/ploomber/debuglater/)

[Click here to tell your friends on LinkedIn!](https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/ploomber/debuglater/)

## Installation

```sh

pip install debuglater

# for better serialization support (via dill)
pip install 'debuglater[all]'
```

## Usage

```python
import sys
import debuglater

sys.excepthook = debuglater.excepthook_factory(__file__)
```

For more details and alternative usage, keep reading.

<!-- #endregion -->

## Example

```sh
# get the example
curl -O https://raw.githubusercontent.com/ploomber/debuglater/master/examples/crash.py
```

```sh tags=["raises-exception"]
# crash
python crash.py
```

<!-- #region -->
Debug:

```sh
dltr crash.dump
```

Upon initialization, try printing the variables `x` and `y`:

```
Starting pdb...
> /Users/ploomber/debuglater/examples/crash.py(5)<module>()
-> x / y
(Pdb) x
1
(Pdb) y
0
(Pdb) quit
```

*Note: you can also use:* `debuglater crash.py.dump`

<!-- #endregion -->

<!-- #region -->
## Integration with Jupyter/IPython

> **Note**
> For an integration with papermill, see [ploomber-engine](https://github.com/ploomber/ploomber-engine)

Add this at the top of your notebook/script:

```python
from debuglater import patch_ipython
patch_ipython()
```
<!-- #endregion -->

```sh
# get sample notebook
curl -O https://raw.githubusercontent.com/ploomber/debuglater/master/examples/crash.ipynb

# install package to run notebooks
pip install nbclient
```

```sh tags=["raises-exception"]
# run the notebook
jupyter execute crash.ipynb
```

Debug:

```
dltr jupyter.dump
```

Upon initialization, try printing the variables `x` and `y`:

```
Starting pdb...
-> x / y
(Pdb) x
1
(Pdb) y
0
(Pdb) quit
```


*Note: you can also use:* `debuglater jupyter.dump`

## Motivation

The [Ploomber team](https://github.com/ploomber/ploomber) develops tools for
data analysis. When data analysis code executes non-interactively
(example: a daily cron job that generates a report), it becomes hard to debug
since logs are often insufficient, forcing data practitioners to re-run the
code from scratch, which can take a lot of time.

However, `debuglater` is a generic tool that can be used for any use case to facilitate post-mortem debugging.

## Use cases

* Debug long-running code (e.g., crashed Machine Learning job)
* Debug multiprocessing code (generate one dump file for each process)

## Credits

This project is a fork of [Eli Finer's pydump](https://github.com/elifiner/pydump).
