---
layout: default
title: Battery Park
description: From Chemistry to Technology
---

# EV Applications <i class="arrow right"></i>

<hr style="background: linear-gradient(#4a8049, #d8f5d0); height: 5px; border: none;">
<h2>&#9672; Batteries vs. Fuel </h2>
<div class="columns">
  <div class="column">
    <figure>
  <img src='https://github.com/energytown/Battery-Park/blob/main2/masthead/bat-gas-comp.png?raw=true' alt="Capacity" style="width:1000px; height:auto;">
    </figure>
  </div>
  <div class="column">
    <li>Fossil fuels are expected to be depleted between 2050 and 2060. Greenhouse gas emissions from burning these fuels, which account for approximately 75% of total GHG emissions<sup>1</sup>, are a primary culprit responsible for global warming and climate change. This necessitates a new energy system that eliminates combustion and the release of harmful gases. This is why people study batteries—particularly lithium-ion (Li-ion) batteries for electric vehicles (EVs), as they represent one of the most promising energy storage solutions.</li>
    <br>
  </div>
</div>
<li>However, the energy stored in Li-ion batteries falls significantly short of the energy content in fossil fuels. Currently, the specific energy of high-performing Li-ion batteries is approximately 200–250 Wh/kg, which equals to 0.72–0.9 MJ/kg. In contrast, gasoline has a specific energy of around 46 MJ/kg <sup>2</sup>—several orders of magnitude higher. This stark difference can be partially offset by the efficiency of electric motors, which convert stored energy into usable power with an efficiency of 70% or higher. This is better than the 20%–40% efficiency typical of internal combustion engines (ICEs).</li>
<li>How do companies enable EVs to perform equivalently to gasoline-powered cars despite this disparity? The solution lies in equipping EVs with large quantities of batteries. Depending on the make and model, an EV's battery pack can weigh between 1,000 to 2,000 pounds. In comparison, a gasoline-powered car carries only 10–15 gallons of fuel, which weighs approximately 60–90 pounds—a huge contrast.</li>
<h3><li> References </li></h3>
1 https://www.un.org/en/climatechange/science/causes-effects-climate-change <br>
2 https://world-nuclear.org/information-library/facts-and-figures/heat-values-of-various-fuels
<br>
<hr>
<br>
<h2>&#9672; Battery Module/Pack </h2>
<br>
<div class="columns">
  <div class="column">
   - A battery module is a collection of cells connected in series or in parallel to achieve desired voltage and energy density.
  <br>
  <br>
   - A battery pack is consisting of one or more modules (or cells) that are connected (likely in series if modules), assembled with the electrical interconnects and packaged into a single unit. Packs are usually located at the lower part compartment of the EV chassis for better design flexibility and uniform weight distribution.
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

<h2>&#9672; Cell Interconnect</h2>

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

<br>
<br>

<h2><li> Tesla EV Model Specs </li></h2>

| Model        |Cell Format|Material|Pack Configuration|Total Cell #|Energy (Nominal)|Battery Used|Pack Weight (kg)|Cell Weight (kg)|
|:-------------|:-----------------|:-----------------|:----------|:-----------------|:----------------------|:------------------|:------------|:------------|
| Model 3 |Prismatic|LFP|106s 1p|106|60|CATL LFP60|440|328.6|
| Model Y |Prismatic|LFP|106s 1p|106|60|CATL LFP60|440|328.6|
| Model 3 LR Dual Motor|Cylindrical|NCM|96s 46p|4416|78|LG M50 / Panasonic 2170|481|309.1|
| Model Y LR Dual Motor|Cylindrical|NCM|96s 46p|4416|78|LG M50 2170|481|309.1|
| Model S |Cylindrical|NCA|110s 72p|7920|100|Panasonic 18650|544|356.4|
| Model X |Cylindrical|NCA|110s 72p|7920|100|Panasonic 18650|536|356.4|

- Sources: https://ev-database.org/ https://vehiclefreak.com/how-much-does-a-tesla-car-battery-weigh-model-s-model-3-model-x-and-model-y/ https://cleantechnica.com/2019/01/28/tesla-model-3-battery-pack-cell-teardown-highlights-performance-improvements/ https://twitter.com/TroyTeslike/status/1285628571491471360 https://www.sciencedirect.com/science/article/pii/S2590116823000802?via%3Dihub#sec2

<br>
<br>

<h2>&#9672; EV Battery Module Comparison</h2>

|EV Manufacturer |Model|Battery Module|Capacity (Ah)|Nominal Voltage (V)|Modules per Pack|Battery Supplier|Note|Source|
|:-------------|:-----------------|:-----------------|:----------|:-----------------|:----------------------|:------------------|:------------|:------------|
| Nissan |Leaf|2s2p2u|112.6|14.6|24|Envision AESC (NCM523 Pouch)|39 kWh|[https://www.nissan-global.com/EN/INNOVATION/TECHNOLOGY/ARCHIVE/LI_ION_EV/](https://www.nissan-global.com/EN/INNOVATION/TECHNOLOGY/ARCHIVE/LI_ION_EV/) <br> [https://pushevs.com/2018/01/29/2018-nissan-leaf-battery-real-specs/](https://pushevs.com/2018/01/29/2018-nissan-leaf-battery-real-specs/) <br> [https://www.automotivemanufacturingsolutions.com/ev-battery-production/nissan-and-envision-aesc-to-build-new-ev-battery-plant-in-japan-reports/42168.article](https://www.automotivemanufacturingsolutions.com/ev-battery-production/nissan-and-envision-aesc-to-build-new-ev-battery-plant-in-japan-reports/42168.article|
| Audi |Q6 E-tron Quattro|15s1p|152|55|12|Samsung SDI (NCM811 Prismatic)|100 kWh|[https://www.audi-mediacenter.com/en/the-audi-q6-e-tron-electric-mobility-on-a-new-level-15929/battery-and-charging-15933](https://www.audi-mediacenter.com/en/the-audi-q6-e-tron-electric-mobility-on-a-new-level-15929/battery-and-charging-15933) <br> [https://electrichasgoneaudi.net/models/q6-e-tron/drivetrain/battery](https://electrichasgoneaudi.net/models/q6-e-tron/drivetrain/battery)|
| BMW|i3|12s1p|120|45|8|Samsung SDI (NCM622 Prismatic)|42 kWh|[https://evshop.eu/en/batteries/298-bmwi3-42kwh-battery-pack.html](https://evshop.eu/en/batteries/298-bmwi3-42kwh-battery-pack.html) <br> [https://www.secondlife-evbatteries.com/products/bmw-i3-120ah-42kwh-pack](https://www.secondlife-evbatteries.com/products/bmw-i3-120ah-42kwh-pack)|
| Hyundai |Ioniq 5|6s2p|111.2|21.8|32<sup>a</sup>|SK Innovation (NCM811 Pouch)|<sup>a</sup>For 77.4 kWh pack|[https://insideevs.com/news/539940/hyundai-ioniq5-battery-pack-opened/](https://insideevs.com/news/539940/hyundai-ioniq5-battery-pack-opened/) <br> [https://openinverter.org/forum/viewtopic.php?t=4181](https://openinverter.org/forum/viewtopic.php?t=4181)
| Kia |EV9 (Long-range)|4s3p|180.9|14.5|38|SK On (NCM)|99.8 kWh|[https://www.kia.com/content/dam/kwcms/kme/se/sv/assets/contents/utility/specifications/ev9/kia-ev9-keyfacts.pdf ](https://www.kia.com/content/dam/kwcms/kme/se/sv/assets/contents/utility/specifications/ev9/kia-ev9-keyfacts.pdf) <br> [https://www.kiamedia.com/us/en/models/ev9/2024/specifications](https://www.kiamedia.com/us/en/models/ev9/2024/specifications)|
| GM |Ultium(Cell)|24<sup>b</sup> cells|103<sup>c</sup>|3.7<sup>c</sup>|6-24|Ultium Cells LLC (LG ES Joint) (NCMA Pouch) CATL (China, NCM Cylindrical)|<sup>b</sup>Different configuration possible, <sup>c</sup>Cell Level|[https://en.wikipedia.org/wiki/Ultium](https://en.wikipedia.org/wiki/Ultium)|
| Chevrolet |Bolt|8 x 10s3p + 2 x 8s3p|~55/60<sup>f</sup>|3.65<sup>f</sup>||LG ES (Pouch Cell)|Cell Level|[https://allev.info/2023/12/chevy-bolt-ev-battery-disassembly/](https://allev.info/2023/12/chevy-bolt-ev-battery-disassembly/)|
| Volkswagen |MEB (ID.4, ID.5, Buzz)|8s3p|234|29.6|12|LG ES (Europe) (NCM712 Pouch) <br> SK On (North America) <br> CATL, VWAC (China)|82 kWh|[https://www.evcreate.com/using-volkswagen-meb-battery-modules/](https://www.evcreate.com/using-volkswagen-meb-battery-modules/) <br> [https://www.secondlife-evbatteries.com/products/vw-id-8s-battery-module-0z1915599h](https://www.secondlife-evbatteries.com/products/vw-id-8s-battery-module-0z1915599h)|
| Ford |Mach-E SR (2023)||302<sup>d</sup>|3.2<sup>d</sup>||CATL (LFP Prismatic)|<sup>d</sup>Cell Level 75 kWh|[https://www.macheforum.com/site/threads/new-mach-e-lfp-battery-specs-revealed.26099/](https://www.macheforum.com/site/threads/new-mach-e-lfp-battery-specs-revealed.26099/)|
| Rivian |R1T/R1S Standard/Large|12s72p|360|43.56|9|Samsung SDI (NCA Cylindrical)|2170 cell 141 kWh|[https://www.motortrend.com/reviews/2022-rivian-r1t-electric-pickup-truck-second-drive-review/](https://www.motortrend.com/reviews/2022-rivian-r1t-electric-pickup-truck-second-drive-review/) <br> [https://insideevs.com/news/500474/rivian-samsung-sdi-battery-supplier/](https://insideevs.com/news/500474/rivian-samsung-sdi-battery-supplier/)|
| Tesla |Model S Plaid|22s72p||81.4|5|Panasonic (NCA Cylindrical)|18650 cell 100 kWh|[https://insideevs.com/news/540380/tesla-models-plaid-battery-open/](https://insideevs.com/news/540380/tesla-models-plaid-battery-open/) <br> [https://insideevs.com/news/513181/samsungsdi-cylindrical-nca-cells-91nickel/](https://insideevs.com/news/513181/samsungsdi-cylindrical-nca-cells-91nickel/) <br> [https://ev-database.org/car/1405/Tesla-Model-S-Plaid](https://ev-database.org/car/1405/Tesla-Model-S-Plaid)|
| Lucid Air |Grand Touring|10s30p|142.5|36.4|22|LG ES (NCM Cylindrical 2170)|112 kWh|[https://eepower.com/tech-insights/teardown-unpacking-the-lucid-motors-battery-pack/#](https://eepower.com/tech-insights/teardown-unpacking-the-lucid-motors-battery-pack/#) <br> [https://insideevs.com/news/544455/lucid-air-118kwh-battery-112kwh/](https://insideevs.com/news/544455/lucid-air-118kwh-battery-112kwh/) <br> [https://www.nhtsa.gov/sites/nhtsa.gov/files/2024-02/16180-NSR-231214-003_SAE_Teardown%20Analysis%20of%20Flood-damaged%20Evs-tag.pdf](https://www.nhtsa.gov/sites/nhtsa.gov/files/2024-02/16180-NSR-231214-003_SAE_Teardown%20Analysis%20of%20Flood-damaged%20Evs-tag.pdf)|

----------------------------------------------------------------------------------------------------------

<h2>&#9672; Battery Packing Efficiency</h2>

- A geometric packing principle tells that the prismatic/pouch cells should yield packing efficiency of 90-95%, way higher than the cylindrical cell. However, it is noteworthy that the volumetric efficiency rate of the prismatic/pouch cells in actual EV batteries are lower and even comparable to those of cylindrical. According to the paper by Löbberding et al., after surveying 25 different BEVs (from 10 OEMs between 2010-2019), the average volume utilization rate is 0.353, which is only slightly higher than that of cylindrical (0.295). This discrepancy can be due to incorporation of auxiliary yet important parts such as interconnects, thermal management (i.e. cooling) system, BMS, and sensors. However, a caveat is that the average cell-to-module efficiency for prismatic/pouch cells is much higher than that of the cylindrical cell while the opposite is true for module-pack system efficiency comparison – making cell-to-system efficiencies all comparable after all. Hence, better space utilization has been sought after by many OEMs including BYD, CATL, and Tesla.

<br>

<h2>&#9672; CMP, CTP, and CMB</h2>

<div class="columns">
  <div class="column">
   - A In the traditional CMP (cell-module-pack) battery structure for the electric vehicle, module size varies among different electric vehicle manufacturers from Nissan’s 8-cell modules to Tesla’s 1584-cell modules. Increasing the module size has improved chassis space utilization to enhance battery capacity but the structure limits the space for other components, thus meeting the performance demand increasingly difficult.
  <br>
  <br>
   - A battery Pack is consisting of one or more modules (or cells) that are connected (likely in series if modules), assembled with the electrical interconnects and packaged into a single unit. Packs are usually located at the lower part compartment of the EV chassis for better design flexibility and uniform weight distribution.
  <br>
  <br>
   - CTP (cell-to-pack) technology improves the space utilization and energy density by skipping the modular arrangements of the cells. This direct integration proposed by CATL, according to their first-generation CTP, can increase space utilization by 15-20%, reduce the part numbers for a pack by 40%, and enhance energy density by 25-30% to 200 Wh/kg, when compared with CMP. Their third generation CTP has boosted volumetric utilization efficiency to 72% (from 55% in the first generation) and allowed energy density to reach 255 Wh/kg using Qilin NMC batteries.
  <br>
  <br>
  - Cell integration to the body (CTB) is the new technology proposed by BYD by launching LFP blade battery and increases volumetric energy density by up to 50% and space utilization by over 50% when compared to the CMP predecessor.  
  </div>
  <div class="column">
    <figure>
  <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/CATLCTP.png?raw=true' alt="CATLBYD" style="width:1000px; height:auto;">
  <figcaption>Top- Source: CATL / https://www.catl.com/en/news/958.html
Bottom- Source: medium.com / https://medium.com/batterybits/the-next-generation-battery-pack-design-from-the-byd-blade-cell-to-module-free-battery-pack-2b507d4746d1</figcaption>
    </figure>
  </div>
</div>
<br>
<h3> Reference </h3>

- Hendrik Löbberding, et al.,"From Cell to Battery System in BEVs: Analysis of System Packing Efficiency and Cell Types", World Electric Vehicle Journal, 11, 77 (2020)
