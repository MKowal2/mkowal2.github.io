---
title: "Global Pooling, More than Meets the Eye: Position Information is Encoded Channel-Wise in CNNs."
collection: publications
permalink: /publication/2009-10-01-paper-title-number-1
excerpt: 'In this paper, we challenge the common assumption that collapsing the spatial dimensions of a 3D (spatial-channel) tensor in a convolutional neural network (CNN) into a vector via global pooling removes all spatial information. Specifically, we demonstrate that positional information is encoded based on the ordering of the channel dimensions, while semantic information is largely not. Following this demonstration, we show the real world impact of these findings by applying them to two applications. First, we propose a simple yet effective data augmentation strategy and loss function which improves the translation invariance of a CNN's output. Second, we propose a method to efficiently determine which channels in the latent representation are responsible for (i) encoding overall position information or (ii) region-specific positions. We first show that semantic segmentation has a significant reliance on the overall position channels to make predictions. We then show for the first time that it is possible to perform a 'region-specific' attack, and degrade a network's performance in a particular part of the input. We believe our findings and demonstrated applications will benefit research areas concerned with understanding the characteristics of CNNs.'
date: 2021-08-17
venue: 'ICCV 2021'
paperurl: 'https://arxiv.org/abs/2108.07884'
---


[Download paper here](https://arxiv.org/pdf/2108.07884.pdf)
