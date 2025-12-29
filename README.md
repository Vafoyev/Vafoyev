<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=38BDF8&center=true&vCenter=true&width=600&lines=Hi+there,+I'm+Isobek+👋;Embedded+Systems+%26+Mobile+Architect;Building+Smart+Drone+Ecosystems+🚁;Bridging+C%2B%2B,+Flutter+%26+Algorithms" alt="Typing SVG" />

<br/>

<h3>🚀 Bridging Hardware & Software</h3>
<p>
I am a <b>Software Engineer</b> specializing in <b>Hard-Real-Time Drone Control Systems</b>. <br>
My passion lies in architecting the complete data flow: from <b>Embedded Sensors (ESP32/C++)</b> to <b>Cross-Platform Interfaces (Flutter)</b> using advanced SDKs.
</p>

<br/>

<table>
  <tr>
    <td align="center" width="33%">
      <h3>📱 Mobile & SDKs</h3>
      <img src="https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white" />
      <br/>
      <img src="https://img.shields.io/badge/Dart-%230175C2.svg?style=for-the-badge&logo=dart&logoColor=white" />
      <br/>
      <img src="https://img.shields.io/badge/Kotlin-%237F52FF.svg?style=for-the-badge&logo=kotlin&logoColor=white" />
      <br/>
      <img src="https://img.shields.io/badge/DJI_SDK-FF6600?style=for-the-badge&logo=dji&logoColor=white" />
      <br/>
      <img src="https://img.shields.io/badge/MyID_Auth-FF0000?style=for-the-badge" />
    </td>
    <td align="center" width="33%">
      <h3>🚁 Hardware & IoT</h3>
      <img src="https://img.shields.io/badge/C++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white" />
      <br/>
      <img src="https://img.shields.io/badge/ESP32-%23E7352C.svg?style=for-the-badge&logo=espressif&logoColor=white" />
      <br/>
      <img src="https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white" />
      <br/>
      <img src="https://img.shields.io/badge/Sensors-Gyro_|_Gas-orange?style=for-the-badge" />
      <br/>
      <img src="https://img.shields.io/badge/Protocols-UDP_|_MavLink-lightgrey?style=for-the-badge" />
    </td>
    <td align="center" width="33%">
      <h3>🧠 Core & Algos</h3>
      <img src="https://img.shields.io/badge/Java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white" />
      <br/>
      <img src="https://img.shields.io/badge/LeetCode-Top_199-yellow?style=for-the-badge&logo=leetcode&logoColor=black" />
      <br/>
      <img src="https://img.shields.io/badge/Git-%23F05032.svg?style=for-the-badge&logo=git&logoColor=white" />
      <br/>
      <img src="https://img.shields.io/badge/Architecture-Clean_Arch-blueviolet?style=for-the-badge" />
      <br/>
      <img src="https://img.shields.io/badge/Tools-Figma_|_Draw.io-purple?style=for-the-badge" />
    </td>
  </tr>
</table>

<br/>

<h3>🏗 System Architecture Visualization</h3>
<i>Data flow from Hardware Sensors to Mobile Interface</i>

</div>

```mermaid
graph LR
    classDef hardware fill:#e74c3c,stroke:#333,stroke-width:2px,color:white;
    classDef mobile fill:#3498db,stroke:#333,stroke-width:2px,color:white;
    classDef native fill:#9b59b6,stroke:#333,stroke-width:2px,color:white;
    classDef sdk fill:#2ecc71,stroke:#333,stroke-width:2px,color:white;
    classDef auth fill:#f1c40f,stroke:#333,stroke-width:2px,color:black;

    A["🚁 Hardware / Drone"]:::hardware
    B["📡 ESP32 / Controller"]:::hardware
    C{"📱 Mobile App (Flutter)"}:::mobile
    D["🤖 Native Android (Kotlin)"]:::native
    E["🎮 Flight Control (DJI SDK)"]:::sdk
    F["🔐 Biometrics (MyID)"]:::auth

    A -->| "Sensors Data (C++)" | B
    B -->| "MavLink / UDP" | C
    C -->| "Platform Channels" | D
    D -->| "Control Commands" | E
    C -->| "Auth Check" | F
