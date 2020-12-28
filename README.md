# RedstoneBot

The goal of this branch is to migrate bot functionality from Selenium to [Requests](https://requests.readthedocs.io/en/master/), whenever possible. 

This should improve performance and reduce the number of dependencies.


## Commands that now use Requests

No commands use Requests, yet!

## To-do List

* Migrate from Selenium to Requests:
  * `login()` function
  * `!redstone status` command
