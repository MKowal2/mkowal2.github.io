---
title: "Position, Padding and Predictions: A Deeper Look at Position Information in CNNs"
collection: publications
permalink: /publication/2021-01-01-position-padding-prediction
excerpt: 'We explore the existance of absolute position information in CNNs in relation to their padding type or other border heuristics.'
date: 2021-10-01
venue: 'BMVC (Oral)'
paperurl: 'https://arxiv.org/pdf/2101.12322.pdf'
---

**Abstract:** In contrast to fully connected networks, Convolutional Neural Networks (CNNs) achieve efficiency by learning weights associated with local filters with a finite spatial extent. An implication of this is that a filter may know what it is looking at, but not where it is positioned in the image. In this paper, we first test this hypothesis and reveal that a surprising degree of absolute position information is encoded in commonly used CNNs. We show that zero padding drives CNNs to encode position information in their internal representations, while a lack of padding precludes position encoding. This gives rise to deeper questions about the role of position information in CNNs: (i) What boundary heuristics enable optimal position encoding for downstream tasks?; (ii) Does position encoding affect the learning of semantic representations?; (iii) Does position encoding always improve performance? To provide answers, we perform the largest case study to date on the role that padding and border heuristics play in CNNs. We design novel tasks which allow us to quantify boundary effects as a function of the distance to the border. Numerous semantic objectives reveal the effect of the border on semantic representations. Finally, we demonstrate the implications of these findings on multiple real-world tasks to show that position information can both help or hurt performance.


Download the paper [here](https://arxiv.org/abs/2101.12322).
