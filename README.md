<div align="center">

<!-- 1. HEADER: VECTOR TYPING TEXT -->
<a href="https://github.com/Isobek">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=26&duration=3000&pause=1000&color=2196F3&center=true&vCenter=true&width=800&lines=Hi+there,+I'm+Isobek;Embedded+Systems+%26+Mobile+Architect;Building+Hard-Real-Time+Drone+Systems;C%2B%2B+%7C+Flutter+%7C+Algorithms" alt="Typing SVG" />
</a>

<br/>

<!-- 2. PROFESSIONAL BIO (No Emojis, Just Clean Typography) -->
<h3 style="border-bottom: 3px solid #2196F3; display: inline-block; color: #ffffff;">
    SYSTEM ARCHITECT PROFILE
</h3>
<p style="font-size: 16px; max-width: 650px; color: #b0b0b0; line-height: 1.6;">
    <b>Software Engineer</b> specializing in complex <b>IoT & Drone Telemetry</b>. <br>
    Bridging the gap between <b>Hardware (ESP32/C++)</b> and <b>Mobile Interfaces (Flutter)</b> using custom protocols and industrial SDKs.
</p>

<br/>

<!-- 3. TEXNOLOGIYALAR (VECTOR BADGES ONLY) -->
<!-- Bu yerda emoji yo'q, faqat rasmiy logotiplar -->
<table border="0" width="100%" cellspacing="0" cellpadding="10">
  <thead>
    <tr>
      <th align="center" width="33%">
        <img src="https://img.shields.io/badge/MOBILE_DEVELOPMENT-02569B?style=for-the-badge&logo=flutter&logoColor=white" />
      </th>
      <th align="center" width="33%">
        <img src="https://img.shields.io/badge/HARDWARE_&_IoT-E7352C?style=for-the-badge&logo=espressif&logoColor=white" />
      </th>
      <th align="center" width="33%">
        <img src="https://img.shields.io/badge/CORE_ENGINEERING-ED8B00?style=for-the-badge&logo=java&logoColor=white" />
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
        <img src="https://img.shields.io/badge/MyID-Biometrics-red?style=flat-square" />
      </td>
      <td align="center" valign="top">
        <br/>
        <img src="https://img.shields.io/badge/C++-Embedded-00599C?style=flat-square&logo=c%2B%2B&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/ESP32-SoC-E7352C?style=flat-square&logo=espressif&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/Arduino-Platform-00979D?style=flat-square&logo=arduino&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/Sensors-MPU6050_|_MQ2-orange?style=flat-square" /><br/>
        <img src="https://img.shields.io/badge/Protocol-UDP_|_MavLink-lightgrey?style=flat-square" />
      </td>
      <td align="center" valign="top">
        <br/>
        <img src="https://img.shields.io/badge/Java-Algorithms-ED8B00?style=flat-square&logo=openjdk&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/LeetCode-199_Solved-yellow?style=flat-square&logo=leetcode&logoColor=black" /><br/>
        <img src="https://img.shields.io/badge/Git-Control-F05032?style=flat-square&logo=git&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/Architecture-Clean-blueviolet?style=flat-square" /><br/>
        <img src="https://img.shields.io/badge/Design-Figma-F24E1E?style=flat-square&logo=figma&logoColor=white" />
      </td>
    </tr>
  </tbody>
</table>

<br/>

<!-- 4. DIAGRAMMA (CLEAN TECHNICAL STYLE) -->
<!-- Bu yerda Emojilar o'rniga faqat geometrik shakllar va ranglar ishlatildi -->
<h3 style="color: #ffffff; border-left: 5px solid #2ecc71; padding-left: 10px; display: inline-block;">
    SYSTEM ARCHITECTURE
</h3>
<br/>
<i style="color: #888888;">Data Flow Pipeline: Sensors -> Controller -> Mobile App</i>
</div>

```mermaid
graph LR
    %% 1. TUGUNLAR (TEXT ONLY - NO EMOJIS)
    %% Shakllar: [] = Rectangle, () = Rounded, {} = Rhombus, [()] = Database
    
    A["HARDWARE UNIT<br/>(Drone Frame)"]
    B[("ESP32 CONTROLLER<br/>(C++ Logic)")]
    C{"MOBILE APP<br/>(Flutter UI)"}
    D["NATIVE BRIDGE<br/>(Kotlin/Android)"]
    E["FLIGHT CONTROL<br/>(DJI SDK)"]
    F["AUTH SERVICE<br/>(MyID)"]

    %% 2. BOG'LANISHLAR
    A -->|Raw Sensor Data| B
    B == "UDP / MavLink" ==> C
    C -. "MethodChannel" .-> D
    D -->|Commands| E
    C -- "Verify User" --> F

    %% 3. PROFESSIONAL STYLES (FLAT COLORS)
    classDef hardware fill:#E7352C,stroke:#B71C1C,stroke-width:0px,color:white,font-weight:bold;
    classDef mobile fill:#02569B,stroke:#01579B,stroke-width:0px,color:white,font-weight:bold;
    classDef native fill:#7F52FF,stroke:#4A148C,stroke-width:0px,color:white,font-weight:bold;
    classDef sdk fill:#00C853,stroke:#1B5E20,stroke-width:0px,color:white,font-weight:bold;
    classDef auth fill:#FFD600,stroke:#F57F17,stroke-width:0px,color:black,font-weight:bold;

    %% 4. ASSIGN STYLES
    class A,B hardware;
    class C mobile;
    class D native;
    class E sdk;
    class F auth;
<div align="center">
<br/>
<!-- 5. STATISTIKA (VECTOR GRAPHS) -->
<table border="0">
<tr>
<td>
<a href="https://github.com/Isobek">
<img src="https://github-readme-stats.vercel.app/api?username=SIZNING_USERNAME&show_icons=true&theme=transparent&hide_border=true&title_color=2196F3&text_color=b0b0b0&icon_color=2196F3" height="160" alt="github stats" />
</a>
</td>
<td>
<a href="https://leetcode.com/SIZNING_LEETCODE_NICK">
<img src="https://leetcard.jacoblin.cool/SIZNING_LEETCODE_NICK?theme=dark&font=Inter&ext=heatmap" height="160" alt="leetcode stats" />
</a>
</td>
</tr>
</table>
</div>
```
💎 Nimalarni o'zgartirdim? (Professional Tahlil)
Emojisiz Header: "👋" va "🚁" kabi belgilar olib tashlandi. Ularning o'rniga Shields.io saytidan olingan "FOR-THE-BADGE" (katta va to'rtburchak) uslubidagi logotiplar qo'yildi. Bu xuddi harbiy yoki muhandislik hujjatlariga o'xshaydi.
Mermaid Diagrammasi (Geometriya):
Oldingi versiyada: 🚁 Hardware (Emoji bor edi).
Yangi versiyada: [("ESP32 CONTROLLER")] (Silindr shakli) va {MOBILE APP} (Romb shakli). Bu "System Engineering" standartidir.
Chiziqlar: Oddiy chiziqlar o'rniga qalin ==> va uzuq-uzuq -.-> chiziqlar ishlatildi, bu ma'lumot turini (Simsiz yoki Software) bildiradi.
Ranglar: "Yorqin neon" ranglar o'rniga, ko'zga yoqimli Flat UI ranglari (To'q ko'k, To'q qizil) tanlandi.
Endi bu profilingiz xuddi jiddiy kompaniyaning (masalan, Boston Dynamics yoki Google) ichki hujjati kabi ko'rinadi. 🚀
42.7s
Model
ThinkingThoughts
Expand to view model thoughts

chevron_right
code
Markdown
<div align="center">

<a href="https://github.com/Isobek">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=26&duration=3000&pause=1000&color=2196F3&center=true&vCenter=true&width=800&lines=Hi+there,+I'm+Isobek;Embedded+Systems+%26+Mobile+Architect;Building+Hard-Real-Time+Drone+Systems;C%2B%2B+%7C+Flutter+%7C+Algorithms" alt="Typing SVG" />
</a>

<br/>

<h3 style="border-bottom: 3px solid #2196F3; display: inline-block; color: #ffffff;">
    SYSTEM ARCHITECT PROFILE
</h3>
<p style="font-size: 16px; max-width: 650px; color: #b0b0b0; line-height: 1.6;">
    <b>Software Engineer</b> specializing in complex <b>IoT & Drone Telemetry</b>. <br>
    Bridging the gap between <b>Hardware (ESP32/C++)</b> and <b>Mobile Interfaces (Flutter)</b> using custom protocols and industrial SDKs.
</p>

<br/>

<table border="0" width="100%" cellspacing="0" cellpadding="10">
  <thead>
    <tr>
      <th align="center" width="33%">
        <img src="https://img.shields.io/badge/MOBILE_DEVELOPMENT-02569B?style=for-the-badge&logo=flutter&logoColor=white" />
      </th>
      <th align="center" width="33%">
        <img src="https://img.shields.io/badge/HARDWARE_&_IoT-E7352C?style=for-the-badge&logo=espressif&logoColor=white" />
      </th>
      <th align="center" width="33%">
        <img src="https://img.shields.io/badge/CORE_ENGINEERING-ED8B00?style=for-the-badge&logo=java&logoColor=white" />
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
        <img src="https://img.shields.io/badge/MyID-Biometrics-red?style=flat-square" />
      </td>
      <td align="center" valign="top">
        <br/>
        <img src="https://img.shields.io/badge/C++-Embedded-00599C?style=flat-square&logo=c%2B%2B&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/ESP32-SoC-E7352C?style=flat-square&logo=espressif&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/Arduino-Platform-00979D?style=flat-square&logo=arduino&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/Sensors-MPU6050_|_MQ2-orange?style=flat-square" /><br/>
        <img src="https://img.shields.io/badge/Protocol-UDP_|_MavLink-lightgrey?style=flat-square" />
      </td>
      <td align="center" valign="top">
        <br/>
        <img src="https://img.shields.io/badge/Java-Algorithms-ED8B00?style=flat-square&logo=openjdk&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/LeetCode-199_Solved-yellow?style=flat-square&logo=leetcode&logoColor=black" /><br/>
        <img src="https://img.shields.io/badge/Git-Control-F05032?style=flat-square&logo=git&logoColor=white" /><br/>
        <img src="https://img.shields.io/badge/Architecture-Clean-blueviolet?style=flat-square" /><br/>
        <img src="https://img.shields.io/badge/Design-Figma-F24E1E?style=flat-square&logo=figma&logoColor=white" />
      </td>
    </tr>
  </tbody>
</table>

<br/>

<h3 style="color: #ffffff; border-left: 5px solid #2ecc71; padding-left: 10px; display: inline-block;">
    SYSTEM ARCHITECTURE
</h3>
<br/>
<i style="color: #888888;">Data Flow Pipeline: Sensors -> Controller -> Mobile App</i>
</div>

```mermaid
graph LR
    A["HARDWARE UNIT<br/>(Drone Frame)"]
    B[("ESP32 CONTROLLER<br/>(C++ Logic)")]
    C{"MOBILE APP<br/>(Flutter UI)"}
    D["NATIVE BRIDGE<br/>(Kotlin/Android)"]
    E["SDK CONTROLLER<br/>(DJI / AUTEL)"]
    F["AUTH SERVICE<br/>(MyID)"]

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
<div align="center">
<br/>
<table border="0">
<tr>
<td>
<a href="https://github.com/SIZNING_USERNAME">
<img src="https://github-readme-stats.vercel.app/api?username=SIZNING_USERNAME&show_icons=true&theme=transparent&hide_border=true&title_color=2196F3&text_color=b0b0b0&icon_color=2196F3" height="160" alt="github stats" />
</a>
</td>
<td>
<a href="https://leetcode.com/SIZNING_LEETCODE_NICK">
<img src="https://leetcard.jacoblin.cool/SIZNING_LEETCODE_NICK?theme=dark&font=Inter&ext=heatmap" height="160" alt="leetcode stats" />
</a>
</td>
</tr>
</table>
</div>
