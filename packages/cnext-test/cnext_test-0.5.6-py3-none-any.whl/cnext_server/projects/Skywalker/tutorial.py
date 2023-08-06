# # Quick Guide
# #### Key concepts
# In CNext, a set of lines can be grouped into a `group`. These grouped lines
# can be executed together interactively similar to a `cell` in Jupyter Notebook.
# 
# #### Shortcut Keys
# All shortcut keys are defined in file __`./config.json`__. 
# Important keys are:
# ##### Group Related Commands
# - __`Ctrl[Cmd]+G`__: create a new group on a selected lines or the line where
# the cursor is.
# - __`Ctrl[Cmd]+U`__: to ungroup a grouped line.
# - __`Ctrl[Cmd]+Shift+G`__: insert a blank group below.
# - __`Ctrl[Cmd]+Shift+L`__: insert a blank line below.
# ##### Code Folding
# - __`Ctrl[Cmd]+Shift+F`__: fold all code including grouped code
# - __`Ctrl[Cmd]+Shift+U`__: unfold all code including grouped code
# - __`Ctrl[Cmd]+Shift+C`__: fold a code section
# - __`Ctrl[Cmd]+Shift+V`__: unfold a code section
# ##### Execute Commands
# - __`Ctrl[Cmd]+Enter`__: execute the group or line where the cursor is.
# - __`Ctrl[Cmd]+Shift+Enter`__: exectue the group then move the cursor to the next group.
# - __`Shift+A`__: turn on/off code auto-completion
# - __`Shift+L`__: turn on/off code analysis more to come


import os
print(os.getcwd())

