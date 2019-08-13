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

![Classic Tupper](images/tupper_classic.png)

Now we use the k number for the "Sick" bmp from http://keelyhill.github.io/tuppers-formula/ , by shifting down along the y axis by the difference divided by the stantard height 17. Then, we save the result, i.e. :
```python
# "Sick" k from http://keelyhill.github.io/tuppers-formula/
k_sick = mp.mpf("19990658104895992159906328363638101787663851414537751539476865503218289618184076530123376594191"
                "24042366024039498437918666302237803582546013046303926310513280468110193127095922276315009796499"
                "31518795365589332244156816053373014059549452066117357397504861137579902513441094521287520230019"
                "51866779239406656151423658961709308717100436684082889189269813403152930991277247967173513256539"
                "22379772695517817049137311869862432577488386845165968713631941327344461868561513599475049479806"
                "55286675865714081044922472071253")

# Taking the difference divided by 17, and passing it to the method
k_diff = (T.k - k_sick) / 17

T.plot_tupper(-k_diff)
plt.savefig(os.path.join("images", "tupper_sick.png"))
```
The result is shown below.

![Classic Tupper](images/tupper_sick.png)
