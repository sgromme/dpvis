# DPVIS
# Evaluation of visualization of dynamic programming for Open Supply Planning

# create a python virtual
```console
python3 -m venv .venv
```
# activate virtual
source .venv/bin/activate
# install dpvis
pip install dpvis


# Running demos
Create a Python environment with module venv

Had to run this to run locally, other wise the demos couldn't
find dpvis module even with them install in the Python Envirionment.
which was install with 

```console

export PYTHONPATH=/home/sgromme/source/dpvis:$PYTHONPATH

```
Can you explain why the code in knapsack.py can't find this method on visualizer.create_app() when the dpvis package has been installed in the python environment, I have to run this on the command line export PYTHONPATH=/home/sgromme/source/dpvis:$PYTHONPATH for it to work?

If I start the Python REPL in the python virtual environment and import dp.  I then look at the dir(dp._visualizer.Visualizer) which shows this ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_attach_callbacks', '_create_figure', '_parse_timesteps', '_show_figure_trace', 'add_array', 'app', 'create_app', 'show'], it seems like the 'create_app'  method is there?


import dp._visualizer
print("Visualizer loaded from:", dp._visualizer.__file__)