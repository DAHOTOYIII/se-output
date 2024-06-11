#Mock Security Automation Playbook

## Below is a Flow Diagram of a mock Phishing Email Security Automation
This workflow represents an automated checking of emails.
The workflow is triggered everytime an email is received in the mailbox of the user.
It will then get the email message extract the details like attachments, URL, messageID.
Using these information the automation can query public threat intelligence tools like virus total, crowsec and metadefender via API
using the indicators of compromise and set of predefined rules that automation will give verdict whether this email is malicious or not and block the email address if necessary.

![Playbook](../assets/sampleplaybook1.png)

