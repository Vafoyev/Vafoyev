<div align="center">

<a href="https://github.com/Vafoyev">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=28&duration=3000&pause=1000&color=2196F3&center=true&vCenter=true&width=800&lines=Hi+there%2C+I'm+Vafoyev+%F0%9F%91%8B;Embedded+Systems+%26+Mobile+Architect;Building+Hard-Real-Time+Drone+Systems+%F0%9F%9A%81;C%2B%2B+%7C+Flutter+%7C+Algorithms+%E2%9A%A1" alt="Typing SVG" />
</a>

<br/>

<!-- Profile Views Counter -->
<img src="https://komarev.com/ghpvc/?username=Vafoyev&color=2196F3&style=flat-square&label=Profile+Views" alt="Profile views" />

<br/><br/>

<h3 style="border-bottom: 3px solid #2196F3; display: inline-block; color: #ffffff;">
    🎯 SYSTEM ARCHITECT PROFILE
</h3>
<p style="font-size: 16px; max-width: 750px; color: #b0b0b0; line-height: 1.7;">
    <b>Software Engineer</b> specializing in complex <b>IoT & Drone Telemetry Systems</b>. <br>
    Bridging the gap between <b>Hardware (ESP32/C++)</b> and <b>Mobile Interfaces (Flutter)</b> <br>
    using custom protocols, real-time communication, and industrial SDKs.
</p>

<br/>

---

### 💼 **TECH STACK & EXPERTISE**

<table border="0" width="100%" cellspacing="0" cellpadding="12">
  <thead>
    <tr>
      <th align="center" width="33%">
        <img src="https://img.shields.io/badge/📱_MOBILE_DEVELOPMENT-02569B?style=for-the-badge&logo=flutter&logoColor=white" />
      </th>
      <th align="center" width="33%">
        <img src="https://img.shields.io/badge/⚙️_HARDWARE_&_IoT-E7352C?style=for-the-badge&logo=espressif&logoColor=white" />
      </th>
      <th align="center" width="33%">
        <img src="https://img.shields.io/badge/🔧_CORE_ENGINEERING-ED8B00?style=for-the-badge&logo=java&logoColor=white" />
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" valign="top">
        <br/>
        <img src="https://img.shields.io/badge/Flutter-Framework-02569B?style=flat-square&logo=flutter&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/Dart-Language-0175C2?style=flat-square&logo=dart&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/Kotlin-Android-7F52FF?style=flat-square&logo=kotlin&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/DJI_SDK-Enterprise-black?style=flat-square&logo=dji&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/Autel_SDK-Robotics-orange?style=flat-square&logo=autodesk&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/MyID-Biometrics-red?style=flat-square" /><br/>
        <img src="https://img.shields.io/badge/Clean_Architecture-MVVM-blueviolet?style=flat-square" />
      </td>
      <td align="center" valign="top">
        <br/>
        <img src="https://img.shields.io/badge/C++-Embedded-00599C?style=flat-square&logo=c%2B%2B&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/ESP32-SoC-E7352C?style=flat-square&logo=espressif&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/Arduino-Platform-00979D?style=flat-square&logo=arduino&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/Sensors-MPU6050_|_MQ2-orange?style=flat-square" /><br/>
        <img src="https://img.shields.io/badge/Protocol-UDP_|_MavLink-lightgrey?style=flat-square" /><br/>
        <img src="https://img.shields.io/badge/Real--Time-FreeRTOS-green?style=flat-square" />
      </td>
      <td align="center" valign="top">
        <br/>
        <img src="https://img.shields.io/badge/Java-Algorithms-ED8B00?style=flat-square&logo=openjdk&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/LeetCode-199_Solved-FFA116?style=flat-square&logo=leetcode&logoColor=black" /><br/>
        <img src="https://img.shields.io/badge/Git-Control-F05032?style=flat-square&logo=git&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/GitHub-Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/Design-Figma-F24E1E?style=flat-square&logo=figma&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/REST-API-009688?style=flat-square" />
      </td>
    </tr>
  </tbody>
</table>

<br/>

---

### 🏗️ **SYSTEM ARCHITECTURE**
<i style="color: #888888;">End-to-End Data Flow: Sensors → Controller → Mobile App → Cloud</i>

```mermaid
graph LR
    A["🛸 HARDWARE UNIT<br/>(Drone Frame)"]
    B[("⚡ ESP32 CONTROLLER<br/>(C++ Logic)")]
    C{"📱 MOBILE APP<br/>(Flutter UI)"}
    D["🔗 NATIVE BRIDGE<br/>(Kotlin/Android)"]
    E["🎮 SDK CONTROLLER<br/>(DJI / AUTEL)"]
    F["🔐 AUTH SERVICE<br/>(MyID)"]

    A -->|Raw Sensor Data| B
    B == "UDP / MavLink" ==> C
    C -. "MethodChannel" .-> D
    D -->|Commands| E
    C -- "Verify User" --> F

    classDef hardware fill:#E7352C,stroke:none,color:white,font-weight:bold;
    classDef mobile fill:#02569B,stroke:none,color:white,font-weight:bold;
    classDef native fill:#7F52FF,stroke:none,color:white,font-weight:bold;
    classDef sdk fill:#00C853,stroke:none,color:white,font-weight:bold;
    classDef auth fill:#FFD600,stroke:none,color:black,font-weight:bold;

    class A,B hardware;
    class C mobile;
    class D native;
    class E sdk;
    class F auth;
```

<br/>

---

### 🚀 **FEATURED PROJECTS**

<table>
<tr>
<td width="50%">

#### 🎯 Drone Telemetry System
Real-time drone control and monitoring
- ESP32 + MPU6050 sensor fusion
- UDP telemetry @ 50Hz
- Flutter cross-platform UI
- Custom MavLink integration

</td>
<td width="50%">

#### 📱 Mobile-Hardware Bridge
Enterprise SDK integration platform
- DJI Mobile SDK 5.x
- Autel SDK integration
- Native Kotlin bridge
- Biometric auth (MyID)

</td>
</tr>
</table>

<br/>

---

### 📊 **GITHUB STATISTICS**

<table border="0" width="100%">
<tr>
<td width="50%" align="center">
<a href="https://github.com/Vafoyev">
<img src="https://github-readme-stats.vercel.app/api?username=Vafoyev&show_icons=true&theme=radical&hide_border=true&title_color=2196F3&text_color=b0b0b0&icon_color=2196F3&bg_color=0d1117" alt="GitHub Stats" />
</a>
</td>
<td width="50%" align="center">
<a href="https://github.com/Vafoyev">
<img src="https://github-readme-streak-stats.herokuapp.com/?user=Vafoyev&theme=radical&hide_border=true&background=0d1117&stroke=2196F3&ring=2196F3&fire=FF6D00&currStreakLabel=2196F3" alt="GitHub Streak" />
</a>
</td>
</tr>
<tr>
<td colspan="2" align="center">
<a href="https://github.com/Vafoyev">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Vafoyev&layout=compact&theme=radical&hide_border=true&title_color=2196F3&text_color=b0b0b0&bg_color=0d1117" alt="Top Languages" />
</a>
</td>
</tr>
</table>

<br/>

---

### 💡 **LEETCODE PROGRESS**

<div align="center">
<a href="https://leetcode.com/SIZNING_LEETCODE_NICK">
<img src="https://leetcard.jacoblin.cool/SIZNING_LEETCODE_NICK?theme=dark&font=Inter&ext=heatmap" alt="LeetCode Stats" />
</a>
</div>

<br/>

---

### 🤝 **LET'S CONNECT**

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/SIZNING_LINKEDIN)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/SIZNING_TELEGRAM)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your.email@example.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white)](https://yourportfolio.com)

</div>

<br/>

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=2196F3&height=100&section=footer" width="100%" />

**"Building the future, one embedded system at a time."** 🚀

<sub>⭐ If you find my work interesting, consider giving a star to my repositories!</sub>

</div>

</div>
