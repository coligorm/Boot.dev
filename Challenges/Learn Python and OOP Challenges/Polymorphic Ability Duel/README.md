# Polymorphic Ability Duel

Build a small ability system using inheritance, polymorphism, and operator overloading.

Complete these classes and functions in main.py:

- ``Ability``
- ``FireAbility``
- ``IceAbility``
- ``WindAbility``
- ``get_strongest_ability``

## Requirements

### 1. Base class: ``Ability``

- Store the ability ``name``
- Define a ``power()`` method
- Overload ``+`` so adding two abilities returns the sum of their power values
- Overload ``>`` so one ability can be compared to another by power

### 2. Subclasses

Each subclass should inherit from ``Ability`` and calculate power differently:

- ``FireAbility(name, flames)`` → power is ``flames * 4``
- ``IceAbility(name, shards)`` → power is ``shards * 3``
- ``WindAbility(name, gusts)`` → power is ``gusts + 5``

### 3. ``get_strongest_ability(abilities)``

Return the **name** of the strongest ability in the list.

- Use the ability objects directly
- If the list is empty, return ``None``
- If multiple abilities tie for strongest, return the first one that reached that highest power

## Example

```
meteor = FireAbility("Meteor", 4)
frost = IceAbility("Frost Lance", 3)
breeze = WindAbility("Breeze Kick", 2)

print(meteor.power())
# 16

print(meteor + breeze)
# 23

print(meteor > frost)
# True

print(get_strongest_ability([frost, meteor, breeze]))
# "Meteor"
```

## Notes

- The point of this challenge is that the same code should work with different ability types
- ``get_strongest_ability`` should rely on shared behavior, not separate logic for each subclass
- Keep ``main.py`` focused on class and function definitions only


