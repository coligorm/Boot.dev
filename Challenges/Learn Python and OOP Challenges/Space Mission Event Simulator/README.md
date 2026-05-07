# Space Mission Event Simulator

## Build a small mission simulator using classes.

### Task

Complete the `Ship` and `Mission` classes, plus the `simulate_mission` function.

The mission is a simple frame-by-frame event loop, similar to processing actions in a game:

- a ship starts with `100` health and `10` energy
- events are processed in order
- each event changes the ship's state
- if the ship is destroyed, the mission stops immediately

### Event types

Each event is a dictionary with a `type` key.

#### `mine`

A mining event looks like this:

```
{"type": "mine", "item": "iron", "amount": 3, "energy": 4}
```

Rules:

- If the ship has enough energy, subtract the energy cost and add the item to `cargo`
- If it does not have enough energy, do not change cargo or energy
- Add one log entry:
    - success: `"Mined iron x3"`
    - failure: `"Skipped iron"`

#### `hit`

```
{"type": "hit", "damage": 25}
```

Rules:

- Subtract damage from health
- Health cannot go below `0`
- Add log entry: `"Took 25 damage"`
- If health becomes `0`, also add `"Ship destroyed"` and stop the mission immediately

#### `charge`

```
{"type": "charge", "energy": 6}
```

Rules:

- Add the given amount to the ship's energy
- Add log entry: `"Charged 6 energy"`

#### `repair`

```
{"type": "repair", "health": 20}
```

Rules:

- Add the given amount to health
- Health cannot go above `100`
- Add log entry: `"Repaired 20 health"`

### Required behavior

#### `Ship`

Your `Ship` class should:

- store `name`, `health`, `energy`, and `cargo`
- start with an empty cargo dictionary
- support these methods:
    - `mine(item, amount, energy_cost)`
    - `take_hit(damage)`
    - `charge(amount)`
    - `repair(amount)`
    - `is_destroyed()`
    - `cargo_text()`

#### `cargo_text()`

Return cargo as a readable string in insertion order.

Examples:

- no cargo -> `"empty"`
- `{"iron": 3}` -> `"iron:3"`
- `{"iron": 3, "ice": 2}` -> `"iron:3, ice:2"`

#### `Mission`

Your `Mission` class should:

- store the ship and the event list
- keep a `log` list
- process events in order with a `run()` method

#### `simulate_mission(name, events)`

This function should:

1. create the ship
2. create the mission
3. run the mission
4. return a summary dictionary with exactly these keys:
```
{
    "pilot": name,
    "health": final_health,
    "energy": final_energy,
    "cargo": final_cargo_dict,
    "cargo_text": readable_cargo_string,
    "log": mission_log,
}
```