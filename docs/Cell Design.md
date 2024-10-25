---
layout: default
title: Battery Park
description: Battery Chemsitry to Technology 
---

# N/P Ratio

The N/P ratio is a crucial cell design parameter that can influences the utilization level of the electrodes, thereby affecting overall performance and cell-level energy density. The N/P ratio represents the capacity ratio between the anode and cathode. The optimal N/P ratio depends on the electrode's electrochemical reaction mechanism, reaction efficiency, and the decay rate of the cathode and anode during cycling. This parameter must be optimized based on the operating environment.


|Anode Type|N/P Ratio|Comments|
|:-------------|:-----------------|:-----------------|
|Graphite|N/P > 1|- An excess cathode can cause excess lithium ions to deposit on the anode surface during charging, forming dendrites. This reduces battery cycle performance and can lead to short circuits. Thus, an excess anode is benefical for preventing lithium deposition on the anode surface during overcharge, thereby improving cycle life and safety. <br><br> - E.g.: N/P ratio is 1.08 with NCM811 @ W. Zhao et al., Materials Today Energy, 34, 101301 (2023)|
|Li<sub>4</sub>Ti<sub>5</sub>O<sub>12</sub>(LTO)|N/P < 1|- LTO has a stable structure, high intercalation potential (1.55V vs Li/Li<sup>+</sup>), and excellent cycle performance, and does not exhibit lithium plating with excess lithium ions from the cathode. Therefore, designing cells with excess cathode capacity and limited anode capacity (N/P < 1) can mitigate electrolyte degradation due to a high cathode potential when the battery is near or at full charge. <br><br> - E.g.: N/P ratio is 0.68 with NCM111 @ 'Comprehensive guide to battery cathode and anode capacity design', 2022, tycorun.com|
|Si|1 < N/P < 2|- If the anode is highly overbalanced, only a small amount of silicon will be lithiated, resulting in a high anode potential at the end of charge. To reach the same full cell voltage, the cathode material may be overcharged, accelerating degradation due to side reactions in the cathode or electrolyte depletion. <br><br> - E.g.: NP ratio is 1.15-1.4 with NCM811 @ F. Reuter et al., Journal of The Electrochemical Society, 166, 14, A3265-A3271 (2019)|
|Li metal|N/P ~ 1|- A thick Li metal anode (N/P > 2.5) provides a stable initial cycle. However, continued cycling leads to a thick SEI layer build-up, increasing cell polarization. When this becomes dominant, it results in electrolyte depletion and a sudden drop in capacity. Conversely, for N/P ratio close to 1, which effectively balances the lithium consumption rate, electrolyte depletion rate, and SEI accumulation rate under realistic conditions, cell polarization is minimized, extending cell cycle life. <br><br> - E.g.: N/P ratio is 1 with NMC622 @ C. Niu et al., Nature Energy, 6, 723-732 (2021)|

## Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)


_yay_

[back](./)
