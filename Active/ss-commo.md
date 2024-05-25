<!--==================-->
# 🔑 Keywords
<!--==================-->
```yaml Universal Principles
# UNIVERSAL PRINCIPLES
Conciseness: Be Abrupt. To the point
Abstraction: Finetune level of detail
User Level: The *what*. Intention of writer
Implementation: The *how*. Tools used to accomplish tasks
ELI5: General Logic. No programming concepts.
General Coder: Loops. Conditionals. Etc
Niche-Programmer: Language specific syntax
Precision: Use the right words for the job
```
```yaml Code Parsing
# CODE PARSING
Mind Your Words: Distinguish between similar, but diff words
ABCD Framework: Anomalies, Behavior, Concepts, Details
LTR and RTL: Emphasize What?
DRY: Don't repeat yourself
Nested Messiness: Referring to nested levels
```
```yaml Code Alongs
# CODE ALONGS
Vocalize Everything: Don't get silent
Multimodal: Speak & Write
Expectations: Explain what you expect code to output
Announce as you do: Explain as you write lines of code
Minimize Negativity: Avoid certain words
```
```yaml Feynman
# FEYNMAN
Analogies: Connect to strong-points
Associations: Cater to audience
Examples: Principle targeted examples
WPW: Moving through abstraction layers
```

<!--==================-->
# 🪲 Deets
<!--==================-->
## _UNIVERSAL PRINCIPLES_
> These are principles that apply to the rest of the types of communication. I like thinking of the major principles with the acronym `CAP` (Conciseness, Abstraction and Precision). Being concise and precise is self explanatory, however, abstraction might need a bit more explanation.

<details><summary>🐧 Abstraction Layers</summary>

> The power of 3. No matter how you slice it there are about 3 levels of abstraction. I divided the type of communication that will be done into 3 types (1) Code Parsing (2) Code Alongs and (3) Feynman. Below, I will go over what the different abstraction layers look like for each communication type.

There are `user-level` and `implementation` explanations. The `implementation` explanation can be further broken down into `language-agnostic` and `language-specific`. Another way to think about it is that there are 3 levels of abstraction. Lv1 is the user-level description where you ware explaining to a non-programmer the concepts. Level 2 and 3 are for programmers.
>  ```yaml
>  Lv1: ELI5, General Logic
>  Lv2: Comp-sci student
>  Lv3: JS Developer
>  ```
</details> <!---------------------->

<details><summary>🐝 Code Parsing</summary>

> Start off with what the developer intends to do. Typically this can be extracted from variable names. If a function is called `addTwoNumbers`. The name abstracts away the implementation. However, if more detail needs to be added, then go inside of the code and start with the general programming concepts: loop, conditionals, general data structures, etc. Lastly, explain the general syntax of the programming language.
</details> <!---------------------->

<details><summary>🐝 Code Alongs</summary>

> Following the PEDAC process naturally helps you foollow this level of abstraction. The `high level overview` is level one where you follow general logic. The next implementation is where you bring over the general programming tools `conditionals, loops, etc`
</details> <!---------------------->

<details><summary>🐝 Feynman</summary>

> There are still 3 levels of abstraction here, but the 3 levels are slightly different. In terms of programming, it might look something like this.

```yaml
Level1: Concept. Introduce the concept. Definition. Analogy.
Level2: Important Details
Level3: Other Details. Usually a concrete example.
```

```yaml
Concept: First class function. Functions can be used anywhere a value can be used
Key Details: Assignment to var, fn argument, return from fn
Other Details: Concrete example. Edge Cases where it doesn't behave as expected
```
</details> <!---------------------->

## _CODE PARSING_
> Code Parsing refers to reading code that someone else has written. It can also be code that you've written and are explaining to someone else.

<details><summary>🔍 Mind Your Words</summary>

> Certain words are similar but have different meanings. They might be the same parts of speech but different. Examples include `arg`  vs `parameter`. Both nouns, but mean slightly different things. Or they might be similar in that once is a verb and the other is a noun. An example is `invocation` and `invoke`. One is a noun and the other is a verb. Mind your words.
</details> <!---------------------->

<details><summary>🔍 ABCD Framework</summary>

> `ABCD` framework is a checklist of things to look for when parsing code. It stands for anomalies, behavior, concepts and details/description.
</details> <!---------------------->

<details><summary>🔍 LTR and RTL</summary>

> English is a `LTR` language, meaning it's read left to right. The subject is the focus of a sentence. When parsing code, the subject seems a little mysterious. Is it the `JS Engine` or is it the `Interpreter`. Even if you know the answer, it seems like unnecessary mental overload to specify a detail that seems trivial. When the subject is not known, it makes sense to read `RTL`. The key to knowing what to use is to discern what to focus. Do you focus the action? Do you focus the value? Use this to decide whether to read LTR or RTL.

> In addition to knowing the direction to read code, another way to think about reading code is in terms of scope. Start from bigger scope to smaller scope as well as reading from top to bottom
<!--~~~~~~~~~~~~~~~~~~-->
```yaml
# LTR
Variables: Declaration, Initialization, Assignment
Functions: Definition, Parameters, Invocation

# RTL
Methods: Standard library Methods
Properties: Standard Library Properties
```
</details> <!---------------------->

<details><summary>🔍 DRY</summary>

> Don't repeat yourself. It can get wordy to be 100% correct at all times. Object references are stored in variables. Establish that fact at the time of initialization, however, after that refer to the array by its variable name. `varName array` vs `the array referenced by varName`. The latter is not bad either, but can get wordier. Choose your poison.
</details> <!---------------------->

<details><summary>🔍 Nested Messiness</summary>

> Think of Inception. How do you refer to the 4 levels of a dream? The most obvious way is to refer to it by the level's distinguishing feature. Hotel level. Snowy Level. You can use a number, but it can be messy to count the level with all the nested delimiters and be too much mental overhead. The first and last levels can be referred to by their relative placement in the bigger whole. The same philosophy can be used with code. The levels on both ends can be called `outer` and `inner` and even `middle`. Using these relative words reduces mental overhead and communicates to the audience in a way that is easy to understand.

If a nested layer is named, you can refer to the layer by its name. In Inception, you say `limbo` and it's clear that you're referring to level 4. Likewise, use similar techniques to refer to the correct nested level. Generally speaking, if you over nesting, there is probably a chance that the code could be optimized and refactored. There is most likely some logic that can be abstracted out.
</details> <!---------------------->

## _CODE ALONGS_
> Code alongs is what I call having someone else along as you code. It's good to remember that there is someone else next to you and include them. Vocalize everything, write and speak to make everything be as CLEAR and easy to understand as possible. It's good to give a preview such as `I expect this to log ___ to the console` before you run the console itself. Generally speaking, this kind of clarity comes from a strong understanding of the logic behind the problem. If the logic behind the problem makes perfect sense, then it's easier to communicate that effectively. Lastly, things aren't going to go as expected. There will be syntactical errors, spelling errors, logical blunders. Anticipate that and don't express any form of negativity during the interview.

## _FEYNMAN_
> `Feynman` refers to an excellent physics teacher who taught complex topics in a simple, digestible way. I included this category here because there might be situations where the other player might not grasph a concept from either `code parsing` or `code alongs`. This is where a more in depth `feynman` technique might come into play. All of this is playing with semantics, however. The other two modes focus on actual examples to teach a concept. When the other person doesn't understand, you can bring analogies, associations (that the audience might know) to leverage their prior knowledge or other, more targeted examples.

<details><summary>🔍 Whole Part Whole</summary>

> `WPW` is about walking down the abstraction levels effectively. You want to be able to connect the bigger picture with the details or the branches from the leaves. You want to be able to leverage both the `focused` and `diffused` modes to make sure the concept is understood deeply at all abstraction levels.

</details> <!---------------------->
