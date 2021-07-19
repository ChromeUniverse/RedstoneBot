# RedstoneBot

This is the source code folder. Includes Python and bash scripts.

## Folder Structure

```
.
├── code                            # source code directory
    ├── activate.py                 # main logic for `start` command
    ├── bot.py                      # main bot file
    ├── db.csv                      # CSV database
    ├── db_funcions.py              # database read/write functions
    ├── deactivate.py               # main logic for `stop` command
    ├── format_help.py              # formats the `help` command Rich Embed
    ├── format_list.py              # formats the `list` command Rich Embed
    ├── format_queuetime.py         # formats the `time` command Rich Embed
    ├── format_status.py            # formats the `status` command Rich Embed
    ├── get_list.py                 # gets online player list through server console
    ├── get_status.py               # gets server status
    ├── get_times.py                # gets queue waiting times
    ├── leave_queue.py              # main logic for `exit` command
    ├── login.py                    # logs in to ploudos.com at startup
    ├── online_player_count.py      # gets the number of online players
    ├── reactivate.py               # main logic for `restart` command
    ├── register.py                 # main logic for `setup` command
    ├── role_functions.py           # functions for user roles
    ├── server_name.py              # gets the name of the server
    ├── serverlist.py               # gets list of servers shared with RedstoneBot
    ├── tester_setup.py             # setup variables for tester bot
    ├── tester.py                   # main file for tester bot
    └── unregister.py               # main logic for `reset` command
```
