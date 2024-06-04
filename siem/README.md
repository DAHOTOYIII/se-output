# Security Ingestion

## Summary
Using one of the famous opensource SIEM/XDR solution called Wazuh we can now take care of SIEM and XDR at the same time.
Wazuh is perfect for organization who are starting to shift left on their security without spending a large cost to implement SIEM and XDR.

### Requirements
- Hardware
  
![Alt Text](../assets/hardware_req.png)

- System

![Alt Text](../assets/Sysem_req.png)

### The Goal
The goal is to setup Wazuh and install agents on each of the endpoints.

### Wazuh Installation:
1. Create an ubuntu server based on the Requirements above.
2. SSH to your server and run this command.
``` curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh && sudo bash ./wazuh-install.sh -a ```
3. 



