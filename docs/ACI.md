---
layout: default
title: Battery Park
description: From Chemistry to Technology
---

# Academic-to-Industry <i class="arrow right"></i>

<hr style="background: linear-gradient(#a4f58e, #d8f5d0); height: 5px; border: none;">
<br>

<div class="columns">
  <div class="column">
    - There is a clear technological gap and lack of the bridge between academic research and industry requirements. Academic research uses the testing parameters and conditions that are much deviated from those that are adopted in commercial cell manufacturing. Adjusting key metrics including cathode/anode active loading, N/P ratio, and electrolyte amounts to the industrial demand is not the primary target in academia as its focus is not on reducing the cost but, instead, much on materials discovery and cell performance enhancement, which can be realized quite frequently through small cell assembly and testing. For EV battery suppliers and automative OEMs who need to meet requirements/demands on safety, cell energy density and power capability, it is also inevitable to think about the cost and energy consumption for manufacturing and hence are keen on making improvement in those metrics.
<br>
<br>
- A table below shows how different are the research lab test metrics from those in the industry setting. The columns highlighted in pink/blue are those from the labs/industry.
  </div>
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/industry_academia.png?raw=true' alt="AcademicIndustry" style="width:500px; height:auto;">
  </div>
</div>



## Table of comparison between cells tested in the lab scale vs manufactured in the industry



||Coin Cell 2032 (Lab, <10mAh) (Li metal)|Pouch Cell (Lab, 1Ah) (NCM622/Li)|Li-ion pouch cell (VW ID.3, 78Ah) (NCM622-811/Gr)|Panasonic NCR18650B, 3.3 Ah (NCA/Gr)|Tesla 4680, 22 Ah (NCM811/Gr)|Tesla Prismatic, 161.5 Ah (LFP/Gr)|BYD Blade Prismatic, 138 Ah (LFP/Gr)|
|:-|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
|Cathode areal capacity (mAh/cm<sup>2</sup>)|&lt;1|3.5|5.02|4.93|4.9|3.44|3.39*|
|Anode Areal Capacity (mAh/cm<sup>2</sup>)|&gt;50|10|5.23|4.97|5.5*|3.66|4.10*|
|N/P Ratio|&gt;50|2.86|1.04|1.01|1.12*|1.06|1.21*|
|Electrolyte weight/Cell Capacity (g/Ah)|&gt;70|3|0.95|~1.3||||
|Average cathode thickness (um)|&lt;60|67|87.3|82.5|~65|94|85*|
|Average anode thickness (um)|&gt;250|50|115.3|95|~135|71|73*|
|Electrode porosity (%)|&gt;40|34|22|||32||
|Reference|Jun Liu, et al., “Pathways for practical high-energy long-cycling lithium metal batteries”, Nature Energy, 4, 180 (2019)|Shuru Chen, et al., “Critical Parameters for Evaluating Coin Cells and Pouch Cells of Rechargeable Li-metal Batteries”, Joule, 3, 1094-1105 (2019)|F. J. Günter, et al., “State of the Art of Lithium-Ion Pouch Cells in Automotive Applications: Cell Teardown and Characterization”, J. Electrochem. Soc., 169, 030515 (2022)|Markus Hagen, et al., “Lithium-Sulfur Cells: The Gap between the State-of-the-Art and the Requirements for High Energy Battery Cells”, Adv. Energy Mater., 5, 1401986 (2015)|"Manuel Ank, et al., “Lithium-Ion Cells in Automotive Applications: Tesla 4680 Cylindrical Cell Teardown and Characterization”, J. Electrochem. Soc., 170, 120536 (2023) <br> *From https://insideevs.com/news/598656/tesla-4680-battery-cell-specs/ (Note there are some gaps between two sources)"|Sandro Stock, et al., “Cell teardown and characterization of an automotive prismatic LFP battery”, Electrochim. Acta, 471, 143341 (2023)|"https://www.linkedin.com/pulse/dry-information-byd-blade-battery-internal-disassembly-photos-cbucc/ <br> Some parameter adopted from Xiao-Guang Yang, et al., 'Thermally modulated lithium iron phosphate batteries for mass-market electric vehicles', Nature Energy, 6, 176 (2021) <br>*Currently numbers are based on the estimation"|

<br>
- As shown in the table above, in the research lab, a thinner cathode is often preferred over the thicker one (especially when uncalendared) for coin cell tests to display high capacity with good reversibility by preventing possible polarization and minimizing the degree of Li stripping and deposition. Further, using excessive amounts of electrolyte and employing thick Li metal anode in the coin cell may translate to good cycle performance without any concern of electrolyte drying out and/or Li ion supply running out during cycling. Although these measures make the data more appealing for publication, these are far from being practical in the industrial perspective owing to the loss of cell energy density.

- The table below reveals that increasing the cathode coating, reducing Li thickness, and reducing the electrolyte amount is detrimental to capacity retention of the cell.

<br>
# Influence of metrics on the coin cell (Li/NCM622) cycle performance

<br>

|Areal capacity (mAh/cm<sup>2</sup>)|Li thickness (um)|N/P Ratio|Electrolyte weight/Cell Capacity (g/Ah)|Cycle life|Current Rate (mAh/cm<sup>2</sup>)|
|:---|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
|0.45|250|111|210|&gt;300|0.9|
|2.5|50|4|35|73|0.5|
|3.8|250|13|25|62|0.76|
|1.4|50|7.1|60|37|0.28|
|3.7|50|2.7|25|15|0.74|
|3.8|250|13|3|12|0.76|
|3.5|50|2.9|3|12|0.7|

- The data from the following paper: Shuru Chen, et al., "Critical Parameters for Evaluating Coin Cells and Pouch Cells of Rechargeale Li-Metal Batteries", Joule, 3, 1094 (2019)


<br>

# Will finding the new cathode material be the solution?

- One metric to improve the cell performance is the cathode areal capacity. Apparently, simply increasing the coathing thickness will not do the job due to an increase in polarization and low material utilization. Hence, finding a new cathode system with high specific capacity is desirable, but this cannot easily be realized.
<br>
<br>
<div class="columns">
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/LFPvsNCA.png?raw=true' alt="LFPNCA" style="width:500px; height:auto;">
  </div>
  <div class="column">
    The perspective article by Frith et al., shows nicely the graphical comparison of performance between the cells consisting of NCA/Graphite-SiOx and LFP/Graphite from theoretical estimation to the pack assembly level. (see the graph on the left.) At the theory level, the differences between the cells in both gravimetric (699 Wh/kg vs. 373 Wh/kg) and volumetric energy densities (2391 Wh/L vs. 1100 Wh/L) are huge; NCA/Graphite-SiOx outperforms LFP/Graphite by almost double. However, the margin gets gradually reduced during various stages of implementation- ultimately the energy densities are almost the same as each other after factoring in reversibility, lifetime, proportion of inactive components, cell-to-pack technology, and so on.
    <br>
    <br>
    <b>Reference:</b> James T Frith, et al., "A non-academic perspective on the future of lithium-based batteries",Nature Commun., 14, 420 (2023)
  </div>
</div>

