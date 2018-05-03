# pagemonitoring

Simple page monitoring app

Configuration in ansible/roles/pagemonitor/files/config.json.
Polls configured sites and logs response times into a file.

Can be installed to localhost using following command in ansible directory

```$ ansible-playbook -i inventory.yaml install_pagemonitor.yaml --ask-become-pass```

Tested with Ubuntu 14.04
