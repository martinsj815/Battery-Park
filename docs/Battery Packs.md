---
layout: default
title: Battery Park
description: Battery Chemistry to Technology
---

# Battery Module/Pack 

<div class="columns">
  <div class="column">
   - A battery Module is a collection of cells connected in series or in parallel to achieve desired voltage and energy density.
  <br>
  <br>
   - A battery Pack is consisting of one or more modules (or cells) that are connected (likely in series if modules), assembled with the electrical interconnects and packaged into a single unit. Packs are usually located at the lower part compartment of the EV chassis for better design flexibility and uniform weight distribution.
  <br>
  <br>
   - The pack usually requires monitoring, sensing (i.e. voltage and temperature), and control through effective battery management system for protection, stability, and safety of the battery.
  </div>
  <div class="column">
    <img src="https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Cell_module_pack.png?raw=true" alt="ECell" style="width:300px; height:auto;">
   <br>
    <figure>
  <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/e-tron%206%20quattro.png?raw=true' alt="Capacity" style="width:1000px; height:auto;">
  <figcaption>Source: https://electrichasgoneaudi.net/models/q6-e-tron/drivetrain/battery/</figcaption>
    </figure>
  </div>
</div>

## Cell Interconnect

<div class="columns">
  <div class="column">
   - Cells are connected electrically using the busbars (typically aluminum) via various joining technologies such as laser welding and ultrasonic wire bonding. Interconnect design can vary depending on the cell form factor. The schematics on the right show the single-sided interconnect of the cells.
  <br>
  <br>
   - Older Tesla Models 3/S/X use wire bonding while newer Model S Plaid and Model Y use laser welding possibly for robustness of the connection, away from the breaking of the fragile wires.
  <br>
  <br>
   - The pack usually requires monitoring, sensing (i.e. voltage and temperature), and control through effective battery management system for protection, stability, and safety of the battery.
  </div>
  <div class="column">
    <img src="https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Cell%20Interconnect.png?raw=true" alt="ECell" style="width:500px; height:auto;">
  </div>
</div>


- Primary Cell

<div class="columns">
  <div class="column">
    It is a galvanic cell that can only be used once before disposal as the electrochemical reaction is irreversible and the cell is unable to be recharged with electricity.
  </div>
  <div class="column">
    <img src="https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Primary%20battery.png?raw=true" alt="Primary" style="width:200px; height:auto;">
  </div>
</div>


- Secondary Cell

<div class="columns">
  <div class="column">
    It is a rechargeable cell with electrochemical reaction reversible by applying the reverse current. Discharge involves converting chemical energy to electricity while the reverse happens upon charge.
  </div>
  <div class="column">
    <img src="https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Secondary%20battery.png?raw=true" alt="Primary" style="width:250px; height:auto;">
  </div>
</div>


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

<div class="columns">
  <div class="column">
    Coin cells are most commonly used in academic research and for the small consumer electronics parts such as   watches and calculators. The electrodes divided by the separator are sealed inside the can with its top and bottom electrically isolated by the gasket. Coin cells have the dimension designation - 20xx, which means 20mm diameter x.x mm height. For example, CR2016 is 20mm in diameter and 1.6 mm in height.
   
   Electrode thickness, spacer thickness, parts alignment are important for controlling both internal and external assembling pressure and acquiring good data with minimum cell-to-cell difference.
  </div>
  <div class="column">
    <img src="https://github.com/donghee1025/Battery-Park/blob/main2/masthead/coin%20cell2.png?raw=true" alt="Primary" style="width:300px; height:auto;">
  </div>
</div>


### 2. Cylindrical Cell

<div class="columns">
  <div class="column">
    In a cylindrical cell, anode, cathode, and separator sheets are rolled in spiral and packed in a cylindrical can. Typically, this cell has a lower casing designed for a negative terminal and a top protruded cap used for a positive terminal. Also included are +/- tabs, CID and PTC elements, to protect against current surge/shorting, and gasket. These types of cells are well produced to be also actively utilized in electric vehicles.
   
   The three widely used dimensions for Li-ion battery cylindrical cells are 18650, 21700, and 4680, with which the first two digits correspond to the cell diameter and the next two digits correspond to its height (i.e. 18650 cell is 18 mm in diameter and 65 mm long.). A 4680 cell has the highest max capacity ~25,000 mAh and is currently used by Tesla in various car models including Model Y and Cybertrucks.
  </div>
  <div class="column">
    <img src="https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Cylindrical%20battery.png?raw=true" alt="Primary" style="width:300px; height:auto;">
  </div>
</div>


## - Cylindrical Cell Comparison

|              | 18650             | 21700 |4680          |
|:-------------|:------------------|:------|:-------------|
| Diameter (mm)| 18                | 21    |46            |
| Height (mm)  | 65                | 70    |80            |
| Nominal Voltage (V)| 3.6-3.7    | 3.6-3.7|3.7 (estimate)|
| Capacity (mAh)| 3450 (LG INR1860-M36) / 3450 (LG INR1860-M36) |5000 (LG INR21700-M50)/5000 (Samsung INR21700-50E)/5000 (Panasonic NCR21700T)"|~23000 (Tesla 4680, estimate)|
| Energy Density (Wh/kg)|248 (LG INR18650-M36) / 264 (Panasonic NCR18650G)|263 (LG CHEM INR21700-M50L)/261 (Samsung INR21700-50E)/271 (Panasonic NCR2170-M)|~23000 (Tesla 4680, estimate)|


### 3. Prismatic Cell

<div class="columns">
  <div class="column">
    Prismatic cells consist of the anode, cathode, and separator sheets that are rolled/pressed (“jelly-rolled”) or stacked to be placed inside the metal cuboid casing. These cells are used in many small (i.e. cell phone & laptop) to larger device and electric vehicle applications.
  </div>
  <div class="column">
    <img src="https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Prismatic%20Cell2.png?raw=true" alt="Primary" style="width:300px; height:auto;">
  </div>
</div>


### 4. Pouch Cell

<div class="columns">
  <div class="column">
    A pouch cell uses a flexible aluminum-coated foil for sealed enclosing of cathode, anode and separator layers that are stacked. Tabs are welded outside the cell for the electron transport. Since there is no rigid outside body casing, enough space should be given inside the cell in preparation for swelling during electrochemical cycling. Pouch cells are used in a wide variety of applications including consumer electronics and electric vehicles owing to their good adaptability, energy density, and lightweight.
  </div>
  <div class="column">
    <img src="https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Pouch%20cell2.png?raw=true" alt="Primary" style="width:300px; height:auto;">
  </div>
</div>



-------------------------------------------------------------------------------------

## - Comparing Cell Formats (for EV Batteries)

|              | 18650             | 21700 |4680          |
|:-------------|:------------------|:------|:-------------|
| Diameter (mm)| 18                | 21    |46            |
| Height (mm)  | 65                | 70    |80            |
| Nominal Voltage (V)| 3.6-3.7    | 3.6-3.7|3.7 (estimate)|
| Capacity (mAh)| 3450 (LG INR1860-M36) / 3450 (LG INR1860-M36) |5000 (LG INR21700-M50)/5000 (Samsung INR21700-50E)/5000 (Panasonic NCR21700T)"|~23000 (Tesla 4680, estimate)|
| Energy Density (Wh/kg)|248 (LG INR18650-M36) / 264 (Panasonic NCR18650G)|263 (LG CHEM INR21700-M50L)/261 (Samsung INR21700-50E)/271 (Panasonic NCR2170-M)|~23000 (Tesla 4680, estimate)|

