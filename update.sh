#!/bin/bash
# Update script for AWS Lightsail or any other VPS.

# NOTE: permissions on VPS need to be updated before running this. 
#       Something like `chmod +x` should do the trick.

# enter appropriate directory
cd ~/RedstoneBot
# restart Node.js server for good measure
pm2 restart bot