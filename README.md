### Hi there, I'm Isobek 👋
#### 🚁 Embedded Systems & Mobile Engineering Architect

I specialize in building **Hard-Real-Time Drone Control Systems**. I don't just write apps; I bridge the gap between **Hardware (Sensors/C++)** and **User Interfaces (Flutter/Kotlin)** using complex SDKs.

---

### 🛠 Tech Stack & Tools

**Mobile & SDKs:**
![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white)
![Dart](https://img.shields.io/badge/dart-%230175C2.svg?style=for-the-badge&logo=dart&logoColor=white)
![Kotlin](https://img.shields.io/badge/kotlin-%237F52FF.svg?style=for-the-badge&logo=kotlin&logoColor=white)
![DJI SDK](https://img.shields.io/badge/SDK-DJI%20%2F%20Autel-black?style=for-the-badge)
![MyID](https://img.shields.io/badge/Biometrics-MyID-red?style=for-the-badge)

**Hardware & IoT:**
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)
![ESP32](https://img.shields.io/badge/SoC-ESP32-red?style=for-the-badge&logo=espressif&logoColor=white)
![Sensors](https://img.shields.io/badge/Sensors-Gyro%20%7C%20Gas%20%7C%20GPS-orange?style=for-the-badge)

**Core & Algorithms:**
![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white)
![Algorithms](https://img.shields.io/badge/LeetCode-Top%20199%20Solved-yellow?style=for-the-badge)

---

### 🧠 System Architecture Visualization
*How I build Drone Control Systems:*

```mermaid
graph LR
    A[Hardware / Drone] -->|Sensors Data (C++)| B(ESP32 / Controller)
    B -->|MavLink / UDP| C{Mobile App (Flutter)}
    C -->|Platform Channels| D[Native Android (Kotlin)]
    D -->|DJI / Autel SDK| E[Flight Control]
    C -->|Biometrics| F[MyID Auth]
