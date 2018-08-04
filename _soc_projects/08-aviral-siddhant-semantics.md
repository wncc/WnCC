---
layout: soc-project
image: /images/semantics.png
title: Capturing semantic structures in Neural Machine Translation
mentor: 
- Aviral Kumar
- Siddhant Garg
category: "Machine Learning, NLP"
application_procedure: "proposal"
weight: 30
ribbon: in progress
stipend: INR 3000
contact: <a target="_blank" >Email ID</a> - aviralkumar2907@gmail.com, sid7954@gmail.com
mentees:
- Abhijeet Dubey
- Krishna Wadhwani
- Gobinath Balamurugan
---

---
#### This project is aimed towards people who are interested in ML and Neuro-Linguistic Programming; and handles Neural Machine Translation with an unusual approach 
<!--break-->

Neural Networks are being extensively used for machine translation. While tools like Google Translate might look so practically effective in translation, the accuracy (BLEU scores) of such models on test benchmarks is just in the range of 28-40%! From our initial experiments with such models, we can say that these networks essentially learn to output translations all of which carry the same semantic structure -- a different way of referring to the same thing or paraphrasing. There has been some previous work in the domain of learning to align to fixed semantic structure or learning to handle paraphrasing during NMT. We have a simple approach in mind, which we want to try out.

<!--break-->

We stick to the standard Encoder-Decoder architecture for Neural Machine Translation(NMT). To give a brief overview, a recurrent neural network (Encoder) takes the input sequence and converts it to an intermediate hidden representation on which another recurrent neural network (Decoder) operates and produces the output sequence. The standard NMT architecture involves a single encoder and decoder mechanism. Here, essentially, we want to have multiple decoders, each of which can capture a different semantic structure of the sequence. Training these multiple decoders will involve not only maximising the likelihood for prediction for each but also producing diverse outputs among themselves. If successfully learned, this model can learn to produce translations which are different ways of saying the same thing. 

<!--break-->

The motivation for this idea comes from an analogy to generative models like GANs. Often GANs suffer from mode collapse, that is they fail to capture different modes in the space of images, and rotate among different modes. Having a ‘n-way’ mixture (which essentially is implemented by multiple decoders), we can prevent such a problem from arising.

<!--break-->

#### Some (initial) relevant papers:
1. Adversarial Example Generation with Syntactically Controlled Paraphrase Networks [https://arxiv.org/pdf/1804.06059.pdf](https://arxiv.org/pdf/1804.06059.pdf)
2. Diverse Beam Search [https://arxiv.org/abs/1610.02424](https://arxiv.org/abs/1610.02424)
3. Breaking softmax bottleneck (might be interesting to see if their solution captures semantic structures too)  [https://arxiv.org/abs/1711.03953](https://arxiv.org/abs/1711.03953)

<!--break-->
#### Base Code: Tensorflow Official NMT repository  [https://github.com/tensorflow/nmt](https://github.com/tensorflow/nmt)
<!--break-->

#### Why should one choose this project?
This project is more on the lines of exploration so active participation is needed from your side not only for the coding part but also for formulating the problem and thus you will have the freedom to test and implement your own ideas as well. This will be an excellent way to venture into the field of Machine Learning (Deep Learning in specific) and can act as a solid starting point for you to pursue more projects/research in DL. This project will also involve active reading of research papers and hence can be a very hands on research experience for you.
<!--break-->

#### Who should choose this project?
A prerequisite for choosing this project is having a basic knowledge of Neural Networks and concepts of Machine Learning (Though this can also be learnt while doing the project if student is motivated and interested to learn). The student should be comfortable coding in Python and should have ability to learn to program in a new environment (Tensorflow). Any prior experience with Keras, Pytorch or Tensorflow is appreciated. 
<!--break-->

Week | Work
--- | ---
Week 1 :    |Reading Seq2Seq NMT paper and getting familiarized with the code by trying out some simple variations and trying to replicate benchmarks on some datasets
Week 2 onwards:    |Implementing a multi-decoder module in the NMT code and modifying the loss for training by incorporating cross entropy on the predicted sequence and divergence between different decoder models
 .|Testing initially on synthetic datasets for proof of concept and use this to tweak the model architecture, loss, etc to improve the prediction scores. If there are signs of the model being able to capture wider semantic structures, we can test the model on bigger datasets.


<!--break-->
#### Miscellaneous
This project might be resource intensive. Google Cloud or other Cloud platforms might be required to test full blown models, once the model seems to work on toy data.

<!--break-->
If the idea works out and results are encouraging, this might lead to an academic research paper at an NLP/ML conference. 
