# Command Function Chooser

**Complete the `choose_command` function.**

It should take:

- a command string
- a `start_fn` function
- a `stop_fn` function

Return the result of:

- `start_fn()` when the command is `"start"`
- `stop_fn()` when the command is `"stop"`
- `"unknown command"` for anything else

## Rules

1. Compare the command using simple exact matches.
2. Only call one of the two functions when the command is known.
3. If the command is unknown, return "unknown command".
4. Unknown commands include values like "pause", "", and "START".

## Example

```
def start_engine():
    return "engine started"


def stop_engine():
    return "engine stopped"

print(choose_command("start", start_engine, stop_engine))
# engine started

print(choose_command("stop", start_engine, stop_engine))
# engine stopped

print(choose_command("pause", start_engine, stop_engine))
# unknown command
```
