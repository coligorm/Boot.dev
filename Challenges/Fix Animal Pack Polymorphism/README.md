# Fix Animal Pack Polymorphism

The classes in `main.py` are supposed to model an animal pack using polymorphism.

Right now, the code has a few problems:
- `Pack.sounds()` is not using each subclass's own `speak()` method correctly
- `__str__`does not show the right class name
- `__eq__` treats different animal types as equal when they only share a name
- `Pack + Pack` does not build the combined pack correctly

## Expected behavior

Each animal subclass should provide its own sound:
- `Dog` -> `"woof"`
- `Cat` -> `"meow"`
- `Parrot` -> `"squawk"`

Converting an animal to a string with `str(...)` should return:
```
"ClassName: Name"
```
So:
```
str(Dog("Rex"))
# "Dog: Rex"
```
Two animals should only be equal if they have:
- the same name
- the same subclass

So these should behave like this:
```
Dog("Rex") == Dog("Rex")
# True

Dog("Rex") == Cat("Rex")
# False
```
Adding two packs with `+` should return a **new** `Pack` containing all animals from the left pack followed by all animals from the right pack.