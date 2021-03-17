---
layout: soc-project
image: /images/text_editor.png
title: "Language Model Based Syntax Autocompletion in a Text Editor"
mentor: 
- Pradipta Parag Bora
- Harshit Gupta
category: "Development, Machine Learning, NLP"
mentees:

application_procedure: "proposal" 
weight: 104
ribbon: new
contact:
- Email - <a target="_blank" href="mailto:190050019@iitb.ac.in">190050019@iitb.ac.in</a>


---

---

This project aims to build an open source code editor (like Sublime Text), that uses natural language processing to create a language model for code prediction

<!--break-->
Description:

"This project aims to build an open source code editor (like Sublime Text), that uses natural language processing to create a language model for code prediction. Natural Language Processing is used widely to build models of languages that can be used to predict the sentiment/future words/infer information from languages and the idea is to build such a model out of a codebase to create auto completions automatically. A lot of papers/projects have come up on this, we will attempt to integrate everything into a nice package. Initially we will create a simple model that learns from an existing corpus of code to create general auto completions, later on we will try to extend this to be more locally aware.

Some reading (NLP):
- https://towardsdatascience.com/building-a-next-word-predictor-in-tensorflow-e7e681d4f03f#:~:text=Next%20Word%20Prediction%20or%20what,or%20emails%20without%20realizing%20it.
- https://web.stanford.edu/~chshah/files/contextual-code-completion.pdf
- https://www.tabnine.com/blog/local (what we want to achieve, although this is a professional product, if we get 20% of this it'll be great)

We will require two teams for this project, a team that will build the editor using software development framework (preferably Electron and Angular). This team will have to be proficient in software development (you can learn!). The goal is team to make a working (and good looking) code editor that is able to integrate with the code completion system easily and effectively.

Links:
- https://www.sitepoint.com/build-a-desktop-application-with-electron-and-angular/
- https://www.electronjs.org/

The Second team will work on the NLP model. The mentors will work with them to build a good model that works decently. The aim is to initially create a language model from the code corpus and then try to implement some recent papers that add in more local awareness. We may investigate using classical code completion methods (like the ones in used in Sublime Text) to augment the NLP based approach.


No. of mentees: 4 - For ML, 4 - For Development


Proposal:

We will take around 4-5 people for the development team and around 4 people for the NLP side of things. For the development team, we need good proficiency in programming (could be a really great cs101 project, or some side stuff you've been doing) or ability to learn things quickly. We will take an interview, and people who have made apps, websites, games etc will be preferred. Ability to code in Javascript and knowledge of web frameworks is a big bonus (you will be expected to learn this during the gap if you are not able to do so)

For the ML team, you need to know decent amount of programming (in python preferably) and also have good math skills and should be able to pick up and learn things quickly. You will be expected to learn basics of ML/DL and also NLP during the gap period so that we can work on the final problem together. Research papers would also have to be implemented (using TensorFlow/PyTorch as per you) and so if you know a deep learning framework it's a plus (although not required)
Please mention your programming experience, motivation, interest, willingless to learn in the proposal.
We may take interviews. Please mention which team you want to work in in the proposal. You may have to study things during the gap period.


<!--break-->

<!--break-->
### Tentative Project Timeline (ML):

|Week Number  | Tasks to be Completed|
|--- | --- | 
|**Week 1-2** |Study basics of DL (starting with neural networks) and NLP (Stanford CS224N will be followed) We will tell what to study, only the required parts are to be covered. If you know this already, start reading the papers. Gap Period: Get proficient with DL and NLP. Learn PyTorch or Tensorflow and code basic things in these frameworks.|
|**Week 3** | Implement/Run the Stanford Project paper linked above and see how it works to create the language model. Create an API that can integrate with the other team effectively. |
|**Week 4** | Improve the model (we'd have to see how!) and add local heuristics to augment the NLP model. |
|**Week 5** | Investigate local contextual awareness by extending the window of input to the model, try other strategies to add localisation to the model. Add everything to the API. |
|**Extra Week** | Nothing much, strategising and creating a good model is all |

### Tentative Project Timeline (Dev):

|Week Number  | Tasks to be Completed|
|--- | --- | 
|**Week 1-2** |Familarise yourself with Electron and Angular. Make some basic working prototypes. You may use other frameworks but we won't be able to help there. Once done, start making a simple editor.|
|**Week 3** | Add file IO, syntax highlighting and also provide endpoints to link the API|
|**Week 4** | Add project view, improve UI.|
|**Week 5** | Wrap up and bind with the API provided by ML team|


### Checkpoints (ML):
<!--break-->

|Checkpoint Number  | Progress|
|--- | --- | 
|**1** |Basic theory of DL. Basic tutorial of Tensorflow/Pytorch|
|**2** |RNN/Attention and simple NLP model (Word2Vec)|
|**3** |Implement basic language model (stanford paper)|
|**4** |Add API and link it. Improve the model.|
|**5** |Add local awareness to the model for better predictions.|

### Checkpoints (Dev):
<!--break-->

|Checkpoint Number  | Progress|
|--- | --- | 
|**1** |Basic Angular apps in Electron|
|**2** |Working basic code editor in Angular|
|**3** |File IO/Syntax Highlighting|
|**4** |Project view, add extra features (templates/keyboard shortcuts)|
|**5** |rap up and create final deployment code.|


<!--break-->
