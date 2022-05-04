---
layout: post
title: "Motivating Interpretability - A Researcher and Engineering Perspective"
author: "Matthew Kowal"
meta: "Springfield"
--- 

Deep neural networks (DNNs) are known to be almost fully opaque compared to traditional algorithms, even to top engineers and scientists who use DNNs. Many reasons have been proposed for why understanding the decision making process of these models is important, such as human curiosity, scientific discovery, bias detection, or algorithm safety measures and auditing. Furthermore, a model which is interpretable may exhibit more fairness, reliability, and trust to the general public [1](https://christophm.github.io/interpretable-ml-book/). Several methods to interpret DNNs in computer vision have been proposed to varying degrees of success. For example, many recent SOTA saliency map visualization methods have been [shown to be on par with some random baselines](https://distill.pub/2020/attribution-baselines/). Similar issues with other interpretability methods have been [criticized on social media](https://twitter.com/zacharylipton/status/1488665302057590787?s=21), pointing out that the reliance on these methods in mission critical situations will likely do more harm than good. 

Along with the varying degrees of success of interpretability algorithms, a viewpoint that questions the necessity of interpretability is gaining traction. For example, see [the debate at NeurIPS 2017](https://www.youtube.com/watch?v=93Xv8vJ2acI&ab_channel=TheArtificialIntelligenceChannel) where the Turing award winner Yann LeCunn vehemently opposes the viewpoint that interpretability is crucial for AI to benefit society in the vast majority of cases. While I don't disagree that many computer vision applications may not require interpretations to be safe and useful, I disagree with the implied ratios in LeCunn's arguments and believe that interpretability will play an important role in building working computer vision systems in the first place. 

I argue that there exists a guaranteed way to validate the usefulness of interpretability methods from the perspective of an engineer or researcher. More specifically, the usefulness of an interpretability method can be measured by the extent to which *findings from the use of the interpretability technique can be leveraged to design better algorithms*. In other words, when it comes to interpretability, the proof is in the pudding. If the individual explanations or model interpretations truly reveal valuable insights into a models learning or decision making process, then this should give the researcher sufficient knowledge to propose a solution to a related problem. I emphasize that the interpretation and solution will not always be produced in a short time span, these things can be difficult to come up with and take time to implement. 