---
layout: default
title: Battery Park
description: From Chemistry to Technology
---


<div class="tab">
  <button class="tablinks" onclick="openCity(event, 'Parameters')"><b>Parameters</b></button>
  <button class="tablinks" onclick="openCity(event, 'Metrics')"><b>Metrics</b></button>
</div>

<!-- Tab content -->
<div id="Parameters" class="tabcontent">

  <br>
  <h2> Current Density </h2>
  <br>
  <div class="columns">
    <div class="column">
      - Current density represents the quantity of current flowing through a unit cross-sectional area [mA/cm²]. Often in the literature, it is expressed in terms of current per unit active material loading [mA/g]. However, it is enssential to also provide the areal active material loading [mg/cm²] concurrently. Without this information, misleading performrance evaluations can occur, especially when the active loading of cells is low, which may not accuratley represent the true performance.

      - Additionally, current density depends on the C-rate. When specifying a current density, it should be indicated under which C-rate it applies. Without this specification, a rate 1C is typically assumed. Furthermore, when rate performance is claimed, the highest rate should correspond to 80% capacity retention. For example, if the capacity can maintain 80% at 3C, it can be claim that this cell can discharge/charge at 3C.

      - With this parameter, areal capacity can also be obtained by multiplying it with time.
    </div>
    <div class="column">
      <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/CurrentDensity.png?raw=true' alt="Current density" style="width:500px; height:auto;">
    </div>
  </div>

<br>
<br>
  
  <h2> Open Circuit Voltage (OCV) and State of Charge (SoC) </h2>
<br>
  <div class="columns">
    <div class="column">
      - OCV and SOC are important parameters in battery characterization.
      - OCV represents the potential difference between the cathode and anode when no current or voltage is applied. Theoretically, assuming that all active electrode particles are fully connected by conductive additives and maintain electrical neutrality, the OCV can be calculated from the difference in Gibbs free energy between cathode and anode materials.
      - OCV is used as an important metric to analyze electrode health and identify potential issues such as internal resistance, and capacity fade by measuring deviations from the OCV.
      - SOC represents the remaining capacity available in the battery at any given point in time. It is expressed as a percentage, where 100% indicates the battery is fully charged, and 0% indicates that it is complete discharge.
      - Since the (electro-)chemical potential of the cathode and anode varies with state of charge, OCV depends on SOC.
      - OCV and SOC are used for battery health assessment, quality control, and aging monitoring.
    </div>
    <div class="column">
      <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/OCV_SOC.png?raw=true' alt="OCV" style="width:500px; height:auto;">
    </div>
  </div>

<spacer type="block" width="50" />

<br>
<br>

  <h2> Voltage and Polarization </h2>
  <br>
    <div class="columns">
      <div class="column">
      - Voltage represents the difference in potential between the cathode and anode and the driving force of current flowing. The unit is volt [V].
      - When a circuit is connected or current begins to flow, the voltage drops, which is caused by electrode polarization due to the kinetic limits of the reaction and other electrochemical kinetical reactions to allow current to flow during the charge/discharge reaction. The degree of this polarization can be estimated from the voltage deviation (overpotential, η) from the open circuit voltage. The overpotential is given by 
      - During the reaction, the cell involves a series of physical, chemical, and electrochemical steps, including charge-transfer and charge transport reactions. The main sources of polarization can be categorized into three parts: 1) ohmic polarization (R<sub>O</sub>), 2) activation polarization (R<sub>CT</sub>), and 3) concentration polarization (R<sub>P</sub>).
      
       * Ohmic Polarization (R<sub>o</sub>) arises from the resistance of connectivity's of individual cell components and contact between the cell components. Ohmic polarization appears instantaneously (≤ 10<sup>-6</sup>s) when current flows.
       * Activation polarization (R<sub>ct</sub>) is related to the kinetics hinderances of the charge-transfer reactions at the electrode/electrolyte interfaces of anode and cathode. The buildup of the activation polarization are fast and can be identified by the voltage change on current interruption in a time frame of 10<sup>-2</sup>s - 10<sup>-4</sup>s.
       * Concentration polarization (R<sub>p</sub>) arises from limited diffusion of active species to and from the electrode surface to replace the reacted material to sustain the reaction. Diffusion limitations are relatively slow, and the buildup takes ≥ 10<sup>-2</sup>s to appear.

      Although R<sub>o</sub>, R<sub>ct</sub> and R<sub>p</sub> are not completely distinct, they are expected to be the dominat contrituion to total resistance at their respective timescales.
     - These resistances are affected by temperature, state of charge, state of health, and applied current.

    </div>
    <div class="column">
      <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Polarization.png?raw=true' alt="Polarization" style="width:500px; height:auto;">
    </div>


<spacer type="block" width="50" />

<br>
<br>

  <h2> References </h2>
  <br>
  * Martin Winter, et al, "What Are Batteries, Fuel Cells, and Supercapacitors?", Chemical Reviews, 104, 4245-4269 (2004)


</div>

<div id="Metrics" class="tabcontent">
  <h3>Paris</h3>
  <p>Paris is the capital of France.</p>
</div>
