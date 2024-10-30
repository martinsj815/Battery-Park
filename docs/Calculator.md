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
    <script src="https://code.highcharts.com/highcharts.js"></script>

</head>

<body>
    <div class="tab2">
        <button class="tablinks active" onclick="openCity(event, 'Single Cell')"><b>Single Cell</b></button>
        <button class="tablinks" onclick="openCity(event, 'Stacked Cell')"><b>Stacked Cell</b></button>
        <button class="tablinks" onclick="openCity(event, 'Jelly-Roll Cell')"><b>Jelly-Roll Cell</b></button>
    </div>
    <!-- Tab content -->
    <div id="Single Cell" class="tabcontent" style="display: block;">
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
                    <input type="number" id="numberInput" placeholder="Enter a number" value="99" step="0.1" oninput="calculateCycleLife()">
                    <br><br>
                    Capacity Retention (%) <br>
                    <input type="number" id="numberInput2" placeholder="Enter a number" value="80" step="0.1" oninput="calculateCycleLife()">
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
                    <input type="number" id="numberInput3" placeholder="Enter a number" value="70" step="0.1" oninput="calculateRequiredCE()">
                    <br><br>
                    Targeted cycle life <br>
                    <input type="number" id="numberInput4" placeholder="Enter a number" value="100" step="1" oninput="calculateRequiredCE()">
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
        <br><br>
      - This page helps estimate the total cell capacity and energy density of the pouch cell based upon a different stacking type by inputting the cell parameters needed. 
        <br><br>
      - For a certain pouch cell design, this calculation can help determine the number of stack layers and electrolyte amount to achieve target cell capacity and energy density.
        <br><br>
        <h2> Electrode Parameters </h2>
        <br>
        <div class="columns">
            <div class="column">    
                <h3> Cathode Parameters </h3>
                <br>
                Electrode density (g/cm<sup>3</sup>) <br>
                <input type="number" id="c_ed" placeholder="Enter a number" value="3" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>
                Electrode thickness [μm] <br>
                <input type="number" id="c_et" placeholder="Enter a number" value="70" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>
                Active material loading ratio <br>
                <input type="number" id="c_amlr" placeholder="Enter a number" value="0.9" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>
                Practical capacity of active material [mAh/g] <br>
                <input type="number" id="c_pcam" placeholder="Enter a number" value="180" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>         
                Electrode area [cm<sup>2</sup>] <br>
                <input type="number" id="c_ea" placeholder="Enter a number" value="19" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>  
            </div>
            <div class="column">   
                <h3> Anode Parameters </h3>
                <br>
                Electrode density [g/cm<sup>3</sup>] <br>
                <input type="number" id="a_ed" placeholder="Enter a number" value="0.534" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>
                Electrode thickness [μm] <br>
                <input type="number" id="a_et" placeholder="Enter a number" value="50" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>
                Active material loading ratio <br>
                <input type="number" id="a_amlr" placeholder="Enter a number" value="1" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>
                Practical capacity of active material [mAh/g] <br>
                <input type="number" id="a_pcam" placeholder="Enter a number" value="3860" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>        
                Electrode area [cm<sup>2</sup>] <br>
                <input type="number" id="a_ea" placeholder="Enter a number" value="19" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>  
            </div>
            <div class="column">   
                <h3> Other Parameters </h3>
                <br>
                Al foil thickness [μm] <br>
                <input type="number" id="Al_t" placeholder="Enter a number" value="12" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>
                Cu foil thickness [μm] <br>
                <input type="number" id="Cu_t" placeholder="Enter a number" value="8" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>
                Tab area [mm²] <br>
                <input type="number" id="area_tap" placeholder="Enter a number" value="25" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>
                Total seperator weight [g] <br>
                <input type="number" id="S_w" placeholder="Enter a number" value="0.5" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>        
            </div>
        </div>  
        <br><br>
        <h2> Cell Parameters </h2>
        <br>
        <div class="columns">
            <div class="column">    
                <b>Type of stacked layer and its unit:</b>
                <select id="operationSelect2" onchange="calculateStackCellEnergyDensity()">
                    <option value="t1">Type 1</option>
                    <option value="t2">Type 2</option>
                    <option value="t3">Type 3</option>
                </select>
                <br><br>
                <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/stack_type.png?raw=true' alt="AcademicIndustry" style="width:500px; height:auto;">
                <br>
                <br>
                <h3> Cell Summary Table</h3>
                <br>
                <!-- Output Section -->
                <table>
                    <thead>
                        <tr>
                            <th>Parameters</th>
                            <th>Results</th>
                        </tr>
                    </thead>
                    <tbody id="resultsBody">
                    </tbody>
                </table>
                <br><br>
                <br>
                <br>
                <div id="container" style="width: 100%; height: 500px;"></div>
                <br>
            </div>
            <div class="column">   
                Sum of other package weight [g]<sup>*1</sup> <br>
                <input type="number" id="other_packageweight" placeholder="Enter a number" value="1.1" step="0.01" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>
                Nominal cell voltage [V] <br>
                <input type="number" id="nom_v" placeholder="Enter a number" value="3.7" step="0.1" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>
                Number of stacked layer <br>
                <input type="number" id="stacked_layer" placeholder="Enter a number" value="7" step="1" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br>
                <h3> Target Energy Density [Wh/Kg]<sup>*2</sup> </h3>
                <input type="number" id="target_ed" placeholder="Enter a number" value="300" step="0.1" oninput="calculateStackCellEnergyDensity()">
                <br>
                <br> 
                <div id="plotEnergyDensity" style="width:600px;height:400px;"></div>
                <br>
            </div>
            <br>
        </div>      
        *1 A sum of other package weights includes the total weight of tabs and the packaging case. <br>
        *2 If the total cell capacity is insufficient to include the electrolyte weight in the total cell weight to reach the target energy density, this target energy density is reset according to EC ratio = 1.3 (g/Ah)(referenced Panasonic 18650B EC ratio).
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
                    Coating thickness (single-side) (μm) <br>
                    <input type="number" id="cthi" placeholder="Enter a number" step="0.1" value="50" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Al foil thickness (μm) <br>
                    <input type="number" id="althi" placeholder="Enter a number" step="0.1" value="20" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Discharge capacity of active material (mAh/g) <br>
                    <input type="number" id="discapa" placeholder="Enter a number" step="0.1" value="200" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Density of electrode material (g/cm<sup>3</sup>) <br>
                    <input type="number" id="densa" placeholder="Enter a number" step="0.1" value="4.8" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Active material loading ratio <br>
                    <input type="number" id="amlr" placeholder="Enter a number" step="0.1" value="0.9" oninput="calculatejellyroll()">
                    <br>
                    <br>         
                    Estimated porosity <br>
                    <input type="number" id="por" placeholder="Enter a number" step="0.1" value="0.2" oninput="calculatejellyroll()">
                    <br>
                    <br>  
                    Electrode width (cm) <br>
                    <input type="number" id="ewid" placeholder="Enter a number" step="0.1" value="5" oninput="calculatejellyroll()">
                    <br>
            </div>
            <div class="column">   
                <h3> Other Cell Parameters </h3>
                    <br>
                    Anode coating thickness (Single-side) (μm) <br>
                    <input type="number" id="ancthi" placeholder="Enter a number" step="0.1" value="50" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Cu foil thickness (μm) <br>
                    <input type="number" id="cuthi" placeholder="Enter a number" step="0.1" value="10" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Separator thickness (μm) <br>
                    <input type="number" id="septhi" placeholder="Enter a number" step="0.1" value="20" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Outer diameter of the cell (mm) <br>
                    <input type="number" id="outdia" placeholder="Enter a number" step="0.1" value="40" oninput="calculatejellyroll()">
                    <br>
                    <br>
                    Cell Can thickness (mm) <br>
                    <input type="number" id="canthi" placeholder="Enter a number" step="0.1" value="1.5" oninput="calculatejellyroll()">
                    <br>
                    <br>         
                    Inner diameter of the cell (mm) <br>
                    <input type="number" id="inndia" placeholder="Enter a number" step="0.1" value="2" oninput="calculatejellyroll()">
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
            `With areal capacity of Li, <b>${T_Li.toFixed(2)}μm</b> Li is stripped or deposited.`;

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
            const w_t = (sigma_1-sigma_0)/(2*Math.PI)
            const acc = densa * amlr * (1 - por) * (cthi * 0.0001) * discapa
            const pccap = acc*L_t*100*ewid/1000
            
            document.getElementById('output3').innerHTML = 
            `The length of the cathode inside the cell is <b>${L_t.toFixed(2)}m</b>. <br><br> The number of winding(turn) inside the cell is <b>${w_t.toFixed(1)}</b>. <br><br> The areal cathode capacity is <b>${acc.toFixed(2)}mAh/cm<sup>2</sup></b>. <br><br> The predicted cell capacity is <b>${pccap.toFixed(2)}Ah</b>.`;
            } else {
            document.getElementById('output3').textContent = "Please enter valid numbers.";
        }
    }


    function calculateStackCellEnergyDensity() {
        const a_ed = parseFloat(document.getElementById('a_ed').value);
        const a_et = parseFloat(document.getElementById('a_et').value);
        const a_amlr = parseFloat(document.getElementById('a_amlr').value);
        const a_pcam = parseFloat(document.getElementById('a_pcam').value);
        const a_ea = parseFloat(document.getElementById('a_ea').value);
        
        const c_ed = parseFloat(document.getElementById('c_ed').value);
        const c_et = parseFloat(document.getElementById('c_et').value);
        const c_amlr = parseFloat(document.getElementById('c_amlr').value);
        const c_pcam = parseFloat(document.getElementById('c_pcam').value);
        const c_ea = parseFloat(document.getElementById('c_ea').value);

        const Al_t = parseFloat(document.getElementById('Al_t').value);
        const area_tap = parseFloat(document.getElementById('area_tap').value);
        const S_w = parseFloat(document.getElementById('S_w').value);
        const stacked_layer = parseInt(document.getElementById('stacked_layer').value);

        const Cu_t = parseFloat(document.getElementById('Cu_t').value);
        const nom_v = parseFloat(document.getElementById('nom_v').value);
        const target_ed = parseFloat(document.getElementById('target_ed').value);
        const other_packageweight = parseFloat(document.getElementById('other_packageweight').value);

        // Retrieve selected type from dropdown
        const type = document.getElementById('operationSelect2').value;

        let cell_cap, cell_energy, NP_ratio, EC, N_al, N_cu, N_ed, cell_w_cath, cell_w_anode, w_Al, w_Cu;
        
        if (!isNaN(a_ed) && a_ed > 0 && !isNaN(a_et) && a_et > 0 && !isNaN(a_amlr) && a_amlr > 0 && !isNaN(a_pcam) && a_pcam > 0 && !isNaN(a_ea) && a_ea > 0 && !isNaN(c_ed) && c_ed > 0 && !isNaN(c_et) && c_et > 0 && !isNaN(c_amlr) && c_amlr > 0 && !isNaN(c_pcam) && c_pcam > 0 && !isNaN(c_ea) && c_ea > 0 && !isNaN(Al_t) && Al_t > 0 && !isNaN(area_tap) && area_tap > 0 && !isNaN(S_w) && S_w && !isNaN(stacked_layer) && stacked_layer > 0 && Number.isInteger(stacked_layer)) {

            const Al_density = 2.7;
            const Cu_density = 8.93;
            const areal_cap_cath = c_ed * c_et * 0.0001 * c_amlr * c_pcam;
            const areal_cap_anode = a_ed * a_et * 0.0001 * a_amlr * a_pcam;
            const cap_cath = areal_cap_cath * c_ea;
            const cap_anode = areal_cap_anode * a_ea;
            const w_cath = c_ed * c_et * 0.0001 * c_ea;
            const w_anode = a_ed * a_et * 0.0001 * a_ea;
            const rep_cap = Math.min(cap_cath, cap_anode);
            
            const Al_area = c_ea + area_tap * 0.01; 
            const Cu_area = a_ea + area_tap * 0.01;
            
            // Calculate results
            if (type === 't1') {
                N_cu = stacked_layer;
                N_al = stacked_layer;
                N_ed = stacked_layer * 2;
                cell_cap = rep_cap * stacked_layer * 2 * 0.001;
                
                // weight for electrode:
                cell_w_cath = w_cath * stacked_layer * 2; 
                cell_w_anode = w_anode * stacked_layer * 2;

                // weight for other componets: otherpackageweight(tabsand packaging), Al_foil, Cu_foil, Separator, anode, cathode, electrolyte:
                w_Al = stacked_layer * Al_density * Al_area * Al_t * 0.0001;
                w_Cu = stacked_layer * Cu_density * Cu_area * Cu_t * 0.0001;
                
            } else if (type === 't2') {
                cell_cap = rep_cap * stacked_layer * 0.001;
                if (stacked_layer === 1) {
                    N_al = 1;
                    N_cu = 1;
                } else {
                    N_al = Math.ceil(stacked_layer / 2);
                    N_cu = Math.floor(stacked_layer / 2) + 1;
                }
                N_ed= stacked_layer;
                cell_w_cath = w_cath * stacked_layer;
                cell_w_anode = w_anode * stacked_layer;
                w_Al = N_al * Al_density * Al_area * Al_t * 0.0001;
                w_Cu = N_cu * Cu_density * Cu_area * Cu_t * 0.0001; 
                
            } else {
                cell_cap = rep_cap * stacked_layer * 0.001;
                if (stacked_layer === 1) {
                    N_al = 1;
                    N_cu = 1;
                } else {
                    N_cu = Math.ceil(stacked_layer / 2);
                    N_al = Math.floor(stacked_layer / 2) + 1;                
                }
                N_ed = stacked_layer;
                cell_w_cath = w_cath * stacked_layer;
                cell_w_anode = w_anode * stacked_layer;
                w_Al = N_al * Al_density * Al_area * Al_t * 0.0001;
                w_Cu = N_cu * Cu_density * Cu_area * Cu_t * 0.0001;
            }
            
            // Calculate amount of electrode to reach target energy density
            cell_energy = cell_cap * nom_v;
            const total_target_weight = (cell_energy / target_ed) * 1000;
            const weight_beside_electrolyte = other_packageweight + w_Al+ w_Cu + S_w + cell_w_cath + cell_w_anode;
            let w_electrolyte = total_target_weight - weight_beside_electrolyte;
            NP_ratio = areal_cap_anode/areal_cap_cath;
    
            if (w_electrolyte < 0) {
                w_electrolyte = 1.3 * cell_cap;
                EC = 1.3;
            } else {
                EC = w_electrolyte/cell_cap;
            }

            const results = [
                { parameter: "Cell Capacity [Ah]", value: cell_cap.toFixed(2) },
                { parameter: "Energy [Wh]", value: cell_energy.toFixed(2) },
                { parameter: "NP Ratio", value: NP_ratio.toFixed(2) },
                { parameter: "EC Ratio", value: EC.toFixed(2) },
                { parameter: "No. Al-foil", value: N_al },
                { parameter: "No. Cu-foil", value: N_cu },
                { parameter: "No. Single Side Electrode", value: N_ed }
            ];
            
            document.getElementById('resultsBody').innerHTML = results.map(result =>
                `<tr><td>${result.parameter}</td><td><b>${result.value}</b></td></tr>`
            ).join('');

                // Create Pie Chart
            Highcharts.chart('container', {
                chart: {
                    type: 'pie'
                },
                title: {
                    text: 'Weight distribution of different cell components'
                },
                series: [{
                    name: 'Weight',
                    data: [
                        { name: 'Electrolyte Weight', y: w_electrolyte },
                        { name: 'Aluminum Weight', y: w_Al },
                        { name: 'Copper Weight', y: w_Cu },
                        { name: 'Other Components Weight', y: other_packageweight },
                        { name: 'Cathode Weight', y: cell_w_cath },
                        { name: 'Anode Weight', y: cell_w_anode }
                    ],
                    showInLegend: true,
                    dataLabels: {
                        enabled: true,
                        format: '<b>{point.percentage:.1f} %</b>',
                        style: {
                            fontSize: '20px',
                            fontWeight: 'bold', 
                        }
                    }
                }],
               tooltip: {
                   pointFormat: '{point.name}: <b>{point.y:.2f} g</b>'
               }
            });  

            let x2Values = [];
            let y2Values = [];
            let x3Trace = [];
            let y3Trace = [];

        
            if (!isNaN(w_electrolyte) && w_electrolyte > 0 ) {
                for (let i = w_electrolyte * 0.2; i <= w_electrolyte * 1.4; i += 0.1) {
                    const e_d = cell_energy/((weight_beside_electrolyte + i) * 0.001);
                    x2Values.push(i);
                    y2Values.push(e_d);
                }

                const specificElectrolyteAmount = (w_electrolyte * 0.2 + w_electrolyte * 1.4) / 2; 
                const specificEnergyDensity = cell_energy / ((weight_beside_electrolyte + specificElectrolyteAmount) * 0.001);
                
                x3Trace.push(specificElectrolyteAmount); 
                y3Trace.push(specificEnergyDensity);
            
                Plotly.newPlot('plotEnergyDensity', [
                    {
                        x: x2Values,
                        y: y2Values,
                        mode: 'lines',
                        type: 'scatter',
                        showlegend: false 
                    },
                    {
                        x: x3Trace,
                        y: y3Trace,
                        mode: 'markers',
                        type: 'scatter',
                        marker: { color: 'red', size: 8 },
                        text: [`e_d: ${y3Trace[0]} Wh/kg`], // label text for the marker
                        textposition: 'top right', // position of the text relative to the marker
                        showlegend: false 
                    }
                ], {
                    title: {
                        text: 'Energy Density vs Amount of Electrolyte',
                        font: {
                            family: 'Arial, sans-serif', 
                            size: 18, 
                            color: 'black',
                            weight: 'bold' 
                        }
                    },
                    xaxis: { title: 'Amount of Electrolyte [g]' },
                    yaxis: { title: 'Energy Density [Wh/kg]'}
                });
            } else {
                console.error("Invalid weight input. Please enter a valid number.");
            }           
        } else {
            document.getElementById('resultsBody').textContent = "Please enter valid numbers.";
        }
    }
    window.onload = function() {
        showInputFields();
        showInputFields2();
    };
    
</script>
