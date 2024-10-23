---
layout: default
title: Battery Park
description: Battery Chemistry to Technology
---

# Li ion battery

<img src="https://dl.dropboxusercontent.com/scl/fi/hc0318st6fcb8hsk7kw11/cell-image.png?rlkey=uutzhyefy4uhb1sie5qdr6wpl&raw=1" alt="ECell" style="width:300px; height:auto;">

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





| Types        |Negative electrode|Positive electrode|Electrolyte|Representative reaction|Nominal Voltage (V)|Energy density (Wh/kg)|Reference|
|:-------------|:-----------------|:-----------------|:----------|:-----------------|:----------------------|:------------------|:------------|
| Lead-Acid    |Pb|PbO<sub>2</sub> |H<sub>2</sub>SO<sub>4</sub>|Pb(s)+PbO<sub>2</sub>(s)+2H<sub>2</sub>SO<sub>4</sub>(aq) &hArr;2PbSO<sub>4</sub>(s)+2H<sub>2</sub>O(l)|2.1|30-50 <sup> 4</sup>|4|
| Nickel-Cd    |Cd|NiO(OH)         |KOH|2NiO(OH)(s) + Cd(s) + 2H<sub>2</sub>O(l) &hArr; 2Ni(OH)<sub>2</sub>(s) + Cd(OH)<sub>2</sub>(s)|1.2|50-75<sup> 5</sup>|5|
| Nickel-Metal Hydride|Intermetallic compound (M)|NiO(OH)|KOH|MH + NiO(OH)(s) <--> M + Ni(OH)<sub>2</sub>(s)|1.2|60-120<sup> 6</sup>|6|
| Lithium-ion  |Carbon(Graphite), Silicon, Li Metal|Layered Oxides (LCO, LMO, LFP, NCM,...)|Wide variety liquid w/ low to high concentration solute|LiMO<sub>2</sub>(s) + C(s) <--> Li<sub>x</sub>C(s) + Li<sub>1-x</sub>MO<sub>2</sub>(s)|3.2-4|100-300<sup> 7</sup>|7|
| Sodium-ion   |                  |                  |        |   |3-3.1|75-200<sup> 8</sup>|8|
| Zinc-ion     |Zn                |Mainly MnO<sub>2</sub>|Liquid (Aqueous/Non-aqueous) w/ sulfate, TFSI, triflate solute|Liquid (Aqueous/Non-aqueous) w/ sulfate, TFSI, triflate solute|1.3|60-80<sup> 9</sup>|9|

## Cell Formats
- Cells can be constructed in many different form factors. These include button/coin-type, cylindrical, prismatic, and pouch-type.

-------------------------------------------------------------------------------------
### 1. Coin Cell
  * Coin cells are most commonly used in academic research and for the small consumer electronics parts such as   watches and calculators. The electrodes divided by the separator are sealed inside the can with its top and bottom electrically isolated by the gasket. Coin cells have the dimension designation - 20xx, which means 20mm diameter x.x mm height. For example, CR2016 is 20mm in diameter and 1.6 mm in height.
  * Electrode thickness, spacer thickness, parts alignment are important for controlling both internal and external assembling pressure and acquiring good data with minimum cell-to-cell difference.

<img src="https://dl.dropboxusercontent.com/scl/fi/03zylofuvvr3mtov6et4v/coin-cell2.png?rlkey=17pw4r0pqlqq00kpujh63yg0o&raw=1" alt="Primary" style="width:250px; height:auto;">

### 2. Cylindrical Cell
  * In a cylindrical cell, anode, cathode, and separator sheets are rolled in spiral and packed in a cylindrical can. Typically, this cell has a lower casing designed for a negative terminal and a top protruded cap used for a positive terminal. Also included are +/- tabs, CID and PTC elements, to protect against current surge/shorting, and gasket. These types of cells are well produced to be also actively utilized in electric vehicles.
  * The three widely used dimensions for Li-ion battery cylindrical cells are 18650, 21700, and 4680, with which the first two digits correspond to the cell diameter and the next two digits correspond to its height (i.e. 18650 cell is 18 mm in diameter and 65 mm long.). A 4680 cell has the highest max capacity ~25,000 mAh and is currently used by Tesla in various car models including Model Y and Cybertrucks.

<img src="https://dl.dropboxusercontent.com/scl/fi/w0iv2jor01ppfoz2k92z9/Cylindrical-battery.png?rlkey=hxen2pb54yesl070le3r0wjw0&raw=1" alt="Primary" style="width:250px; height:auto;">

### 3. Prismatic Cell
  * Prismatic cells consist of the anode, cathode, and separator sheets that are rolled/pressed (“jelly-rolled”) or stacked to be placed inside the metal cuboid casing. These cells are used in many small (i.e. cell phone & laptop) to larger device and electric vehicle applications.

<img src="https://dl.dropboxusercontent.com/scl/fi/fngsptshttxmi7znxdie9/Prismatic-Cell2.png?rlkey=laa7f0j1y1i4mecx3dh1n1qwd&raw=1" alt="Primary" style="width:250px; height:auto;">

### 4. Pouch Cell
  * A pouch cell uses a flexible aluminum-coated foil for sealed enclosing of cathode, anode and separator layers that are stacked. Tabs are welded outside the cell for the electron transport. Since there is no rigid outside body casing, enough space should be given inside the cell in preparation for swelling during electrochemical cycling. Pouch cells are used in a wide variety of applications including consumer electronics and electric vehicles owing to their good adaptability, energy density, and lightweight.

<img src="https://dl.dropboxusercontent.com/scl/fi/09mxpib7azoh9mfc95dds/Pouch-cell2.png?rlkey=p4km2g4bxqkxylan6cy1whdj5&raw=1" alt="Primary" style="width:250px; height:auto;">

-------------------------------------------------------------------------------------

## - Comparing Cell Formats (for EV Batteries)

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |
