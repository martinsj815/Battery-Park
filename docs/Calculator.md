---
layout: default
title: Battery Park
description: Battery Chemistry to Technology
---

<div class="tab2">
  <button class="tablinks" onclick="openCity(event, 'Single Cell')"><b>Single Cell</b></button>
  <button class="tablinks" onclick="openCity(event, 'Stacked Cell')"><b>Stacked Cell</b></button>
  <button class="tablinks" onclick="openCity(event, 'Jelly-Roll Cell')"><b>Jelly-Roll Cell</b></button>
</div>

<!-- Tab content -->
<div id="Single Cell" class="tabcontent">

  <br>
  <h2> Estimation of Cycle Life </h2>
  <br>
      - This calculation estimates the cycle life when cell cycles at a specific columbic efficiency each cycle (Option1) or estimates the required coulombic efficiency to achieve achieve a target cycle life (Option2).
    <br>
    <br>
      - This calculation assumes that the coulombic efficiency is maintained throughout the entire cycle. This estimation therefore provides an upper bound on cycle life (Option1) and a lower bound on coulombic efficiency (Option2).
  <br>
  <br>
</div>

<div id="Stacked Cell" class="tabcontent">
    <br>
  <h2> Estimation of Pouch Cell Capacity and Energy Density </h2>
    <br>
    <br>
  - This estimates the total cell capacity and eneryg density of the pouch cells.
    <br>
    <br>
  - This calculation can support in pouch cell design. For example, with a designed electrode, this modeling can determine the number of stack layers and electrolyte amount to achive target cell apacity and energy density.
</div>


<div id="Jelly-Roll Cell" class="tabcontent">
    <br>
  <h2> Estimation of Jelly-roll capacity and required electrode dimension </h2>
    <br>
    <br>
  <div class="columns">
    <div class="column">
      - This calculator can be used to compute the metrics for the cylindrical cell consisting of a jelly-roll of cathode, anode, and separator sheets.
    <br>
    <br>
      - This module calculates the electrode length required for customized cell components dimensions to fit the cylindrical cell case dimensions.
    <br>
    <br>
     - By knowing the outer and inner diameters, which are determined based on the cylindrical cell case, the cylindrical cell electrode length can be calculated using the Archimedean sppral using polar coordinates using the following equation:
    <br>
    <br>
    <ul> For the electrode length: </ul>
    <br>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=default'></script>
      $$ L = \frac{a}{2\pi}(\frac{\phi_{1}}{2}\sqrt{\phi_1^2+1}+\frac{1}{2}ln(\phi_1+\sqrt{\phi_1^2+1}-\frac{\phi_{0}}{2}\sqrt{\phi_0^2+1}-\frac{1}{2}ln(\phi_0+\sqrt{\phi_0^2+1}) $$
    <br>
    <ul> Number of windings: </ul>
    <br>
       $$ N_W = \frac{\phi_{1} - \phi_{0}}{2\pi} $$
  </div>
