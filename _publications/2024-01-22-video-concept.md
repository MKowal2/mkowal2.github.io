---
title: "Understanding Video Transformers via Universal Concept Discovery"
collection: publications
permalink: /publication/2024-01-22-video-concept
excerpt: 'We design a method for discovering universal spatiotemporal concepts in deep video transformers.'
date: 2024-01-22
venue: 'CVPR (Highlight)'
paperurl: 'https://arxiv.org/pdf/2401.10831.pdf'
---

**Abstract:** This paper studies the problem of concept-based interpretability of transformer representations for videos. Concretely, we seek to explain the decision-making process of video transformers based on high-level, spatiotemporal concepts that are automatically discovered. Prior research on concept-based interpretability has concentrated solely on image-level tasks. Comparatively, video models deal with the added temporal dimension, increasing complexity and posing challenges in identifying dynamic concepts over time. In this work, we systematically address these challenges by introducing the first Video Transformer Concept Discovery (VTCD) algorithm. To this end, we propose an efficient approach for unsupervised identification of units of video transformer representations - concepts, and ranking their importance to the output of a model. The resulting concepts are highly interpretable, revealing spatio-temporal reasoning mechanisms and object-centric representations in unstructured video models. Performing this analysis jointly over a diverse set of supervised and self-supervised representations, we discover that some of these mechanism are universal in video transformers. Finally, we demonstrate that VTCD can be used to improve model performance for fine-grained tasks.


Download the paper [here](https://arxiv.org/abs/2401.10831).
