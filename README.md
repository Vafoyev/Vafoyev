<div align="center">

<!-- 1. DINAMIK HEADER (Yozilib turadigan animatsiya) -->
<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=30&duration=3000&pause=1000&color=38BDF8&center=true&vCenter=true&width=600&lines=Hi+there,+I'm+Isobek+👋;Embedded+Systems+%26+Mobile+Architect;Building+Smart+Drone+Ecosystems+🚁" alt="Typing SVG" />

<br/>

<!-- 2. QISQA BIO -->
<h3>🚀 Bridging Hardware (C++) & Mobile (Flutter)</h3>
<p>
I specialize in building <b>Hard-Real-Time Drone Control Systems</b>. <br>
I don't just write apps; I architect the entire flow from <b>Sensors (ESP32)</b> to <b>User Interfaces (Flutter/Kotlin)</b> using complex SDKs.
</p>

---

<!-- 3. TEXNOLOGIYALAR STACKI (Rangli Badges) -->
<h3>🛠 Tech Stack & Arsenal</h3>

<!-- Mobile Section -->
<img src="https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white" />
<img src="https://img.shields.io/badge/Dart-%230175C2.svg?style=for-the-badge&logo=dart&logoColor=white" />
<img src="https://img.shields.io/badge/Kotlin-%237F52FF.svg?style=for-the-badge&logo=kotlin&logoColor=white" />
<img src="https://img.shields.io/badge/DJI_SDK-FF6600?style=for-the-badge&logo=dji&logoColor=white" />
<img src="https://img.shields.io/badge/MyID_Auth-FF0000?style=for-the-badge" />

<br/><br/>

<!-- Hardware Section -->
<img src="https://img.shields.io/badge/C++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white" />
<img src="https://img.shields.io/badge/ESP32_SoC-E7352C?style=for-the-badge&logo=espressif&logoColor=white" />
<img src="https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white" />
<img src="https://img.shields.io/badge/Sensors-Gyro_|_Gas-orange?style=for-the-badge" />

<br/><br/>

<!-- Algorithms Section -->
<img src="https://img.shields.io/badge/Java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white" />
<img src="https://img.shields.io/badge/LeetCode-Top_199_Solved-yellow?style=for-the-badge&logo=leetcode&logoColor=black" />

</div>

---

<!-- 4. RANGLI ARXITEKTURA DIAGRAMMASI (Eng muhim joyi) -->
### 🧠 System Architecture Visualization
*How I build Drone Control Systems (Hardware to Mobile Flow):*

```mermaid
graph LR
    %% Stil berish (Ranglar)
    classDef hardware fill:#e74c3c,stroke:#333,stroke-width:2px,color:white;
    classDef mobile fill:#3498db,stroke:#333,stroke-width:2px,color:white;
    classDef native fill:#9b59b6,stroke:#333,stroke-width:2px,color:white;
    classDef sdk fill:#2ecc71,stroke:#333,stroke-width:2px,color:white;
    classDef auth fill:#f1c40f,stroke:#333,stroke-width:2px,color:black;

    %% Nodes (Tugunlar)
    A["🚁 Hardware / Drone"]:::hardware
    B["📡 ESP32 / Controller"]:::hardware
    C{"📱 Mobile App (Flutter)"}:::mobile
    D["🤖 Native Android (Kotlin)"]:::native
    E["🎮 Flight Control (DJI SDK)"]:::sdk
    F["🔐 Biometrics (MyID)"]:::auth

    %% Connections (Bog'lanishlar)
    A -->| "Sensors Data (C++)" | B
    B -->| "MavLink / UDP" | C
    C -->| "Platform Channels" | D
    D -->| "Control Commands" | E
    C -->| "Auth Check" | F
