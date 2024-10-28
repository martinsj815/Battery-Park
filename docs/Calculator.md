---
layout: default
title: Battery Park
description: Battery Chemistry to Technology
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number Input Operations</title>
    <style>
        /* Style the horizontal rule */
        .colored-line {
            border: 0; /* Remove default border */
            height: 2px; /* Height of the line */
            background-color: #4CAF50; /* Color of the line */
            margin: 20px 0; /* Space above and below the line */
        }
    </style>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>

<body onload="openCity('Single Cell'); showInputFields()">
    <div class="tab2"><button class="tablinks" onclick="openCity(event, 'Single Cell')"><b>Single Cell</b></button>
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
        <select id="operationSelect" onchange="showInputFields()">
            <option value="cycle-life" selected>Option 1: Cycle Life</option>
            <option value="ce">Option 2: Required CE</option>
        </select>
        <br>
        <br>
        <div id="cycleLifeInputs" style="display: block;">
            <div class="columns">
                <div class="column">    
                    <br>
                    <b>Option 1: Estimate Cycle Number</b>
                    <br><br>
                    Coulombic Efficiency (%) <br>
                    <input type="number" id="numberInput" placeholder="Enter a number" step="0.1" oninput="calculateCycleLife()">
                    <br><br>
                    Capacity Retention (%) <br>
                    <input type="number" id="numberInput2" placeholder="Enter a number" step="0.1" oninput="calculateCycleLife()">
                </div>
                <div class="column">    
                    <br>
                    <div id="myPlotCycleLife" style="width:600px;height:400px;"></div>
                </div> 
            </div>
        </div>
        <div id="requiredCEInputs" style="display: none;">
            <div class="columns">
                <div class="column">       
                    <br>
                    <b>Option 2: Estimate Required Coulombic Efficiency (%) to achieve N cycle life</b>
                    <br><br>
                    Targeted capacity retention(%) <br>
                    <input type="number" id="numberInput3" placeholder="Enter a number" step="0.1" oninput="calculateRequiredCE()">
                    <br><br>
                    Targeted cycle life <br>
                    <input type="number" id="numberInput4" placeholder="Enter a number" step="1" oninput="calculateRequiredCE()">
                </div>
                <div class="column">    
                    <br>
                    <div id="myPlotRequiredCE" style="width:600px;height:400px;"></div>
                </div> 
            </div>
        </div> 
            <!-- Output Section -->
        <h3 id="output"></h3>
        <br><br>
    <hr class="colored-line">
        <br><br>
        <div>
            <h2> Estimation of Li-metal thickness </h2>
            <br>
              - This calculation estimates the amount of Li deposition or exfoliation during charge/discharge reactions depending on the applied areal current density.
            <br>
            <br>
              - Note that this is theoretical estimation and calculated by assuming perfectly flat and smooth film of Li.
            <br>
            <br>
            <div class="columns">
                <div class="column">    
                    Li Areal Capacity [mAh/cm<sup>2</sup>] <br>
                    <input type="number" id="LiAC" placeholder="Enter a number" step="0.01" oninput="calculateLithickness()">
                </div>
                <br>
                <div class="column">    
                    <br>
                    <div id="myPlotLithickness" style="width:600px;height:400px;"></div>
                </div>
            </div>
            <!-- Output Section -->
            <h3 id="output2"></h3>
            <br><br>
        </div>
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
        Note: cell outer diameter = \(\frac{a}{\pi}\phi_1\) & cell inner diameter = \(\frac{a}{\pi}\phi_0\) 
        <br>
        <br>
        <br>
        <br>
        <div class="columns">
            <div class="column">    
                <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/cylindrical%20spiral_wcaption.png?raw=true' alt="AcademicIndustry" style="width:500px; height:auto;">
            </div>
            <div class="column">    
                <h3> Cathode Parameters </h3>
                    <br>
                    Coating thickness (single-side) (um) <br>
                    <input type="number" id="cthi" placeholder="Enter a number" step="0.1" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Al foil thickness (um) <br>
                    <input type="number" id="althi" placeholder="Enter a number" step="0.1" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Discharge capacity of active material (mAh/g) <br>
                    <input type="number" id="discapa" placeholder="Enter a number" step="0.1" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Density of electrode material (g/cm<sup>3</sup>) <br>
                    <input type="number" id="densa" placeholder="Enter a number" step="0.1" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Active material loading ratio <br>
                    <input type="number" id="amlr" placeholder="Enter a number" step="0.1" oninput="calculatejellyroll()">
                    <br>
                    <br>         
                    Estimated porosity <br>
                    <input type="number" id="por" placeholder="Enter a number" step="0.1" oninput="calculatejellyroll()">
                    <br>
                    <br>  
                    Electrode width (cm) <br>
                    <input type="number" id="ewid" placeholder="Enter a number" step="0.1" oninput="calculatejellyroll()">
                    <br>
            </div>
            <div class="column">   
                <h3> Other Cell Parameters </h3>
                    <br>
                    Anode coating thickness (Single-side) (um) <br>
                    <input type="number" id="ancthi" placeholder="Enter a number" step="0.1" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Cu foil thickness (um) <br>
                    <input type="number" id="cuthi" placeholder="Enter a number" step="0.1" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Separator thickness (um) <br>
                    <input type="number" id="septhi" placeholder="Enter a number" step="0.1" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Outer diameter of the cell (mm) <br>
                    <input type="number" id="outdia" placeholder="Enter a number" step="0.1" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Cell Can thickness (mm) <br>
                    <input type="number" id="canthi" placeholder="Enter a number" step="0.1" oninput="calculatejellyroll()">
                    <br>
                    <br>         
                    Inner diameter of the cell (mm) <br>
                    <input type="number" id="inndia" placeholder="Enter a number" step="0.1" oninput="calculatejellyroll()">
                    <br>
            </div>
        </div>  
        <!-- Output Section -->
        <h3 id="output3"></h3>
    </div>
</body>

<!-- JavaScript -->
<script>
    let xValues = [];
    let yValues = [];
    let xTrace = [];
    let yTrace = [];
    let x2Trace = [];
    let y2Trace = [];

    function generatePlot() {
        xValues = [];
        yValues = [];
        
        const ce = parseFloat(document.getElementById('numberInput').value);

        if (!isNaN(ce) && ce > 0 && ce < 100) {
            for (let capacityRetention = 0; capacityRetention <= 100; capacityRetention += 1) {
                const cycleNumber = Math.round(Math.log(capacityRetention/100) / Math.log(ce/100));
                xValues.push(cycleNumber);
                yValues.push(capacityRetention);
            }
            Plotly.newPlot('myPlotCycleLife', [
                {
                    x: xValues,
                    y: yValues,
                    mode: 'lines',
                    type: 'scatter',
                    showlegend: false 
                },
                {
                    x: xTrace,
                    y: yTrace,
                    mode: 'markers',
                    type: 'scatter',
                    marker: { color: 'red', size: 8 },
                    text: [`Cycle: ${xTrace[0]}, Capacity: ${yTrace[0]}%`], // label text for the marker
                    textposition: 'top right', // position of the text relative to the marker
                    showlegend: false 
                }
            ], {
            title:  {
                text: 'Cycle Number vs Capacity Retention',
                font: {
                    family: 'Arial, sans-serif', // Choose a font family
                    size: 18, // Adjust the font size
                    color: 'black', // Title color
                    weight: 'bold' // Make title bold
                    }
            },        
            xaxis: { title: 'Cycle Number' },
            yaxis: { title: 'Capacity Retention'}
            }
            );
        } else {
            console.error("Invalid CE input. Please enter a valid number.");
        }
    }  
    function generateSecPlot() {
        xValues = [];
        yValues = [];

        const cr = parseFloat(document.getElementById('numberInput3').value);

        if (!isNaN(cr) && cr > 0 && cr < 100 ) {
            for (let cycleNumber = 1; cycleNumber <= 200; cycleNumber += 1) {
                const ReqceValue = 100 * (Math.exp(Math.log(cr/100) / cycleNumber));
                xValues.push(cycleNumber);
                yValues.push(ReqceValue);
            }
            Plotly.newPlot('myPlotRequiredCE', [
                {
                    x: xValues,
                    y: yValues,
                    mode: 'lines',
                    type: 'scatter',
                    showlegend: false 
                },
                {
                    x: xTrace,
                    y: yTrace,
                    mode: 'markers',
                    type: 'scatter',
                    marker: { color: 'red', size: 8 },
                    text: [`Cycle: ${xTrace[0]}, CE: ${yTrace[0]}%`], // label text for the marker
                    textposition: 'top right', // position of the text relative to the marker
                    showlegend: false 
                }
            ], {
                title: {
                    text: 'Cycle Number vs Coulombic Efficiency',
                    font: {
                        family: 'Arial, sans-serif', // Choose a font family
                        size: 18, // Adjust the font size
                        color: 'black', // Title color
                        weight: 'bold' // Make title bold
                            }
                },
                xaxis: { title: 'Cycle Number' },
                yaxis: { title: 'Coulombic Efficiency (%)'}
            }
            );
        } else {
            console.error("Invalid cycle retention input. Please enter a valid number.");
        }
    } 
    function generateLithickPlot() {
        xValues = [];
        yValues = [];

        const LiAC = parseFloat(document.getElementById('LiAC').value);

        if (!isNaN(LiAC) && LiAC > 0 ) {
            for (let i = 0; i <= LiAC * 1.5; i += 0.1) {
                const T_Li = 10000*i*6.941/(26801.4814*0.534);
                xValues.push(i);
                yValues.push(T_Li);
            }
            
            Plotly.newPlot('myPlotLithickness', [
                {
                    x: xValues,
                    y: yValues,
                    mode: 'lines',
                    type: 'scatter',
                    showlegend: false 
                },
                {
                    x: x2Trace,
                    y: y2Trace,
                    mode: 'markers',
                    type: 'scatter',
                    marker: { color: 'red', size: 8 },
                    text: [`LiAC: ${x2Trace[0]} mAh/cm²`], // label text for the marker
                    textposition: 'top right', // position of the text relative to the marker
                    showlegend: false 
                }
            ], {
                title: {
                    text: 'Li Thickness Response to Li Areal Capacity',
                    font: {
                        family: 'Arial, sans-serif', 
                        size: 18, 
                        color: 'black',
                        weight: 'bold' 
                            }
                },
                xaxis: { title: 'Li Areal Capacity [mAh/cm²]' },
                yaxis: { title: 'Li Thickness (um)'}
            }
            );
        } else {
            console.error("Invalid areal capacity input. Please enter a valid number.");
        }
    }    
    function showInputFields() {
        const operation = document.getElementById("operationSelect").value;
        document.getElementById("cycleLifeInputs").style.display = operation === "cycle-life" ? "block" : "none";
        document.getElementById("requiredCEInputs").style.display = operation === "ce" ? "block" : "none";
        document.getElementById("output").textContent = "";

        if (operation === "cycle-life") {
            generatePlot();
        } else {
            generateSecPlot();
        }
    }
  
    function calculateCycleLife() {
        // Get the value of the input box and convert it to a number
        const input = parseFloat(document.getElementById('numberInput').value);
        const input2 = parseFloat(document.getElementById('numberInput2').value);

        
      // Check if input is a valid number
        if (!isNaN(input) && !isNaN(input2)) {
            const cycnumValue = Math.round(Math.log(input2/100)/Math.log(input/100));   
            document.getElementById('output').innerHTML = `The cell is expected to undergo <b>${cycnumValue}</b> cycles.`;
            
            xTrace = [cycnumValue];
            yTrace = [input2];
            
            generatePlot(); // Re-generate plot with new data
        } else {
          document.getElementById('output').textContent = "Please enter a valid number.";
        }
    }
    function calculateRequiredCE() {
        const input3 = parseFloat(document.getElementById('numberInput3').value);
        const input4 = parseFloat(document.getElementById('numberInput4').value);

        if (!isNaN(input3) && !isNaN(input4)) {
          // Perform cycle number calculation
          const ReqceValue = 100*(Math.exp(Math.log(input3/100)/input4)); 
          document.getElementById('output').innerHTML = 
            `The cell is required <b>${ReqceValue.toFixed(2)}%</b> CE to achieve ${input4} cycle life`;
            
            xTrace = [input4];
            yTrace = [ReqceValue];
            
            generateSecPlot(); // Re-generate plot with new data
        } else {
          document.getElementById('output').textContent = "Please enter a valid number.";
        }
    }
    function calculateLithickness() {
        const LiAC = parseFloat(document.getElementById('LiAC').value);

        if (!isNaN(LiAC) && LiAC > 0) {
          const T_Li = 10000*LiAC*6.941/(26801.4814*0.534); 
          document.getElementById('output2').innerHTML = 
            `With areal capacity of Li, <b>${T_Li.toFixed(2)}um</b> Li is stripped or deposited.`;

            x2Trace = [LiAC];
            y2Trace = [T_Li];
            
            generateLithickPlot(); // Re-generate plot with new data
        } else {
          document.getElementById('output2').textContent = "Please enter a valid number.";
        }
    }
    function calculatejellyroll() {
        const cthi = parseFloat(document.getElementById('cthi').value);
        const althi = parseFloat(document.getElementById('althi').value);
        const discapa = parseFloat(document.getElementById('discapa').value);
        const densa = parseFloat(document.getElementById('densa').value);
        const amlr = parseFloat(document.getElementById('amlr').value);
        const por = parseFloat(document.getElementById('por').value);
        const ewid = parseFloat(document.getElementById('ewid').value);

        const ancthi = parseFloat(document.getElementById('ancthi').value);
        const cuthi = parseFloat(document.getElementById('cuthi').value);
        const septhi = parseFloat(document.getElementById('septhi').value);
        const outdia = parseFloat(document.getElementById('outdia').value);
        const canthi = parseFloat(document.getElementById('canthi').value);
        const inndia = parseFloat(document.getElementById('inndia').value);
        
        if (!isNaN(cthi) && cthi > 0 && !isNaN(althi) && althi > 0 && !isNaN(discapa) && discapa > 0 && !isNaN(densa) && densa > 0 && !isNaN(amlr) && amlr > 0 && !isNaN(por) && por > 0 && !isNaN(ewid) && ewid > 0 && !isNaN(ancthi) && ancthi > 0 && !isNaN(cuthi) && cuthi > 0 && !isNaN(septhi) && septhi > 0 && !isNaN(outdia) && outdia > 0 && !isNaN(canthi) && canthi > 0 && !isNaN(inndia) && inndia > 0) {
            const d_asc = cthi*2 + althi + ancthi*2 + cuthi + septhi*2;
            const a = d_asc/(2*Math.PI)*(0.000001);
            const d_o = outdia - 2*canthi;
            const r_o = d_o*(0.001)/2;
            const d_i = inndia;
            const r_i = d_i*(0.001)/2;
            const sigma_1 = r_o / a;
            const sigma_0 = r_i / a;
            const L_1 = (sigma_1/2)*(Math.pow(((sigma_1)*(sigma_1)+1),0.5)) + 0.5*Math.log(sigma_1 + Math.pow(((sigma_1)*(sigma_1)+1),0.5));
            const L_0 = (sigma_0/2)*(Math.pow(((sigma_0)*(sigma_0)+1),0.5)) + 0.5*Math.log(sigma_0 + Math.pow(((sigma_1)*(sigma_1)+1),0.5));
            const L_t = (L_1 - L_0) * d_asc / (2 * Math.PI) * 0.000001;
            const acc = densa * amlr * (1 - por) * (cthi * 0.0001) * discapa
            const pccap = acc*L_t*100*ewid
            
            document.getElementById('output3').innerHTML = 
            `The length of the cathode inside the cell is <b>${L_t.toFixed(2)}m</b>.`<br><br>
            The number of winding(turn) inside the cell is <b>${w_t.toFixed(1)}</b>.`<br><br>
            The areal cathode capacity is <b>${acc.toFixed(2)}mAh/cm<sup>2</sup></b>.`<br><br>
            The predicted cell capacity is <b>${acc.toFixed(2)}Ah</b>.`;
            
        } else {
            document.getElementById('output3').textContent = "Please enter valid numbers.";
        }
    }
    window.onload = function() {
        showInputFields();
    };
    
</script>
