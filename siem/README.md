# Security Ingestion

## Summary
Using one of the famous opensource SIEM/XDR solution called Wazuh we can now take care of SIEM and XDR at the same time.
Wazuh is perfect for organization who are starting to shift left on their security without spending a large cost to implement SIEM and XDR.

# Simple SIEM Architecture
![Alt Text](../assets/wazuh_arch.png)

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
3. After install Wazuh the details below will appear to your Terminal. Take note of the username and password.

```
INFO: --- Summary ---
INFO: You can access the web interface https://<wazuh-dashboard-ip>
    User: admin
    Password: <ADMIN_PASSWORD>
INFO: Installation finished.
```
4. Open your web browser and access you wazuh server via hostname, domain or IP Address. <!-- Note the in production you'll need to map out a domain for your wazuh server -->
5. Login to your Wazuh Server and create a new agent. Follow the steps here in enrolling an agent ![Alt Text](https://documentation.wazuh.com/current/user-manual/agent/agent-enrollment/index.html) 
   <!-- There are options available for different types of device. Select the appropriate option for the machine where you want to deploy the Wazuh Agent -->
   <!-- In this example we will be using Windows Device -->
6. 




