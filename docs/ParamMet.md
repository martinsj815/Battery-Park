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
  # Current Density
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
</div>

<div id="Metrics" class="tabcontent">
  <h3>Paris</h3>
  <p>Paris is the capital of France.</p>
</div>
