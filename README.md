# StoreOnce 52xx Zabbix Monitoring

A set of tools for monitoring HPE StoreOnce 52xx devices using Zabbix.

## 📌 Overview

This project provides scripts and templates to integrate HPE StoreOnce 52xx devices into the Zabbix monitoring system, enabling health and performance tracking.

## 🧩 Contents

* storeonce.discovery — script for discovering StoreOnce devices
* storeonce.getdata — script for collecting metrics from devices
* storeonce.receive — script for processing collected data
* storeonce_monitoring_main.py — main Python script for monitoring execution
* zbx_export_templates.xml — Zabbix template for import

## ⚙️ Requirements

* Zabbix version 5.0 or later
* Python 3.6 or higher
* Network access to HPE StoreOnce 52xx devices

## 🚀 Installation & Configuration

* Clone the repository:

```bash
git clone https://github.com/laspavel/storeonce52xx-monitoring.git
```

* Import the zbx_export_templates.xml file into Zabbix.
* Configure connection parameters in the storeonce.discovery, storeonce.getdata, and storeonce.receive scripts.
* Schedule regular execution of scripts (e.g., via cron).

## 🛡️ License

MIT License.

## 🤝 Contributions

Suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## 📬 Contact

Author: [laspavel](https://github.com/laspavel)

Feel free to reach out with questions or ideas.

---