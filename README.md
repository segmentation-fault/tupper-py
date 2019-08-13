# tupper-py

## Introduction
Implements a class that plots [Tupper's self-referencing formula](https://en.wikipedia.org/wiki/Tupper%27s_self-referential_formula) at custom shifts, up and down the vertical axis. [There is a nice video by Matt Parker](https://www.youtube.com/watch?v=_s5RFgd59ao) explaining the formula.

## Example
First we instantiate the class:
```python
T = TupperPy()
```
Then we save the original Tupper's bitmap, by calling the `plot_tupper` method without arguments:
```python
T.plot_tupper()
plt.savefig(os.path.join("images", "tupper_classic.png"))
```
The result is shown below.
