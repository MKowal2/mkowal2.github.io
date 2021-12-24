---
title: "Category Specific Feature Binding for Semantic Segmentation and Adversarial Robustness"
collection: publications
permalink: /publication/2020-06-01-feature-binding
excerpt: 'We propose a new type of data augmentation for dense labelling tasks. We train neural networks to seperate and label mixed images based on their co-occurance probabilities.'
date: 2021-10-01
venue: 'BMVC (Oral)'
paperurl: 'https://arxiv.org/pdf/2008.05667.pdf'
---

**Abstract:** In this paper, we present a strategy for training convolutional neural networks to effectively resolve interference arising from competing hypotheses relating to inter-categorical information throughout the network. The premise is based on the notion of feature binding, which is defined as the process by which activation's spread across space and layers in the network are successfully integrated to arrive at a correct inference decision. In our work, this is accomplished for the task of dense image labelling by blending images based on their class labels, and then training a feature binding network, which simultaneously segments and separates the blended images. Subsequent feature denoising to suppress noisy activations reveals additional desirable properties and high degrees of successful predictions. Through this process, we reveal a general mechanism, distinct from any prior methods, for boosting the performance of the base segmentation network while simultaneously increasing robustness to adversarial attacks.


Download the paper [here](https://arxiv.org/abs/2008.05667).
