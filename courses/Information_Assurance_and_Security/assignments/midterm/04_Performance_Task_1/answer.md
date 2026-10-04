**Course Code: IT2511 | Information Assurance and Security (Data Privacy) - SY2627-1T**

**04 Performance Task 1: OT Attacks**

*Student:* Godwyn Neri | *Date:* October 3, 2026

---

### Direction
Analyze three (3) OT cyber threat scenarios. For each scenario, complete the OT Threat Evaluation Sheet focusing on OT Concept Application, Asset Identification, and Purdue Model Mapping (Part A: Steps 1, 2, and 4).

---

## Scenario 1: Spear Phishing -> IT-to-OT Pivot (Manufacturing)

### 1. OT Concept Application
In this scenario, the system is monitoring the factory's machines and assembly line during production. The engineer's computer and the plant monitoring screen track whether machines are running properly and meeting daily output targets. Even though the machines did not stop running, the hacker gained access to the monitoring screen and stole important plant setup files and daily activity records. This is dangerous because the stolen information gives the hacker the blueprints to mess with the machines later.

### 2. Asset Identification
| Asset | Physical or Logical | OT / IT / Mixed | Why (1 sentence) |
| :--- | :--- | :--- | :--- |
| Engineer's Computer | Physical Asset | IT | It is the office PC used by the engineer to check emails and do regular office work. |
| Phishing Email | Logical Asset | IT | It is a fake email containing a hidden virus link that tricked the engineer. |
| Remote Access Tool (RAT) | Logical Asset | Mixed | It is spyware secretly installed on the computer that gave the hacker remote control. |
| Plant Monitoring Screen (SCADA / HMI) | Physical Asset | OT | It is the screen on the factory floor that shows how machines are running in real time. |
| Factory Machine Controller (PLC) | Physical Asset | OT | It is the small computer that directly controls and runs the factory equipment. |
| Machine Setup Files | Logical Asset | OT | They are digital files containing the settings and instructions that tell the machines how to work. |
| Plant Activity Logs | Logical Asset | OT | They are history logs that record what the machines did and when errors happened. |
| Network Firewall | Physical Asset | Mixed | It is the security barrier that connects and protects the office network from the factory network. |

### 4. Purdue Model Mapping
| Purdue Level | Systems Affected | Reason |
| :--- | :--- | :--- |
| Level 5: Enterprise Network (IT Zone) | Office Email Server | The hacker sent the fake email through the company's regular internet and mail system. |
| Level 4: Business Logistics (IT Zone) | Engineer's PC | The engineer opened the bad email and accidentally installed the hacker's tool on this office PC. |
| Level 3: Operations / Plant Monitoring (OT Zone) | Plant Monitoring Screen (SCADA) | The hacker jumped from the office PC into this factory screen to view machine status and steal activity logs. |
| Level 2: Area Supervisory Control (OT Zone) | Machine Setup Files | The stolen configuration files hold the operating settings for the factory controllers. |

---

## Scenario 2: Protocol Abuse Against Legacy OT (Warehouse Automation)

### 1. OT Concept Application
In this warehouse, the system physically controls conveyor belts and robotic arms that move and sort packages. Small industrial computers called PLCs tell the belts how fast to roll and direct the robotic arms where to drop boxes. The system also manages the emergency stop feature, which immediately stops everything if there is an accident or danger. The attacker abused old communication rules to fake an emergency stop, freezing the whole warehouse and halting work.

### 2. Asset Identification
| Asset | Physical or Logical | OT / IT / Mixed | Why (1 sentence) |
| :--- | :--- | :--- | :--- |
| Conveyor Belts | Physical Asset | OT | They are motorized belts that physically carry packages across the warehouse. |
| Robotic Sorting Arms | Physical Asset | OT | They are robot arms that physically grab and sort boxes into different bins. |
| Conveyor Controllers (PLCs) | Physical Asset | OT | They are industrial computers that send run and stop signals to the belts and robots. |
| Emergency Stop Button / Relays | Physical Asset | OT | They are safety switches designed to cut power and halt all machines instantly. |
| Old Industrial Protocol (Modbus / CAN bus) | Logical Asset | OT | It is the old communication language used by machines that has no password or security checks. |
| Fake Stop Command | Logical Asset | OT | It is a forged signal sent by the hacker that falsely told the machines to shut down. |
| Controller Program Code | Logical Asset | OT | It is the code saved inside the PLC that defines how boxes are sorted and when stops happen. |
| Network Converter / Bridge | Physical Asset | Mixed | It is the box connecting modern network cables to old machine wiring. |

### 4. Purdue Model Mapping
| Purdue Level | Systems Affected | Reason |
| :--- | :--- | :--- |
| Level 2: Area Supervisory Control (OT Zone) | Warehouse Control Screen / Gateway | The hacker used this interface to inject the unauthorized stop command into the machine network. |
| Level 1: Basic Control (OT Zone) | Machine Controllers (PLCs) | The PLCs received the fake stop command and told the equipment to shut off. |
| Level 0: Physical Process (OT Zone) | Conveyor Belts and Robotic Arms | The actual moving machines and safety switches that suddenly froze on the warehouse floor. |

---

## Scenario 3: DoS in Industrial Network (Utilities / Smart City)

### 1. OT Concept Application
In this smart city setup, the system controls and monitors public charging stations that deliver electricity to electric cars. Central servers track which chargers are in use, handle driver billing, and monitor power levels. Inside each charger, physical power switches turn electricity on or off safely when a car plugs in. The attack flooded the chargers with junk traffic and messed up their network settings, so they could no longer talk to the main server and stopped charging cars.

### 2. Asset Identification
| Asset | Physical or Logical | OT / IT / Mixed | Why (1 sentence) |
| :--- | :--- | :--- | :--- |
| EV Charging Stations | Physical Asset | OT | They are physical roadside charging boxes where drivers plug in their cars. |
| Power Switches (Relays) | Physical Asset | OT | They are internal electrical switches that physically turn power on or off to the car cable. |
| Central Charging Server | Physical Asset | Mixed | It is the main computer that monitors charger status, handles billing, and sends commands. |
| Charger Circuit Board (Microcontroller) | Physical Asset | OT | It is the built-in mini-computer inside each station that controls the physical charging process. |
| IP Address Settings | Logical Asset | Mixed | They are network settings that tell the chargers what address to use on the network. |
| Charging Communication Protocol | Logical Asset | Mixed | It is the messaging system used by chargers to send status and billing data back to the server. |
| Junk Traffic Flood (DoS Packets) | Logical Asset | IT | They are huge streams of fake requests sent by the hacker to clog up the chargers' memory. |
| City Network Router | Physical Asset | Mixed | It is the networking hardware connecting roadside chargers to the city's main computer network. |

### 4. Purdue Model Mapping
| Purdue Level | Systems Affected | Reason |
| :--- | :--- | :--- |
| Level 4 / Level 5: Enterprise / City IT (IT Zone) | Central Charging Server | The main city dashboard lost contact with the charging stations and could no longer manage them. |
| Level 2 / Level 3: Area Supervisory / Network (OT Zone) | Field Routers | The local routers got overloaded by junk traffic, blocking normal messages from getting through. |
| Level 1: Basic Control (OT Zone) | Charger Microcontrollers | The internal chips inside the chargers received bad IP settings and stopped responding to commands. |
| Level 0: Physical Process (OT Zone) | Power Relays and Charging Cables | The physical parts that plug into cars and deliver electricity could not turn on because of the communication loss. |

---

## Supplementary Reference (Handout-Grounded Steps 3 & 5)

| Scenario | 3. Threat Type Classification (Handout-Based) | 5. OT Weaknesses (Handout-Grounded) |
| :--- | :--- | :--- |
| **Scenario 1** | • **Spear Phishing**: Attacker sent a fake email to trick the engineer.<br>• **Data Leakage**: Stole plant settings and machine history logs. | 1. No strict separation between office computers and plant screens.<br>2. Weak email security that allowed the malware to run. |
| **Scenario 2** | • **Protocol Abuse**: Abused old machine languages (Modbus/CAN bus).<br>• **Potential Destruction of ICS Resources**: Forced sudden emergency stops that halted operations. | 1. Old machine protocols do not require passwords or security checks.<br>2. Machine networks lacked barriers to block unauthorized commands. |
| **Scenario 3** | • **Denial-of-Service Attacks**: Flooded chargers with junk traffic.<br>• **Exploiting Unpatched Vulnerabilities**: Chargers accepted bad network changes without verification. | 1. No traffic limits to stop chargers from getting overwhelmed.<br>2. Devices allowed network settings to be changed without an admin password. |
