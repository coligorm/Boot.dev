def choose_command(command, start_fn, stop_fn):
    match command:
        case "start":
            return start_fn()
        case "stop":
            return stop_fn()
        case _:
            return "unknown command"
        
