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
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Number Input Operations</title>
</head>
<body>

<select id="operationSelect" onchange="showInputFields()">
    <option value="cyclie-life">Option 1: Cycle Life</option>
    <option value="ce">Option 2: Required CE</option>
</select>

<div id="cycleLifeInputs" style="display: none;">
  <br>
  <b>Option 1: Estimate Cycle Number</b>
  <br>
  <br>
  Coulombic Efficiency (%) <br>
    <!-- Number Input Box -->
    <input type="number" id="numberInput" placeholder="Enter a number" oninput="handleNumberOperations()">
  <br>
  <br>
  Capacity Retention (%) <br>
    <!-- Number Input Box -->
    <input type="number" id="numberInput2" placeholder="Enter a number" oninput="handleNumberOperations()">

</div>

<div id="requiredCEInputs" style="display: none;">
  <br>
  <b>Option 2: Estimate Required Coulombic Efficiency (%) to achieve N cycle life</b>
  <br>
  <br>
  Targeted capacity retention(%) <br>
    <input type="number" id="numberInput3" placeholder="Enter a number" oninput="handleNumberOperations()">
  <br>
  <br>
  Targeted cycle life <br>
    <input type="number" id="numberInput4" placeholder="Enter a number" oninput="handleNumberOperations()">
</div>

<!-- Output Section -->
<p id="output"></p>
    
<!-- JavaScript -->
<script>
    // Show relevant input fields based on selected option
  function showInputFields() {
    const operation = document.getElementById("operationSelect").value;
    document.getElementById("cycleLifeInputs").style.display = operation === "cycle-life" ? "block" : "none";
    document.getElementById("requiredCEInputs").style.display = operation === "ce" ? "block" : "none";
    document.getElementById("output").textContent = "";
  }
  
    // Callback function to handle addition and multiplication on the input
  function calculateCycleLife() {
      // Get the value of the input box and convert it to a number
      const input = parseFloat(document.getElementById('numberInput').value);
      const input2 = parseFloat(document.getElementById('numberInput2').value);

      // Check if input is a valid number
      if (!isNaN(input)) {
        // Perform cycle number calculation
        const cycnumValue = Math.round(Math.log10(input2/100)/Math.log10(input/100));   // Cycle Number

        // Display the results
        document.getElementById('output').textContent = 
          `The cell is expected to undergo ${cycnumValue} cycles`;
      } else {
        document.getElementById('output').textContent = "Please enter a valid number.";
      }
    }
  
      function calculateRequiredCE() {
      // Get the value of the input box and convert it to a number
      const input3 = parseFloat(document.getElementById('numberInput3').value);
      const input4 = parseFloat(document.getElementById('numberInput4').value);

      // Check if input is a valid number
      if (!isNaN(input)) {
        // Perform cycle number calculation
        const cycnumValue = Math.round(Math.log10(input2/100)/Math.log10(input/100));   // Cycle Number

        // Display the results
        document.getElementById('output').textContent = 
          `The cell is expected to undergo ${cycnumValue} cycles`;
      } else {
        document.getElementById('output').textContent = "Please enter a valid number.";
      }
    }
  </script>

</body>
</html>


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
    <script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=default'></script>
      $$ L = \frac{a}{2\pi}(\frac{\phi_{1}}{2}\sqrt{\phi_1^2+1}+\frac{1}{2}ln(\phi_1+\sqrt{\phi_1^2+1}-\frac{\phi_{0}}{2}\sqrt{\phi_0^2+1}-\frac{1}{2}ln(\phi_0+\sqrt{\phi_0^2+1}) $$
    <br>
    <ul> Number of windings: </ul>
       $$ N_W = \frac{\phi_{1} - \phi_{0}}{2\pi} $$
    <br>
      where &Phi; = rotation angle and a = electrode thickness (double-sided cathode thickness + double-sided anode thickness + 2*separator thickness)
    <br>
      Note: cell outer diameter = $\frac{a}{\pi}\phi_1$ & cell inner diameter = $\frac{a}{\pi}\phi_0$ 
  </div>
