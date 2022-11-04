---
title: "Quantifying and Learning Static vs. Dynamic Information in Deep Spatiotemporal Networks"
collection: publications
permalink: /publication/2022-03-02-static-dynamic
excerpt: 'We quantify, and design algorithms to learn, static and dynamic information in deep spatiotemporal networks.'
date: 2022-03-02
venue: 'Arxiv pre-print, 2022'
paperurl: 'https://arxiv.org/pdf/2211.01783.pdf'
---

**Abstract:** There is limited understanding of the information captured by deep spatiotemporal models in their intermediate representations. For example, while evidence suggests that action recognition algorithms are heavily influenced by visual appearance in single frames, no quantitative methodology exists for evaluating such static bias in the latent representation compared to bias toward dynamics. We tackle this challenge by proposing an approach for quantifying the static and dynamic biases of any spatiotemporal model, and apply our approach to three tasks, action recognition, automatic video object segmentation (AVOS) and video instance segmentation (VIS). Our key findings are: (i) Most examined models are biased toward static information. (ii) Some datasets that are assumed to be biased toward dynamics are actually biased toward static information. (iii) Individual channels in an architecture can be biased toward static, dynamic or a combination of the two. (iv) Most models converge to their culminating biases in the first half of training. We then explore how these biases affect performance on dynamically biased datasets. For action recognition, we propose StaticDropout, a semantically guided dropout that debiases a model from static information toward dynamics. For AVOS, we design a better combination of fusion and cross connection layers compared with previous architectures.

Download the paper [here](https://arxiv.org/abs/2211.01783).
