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

<br>
<br>

## Tesla EV Model Specs

| Model        |Cell Format|Material|Pack Configuration|Total Cell #|Energy (Nominal)|Battery Used|Pack Weight (kg)|Cell Weight (kg)|
|:-------------|:-----------------|:-----------------|:----------|:-----------------|:----------------------|:------------------|:------------|:------------|
| Model 3 |Prismatic|LFP|106s 1p|106|60|CATL LFP60|440|328.6|
| Model Y |Prismatic|LFP|106s 1p|106|60|CATL LFP60|440|328.6|
| Model 3 LR Dual Motor|NCM|96s 46p|4416|78|LG M50 / Panasonic 2170|481|309.1|
| Model Y LR Dual Motor |NCM|96s 46p|4416|78LG M50 2170|481|309.1|
| Model S |Cylindrical|NCA|110s 72p|7920|100|Panasonic 18650|544|356.4|
| Model X |Cylindrical|NCA|110s 72p|7920|100|Panasonic 18650|536|356.4|

- Sources: https://ev-database.org/ https://vehiclefreak.com/how-much-does-a-tesla-car-battery-weigh-model-s-model-3-model-x-and-model-y/ https://cleantechnica.com/2019/01/28/tesla-model-3-battery-pack-cell-teardown-highlights-performance-improvements/ https://twitter.com/TroyTeslike/status/1285628571491471360 https://www.sciencedirect.com/science/article/pii/S2590116823000802?via%3Dihub#sec2

<br>
<br>

## EV Battery Module Comparison

|EV Manufacturer |Model|Battery Module|Capacity (Ah)|Nominal Voltage (V)|Modules per Pack|Battery Supplier|Note|Source|
|:-------------|:-----------------|:-----------------|:----------|:-----------------|:----------------------|:------------------|:------------|:------------|
| Nissan |Leaf|2s2p2u|112.6|14.6|24|Envision AESC (NCM523 Pouch)|39 kWh|[https://www.nissan-global.com/EN/INNOVATION/TECHNOLOGY/ARCHIVE/LI_ION_EV/](https://www.nissan-global.com/EN/INNOVATION/TECHNOLOGY/ARCHIVE/LI_ION_EV/) <br>
 [https://pushevs.com/2018/01/29/2018-nissan-leaf-battery-real-specs/](https://pushevs.com/2018/01/29/2018-nissan-leaf-battery-real-specs/) <br>
 [https://www.automotivemanufacturingsolutions.com/ev-battery-production/nissan-and-envision-aesc-to-build-new-ev-battery-plant-in-japan-reports/42168.article](https://www.automotivemanufacturingsolutions.com/ev-battery-production/nissan-and-envision-aesc-to-build-new-ev-battery-plant-in-japan-reports/42168.article|
| Audi |Q6 E-tron Quattro|15s1p|152|55|12|Samsung SDI (NCM811 Prismatic)|100 kWh|"[https://www.audi-mediacenter.com/en/the-audi-q6-e-tron-electric-mobility-on-a-new-level-15929/battery-and-charging-15933](https://www.audi-mediacenter.com/en/the-audi-q6-e-tron-electric-mobility-on-a-new-level-15929/battery-and-charging-15933) <br>
 [https://electrichasgoneaudi.net/models/q6-e-tron/drivetrain/battery](https://electrichasgoneaudi.net/models/q6-e-tron/drivetrain/battery)/"|
| BMW|i3|12s1p|4416|12s1p|120|45|8|Samsung SDI (NCM622 Prismatic)|42 kWh|"[https://evshop.eu/en/batteries/298-bmwi3-42kwh-battery-pack.html](https://evshop.eu/en/batteries/298-bmwi3-42kwh-battery-pack.html) <br>
 [https://www.secondlife-evbatteries.com/products/bmw-i3-120ah-42kwh-pack](https://www.secondlife-evbatteries.com/products/bmw-i3-120ah-42kwh-pack)"|
| Hyundai |Ioniq 5|6s2p|111.2|21.8|32<sup>a</sup>|309.1|SK Innovation (NCM811 Pouch)|<sup>a</sup>For 77.4 kWh pack|"[https://insideevs.com/news/539940/hyundai-ioniq5-battery-pack-opened/](https://insideevs.com/news/539940/hyundai-ioniq5-battery-pack-opened/) <br>
 [https://openinverter.org/forum/viewtopic.php?t=4181](https://openinverter.org/forum/viewtopic.php?t=4181)"
| Kia |EV9 (Long-range)|4s3p|180.9|14.5|38|SK On (NCM)|99.8 kWh|356.4|"[https://www.kia.com/content/dam/kwcms/kme/se/sv/assets/contents/utility/specifications/ev9/kia-ev9-keyfacts.pdf ](https://www.kia.com/content/dam/kwcms/kme/se/sv/assets/contents/utility/specifications/ev9/kia-ev9-keyfacts.pdf) 
 [https://www.kiamedia.com/us/en/models/ev9/2024/specifications](https://www.kiamedia.com/us/en/models/ev9/2024/specifications)"|
| GM |Ultium(Cell)|24<sup>b</sup> cells|110s 72p|7920|100|Panasonic 18650|536|356.4|
| Chevrolet |Bolt|8 x 10s3p + 2 x 8s3p|4416|78LG M50 2170|481|309.1|
| Volkswagen |MEB (ID.4, ID.5, Buzz)|8s3p|110s 72p|7920|100|Panasonic 18650|544|356.4|
| Ford |Mach-E SR (2023)|NCA|110s 72p|7920|100|Panasonic 18650|536|356.4|
| Rivian |R1T/R1S Standard/Large|12s72p|4416|78LG M50 2170|481|309.1|
| Tesla |Model S Plaid|22s72p|22s72p|7920|100|Panasonic 18650|544|356.4|
| Lucid Air |Grand Touring|10s30p|110s 72p|7920|100|Panasonic 18650|536|356.4|
