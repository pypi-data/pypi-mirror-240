import pyperclip
from textwrap import dedent
from jcopdl.utils.nb_check import IN_NOTEBOOK


def _copy_snippet(snippet):
    pyperclip.copy(dedent(snippet)[1:-1])
    if IN_NOTEBOOK:
        from IPython.display import HTML
        return HTML("""
            <style>
                /* Style for the box */
                .box {
                    background-color: #008000;
                    color: white;
                    padding: 5px 10px;
                    line-height: 30px;
                    border-radius: 5px;
                }
            </style>
            <span class="box">Copied &#10003;</span>
        """)
