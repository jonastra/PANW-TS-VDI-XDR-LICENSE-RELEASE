# DESCRIPTION

This script is used to adjust the time it takes for licenses to be released in TS/VDI environments where you can hit license limit when servers reboot.
Servers can stay unprotected for up to 90 minutes or more.

# GUIDE

1. Make sure to install Python 3 and it's dependencies using pip3: requests, json
2. Run script to verify that the correct filters are being used and you only delete intended endpoints.
3. Uncomment delete_all_inactive_endpoints() below main() function to delete.
4. Run script every 5-10 minutes or so using your preferred tool.

# LEGEND

Connection Lost — The Cortex XDR agent has not checked in within 30 to 180 days for standard endpoints, and between 90 minutes and 6 hours for VDI and temporary sessions.

Disconnected — The Cortex XDR agent has checked in within the defined inactivity window: between 10 minutes and 30 days for standard endpoints, and between 10 minutes and 90 minutes for VDI and temporary sessions.

# LIMITATIONS / IMPROVEMENTS
- Check and filter on endpoint group. (limitation in "GET ALL ENDPOINTS" demands 2 API calls)

# VERSIONS
- 0.1: Not tested properly.