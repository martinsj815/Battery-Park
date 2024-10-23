---
layout: default
title: Battery Park
description: Battery Chemistry to Technology
---

# Li ion battery


<div class="columns">
  <div class="column">
    - Lithium-ion batteries are consisting of a host material with a high redox potential (> 3V vs Li) as a cathode and that of a low electrochemical potential (vs Li) as an anode. Typically, lithium transition metal oxides are cathodes while graphite is an anode, both of which undergo Li (de-)intercalation during charge and discharge.
    
    - Upon discharge, lithium ions migrate from the anode (e.g. lithiated graphite) towards the electrolyte while electrons move through the external circuit. Lithium ions are then carried by the electrolyte and flow into the cathode along with electrons. Upon charge, the process is reversed with the help of electrical energy injected.
  </div>
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Li%20ion%20battery.png?raw=true' alt="Capacity" style="width:500px; height:auto;">
  </div>
</div>


# Cell reaction mechanism

> The way Li-ions react with electrode active materials during charge/discharge can be categorized into following:

## Intercalation reaction:
- Li-ions are inserted or extracted from interstitital sites of the host structure without causing substantial structural changes. This makes intercalation compounds ideal for electrochemical energy storage applications. Indeed, most commercialized Li-ions batteries use electrodes with this type of reaction mechanism. However, intercalation compounds have a limited capacity due to crystallographic constrains of the host and thermodynamic instabilities arising from large changes in Li concentrations within the host.

## Alloying reaction:
- Li reacts directly with active element/compound (M) to form an intermetallic phase (LixM). Despite providing a high specific capacity for the electrode, alloying reactions generally lead to multiple phase transformations during (de-)lithiation with large volume changes, resulting in a large hysteresis in the voltage profile and poor reversibility. This hysteresis leads to irreversible energy loss upon cycling, making commercialization difficult.

## Conversion reaction:
- The reaction involves full reduction of the metal ions by lithium. It can accommodate as many electrons per transitional metal as needed to reduce its ions to the metallic state M. Therefore, materials undergoing conversion reaction can achieve much higher capacities than the intercalation compounds. When the starting compound has a strong structural relationship with its lithiated products, the conversion reaction is usually called a displacement reaction. Since these reactions involve phase transformations to extrude the transition metal, large voltage polarization and hysteresis are common.


--------------------------------------------------------------------------


# Cathode materials


<div class="columns">
  <div class="column">
    - Since the voltage is dictated by the redox energy difference between the cathode and the anode, it is imperative to have the cathode to reach the lower energy band of a metal ion at the higher oxidation state to increase the cell voltage.
    
    - The use of transition metal oxide instead of sulfide (e.g. TiS2) enables an increase in cell voltage by accessing the energy bands lying low in the energy band diagram as the O2- 2p band lies at a lower energy below a S2- 3p band.
    
    - Typical transition metal oxides used for the cathode have spinel, layered, or olivine structures that undergo Li (de-)intercalation.
    
    - There is also a conversion-based cathode material such as FeF2, with a theoretical capacity of 571 mAh/g with average operating voltage of ~2.5V.
  </div>
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Energy%20band%20diagram.png?raw=true' alt="Capacity" style="width:500px; height:auto;">
    Image Courtesy: A. Manthiram, Nature Commun. 11, 1550 (2020)
  </div>
</div>  

## Cathode Comparison Table

|Cathode Name|Crystal Structure|Chemical Formula|Specific Capacity (mAh/g) (The/Exp)|Average Voltage (V)|Electrical Conductivity (S/cm)|Li Diffusivity (cm2/s)|Exothermic Rxn T (Deg)|Heat Release (J/g)|Pros|Cons|
|:-------------|:-----------------|:-----------------|:----------|:--------------|:----------|:-------------|:------------|:------------|:-----------|:------------|
|Lithium Cobalt Oxide|Layered|LiCoO<sub>2</sub>|H<sub>2</sub>SO<sub>4</sub>|Pb(s)+PbO<sub>2</sub>(s)+2H<sub>2</sub>SO<sub>4</sub>(aq) &hArr;2PbSO<sub>4</sub>(s)+2H<sub>2</sub>O(l)|2.1|30-50 <sup> 4</sup>|4|
|Lithium Manganese Oxide|Spinel|LiMn<sub>2</sub>O<sub>4</sub>|KOH|2NiO(OH)(s) + Cd(s) + 2H<sub>2</sub>O(l) &hArr; 2Ni(OH)<sub>2</sub>(s) + Cd(OH)<sub>2</sub>(s)|1.2|50-75<sup> 5</sup>|5|
|Lithium Iron Phosphate|Olivine|LiFePO<sub>4</sub>|KOH|MH + NiO(OH)(s) <--> M + Ni(OH)<sub>2</sub>(s)|1.2|60-120<sup> 6</sup>|6|
|Lithium Iron Manganese Phosphate|Olivine|LiFe<sub>x</sub>Mn<sub>1-x</sub>PO<sub>4</sub>|Wide variety liquid w/ low to high concentration solute|LiMO<sub>2</sub>(s) + C(s) <--> Li<sub>x</sub>C(s) + Li<sub>1-x</sub>MO<sub>2</sub>(s)|3.2-4|100-300<sup> 7</sup>|7|
|Lithium Nickel Cobalt Manganese Oxide (NCM111)|Layered|Li[Ni<sub>0.33</sub>Co<sub>0.33</sub>Mn<sub>0.33</sub>]O<sub>2</sub>|        |   |3-3.1|75-200<sup> 8</sup>|8|
|Lithium Nickel Cobalt Manganese Oxide (NCM622)|Layered|Li[Ni<sub>0.6</sub>Co<sub>0.2</sub>Mn<sub>0.2</sub>]O<sub>2</sub>|Liquid (Aqueous/Non-aqueous) w/ sulfate, TFSI, triflate solute|1.3|60-80<sup> 9</sup>|9|
|Lithium Nickel Cobalt Manganese Oxide (NCM811)|Layered|Li[Ni<sub>0.8</sub>Co<sub>0.1</sub>Mn<sub>0.1</sub>]O<sub>2</sub>|Liquid (Aqueous/Non-aqueous) w/ sulfate, TFSI, triflate solute|1.3|60-80<sup> 9</sup>|9|
|Lithium Nickel Cobalt Aluminum Oxide|Layered|LiNi<sub>0.8</sub>Co<sub>0.15</sub>Al<sub>0.05</sub>O<sub>2</sub>|Liquid (Aqueous/Non-aqueous) w/ sulfate, TFSI, triflate solute|Liquid (Aqueous/Non-aqueous) w/ sulfate, TFSI, triflate solute|1.3|60-80<sup> 9</sup>|9|

