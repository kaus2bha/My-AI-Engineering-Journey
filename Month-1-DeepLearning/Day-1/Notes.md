🎯 Today's Learning Goals

By the end of today, you should be able to answer:

Why wasn't Machine Learning enough?

Why were Neural Networks invented?

How does a neuron "think"?

What are weights?

What is bias?

What is an activation function?

Step 1 (30 minutes)
Watch ONE video.

3Blue1Brown – But what is a Neural Network?

This is, in my opinion, one of the best explanations ever made.

Don't take notes.

Step 2 (45 minutes)

Read:

Neural Networks from Scratch

1.Why wasn't Machine Learning enough?
---> machine learning is a basic thing when we think about neural network and ai. machine learning focuses on mathematical learning concepts like regression, clustering, mean, mode, median of array including libraries like pandas matplotlib and numpy. while neural network uses machine learning to expand the view broader. where we see multiple neurons working to figure things out.

Why were Neural Networks invented?
---> Neural network is based on machine learning concepts and we can even say thats its a broader vision of machine learning. taking a living example as we know english is a language but english is not everything in life unless its applied somewhere. just like that machie learning is! we can learn machine learning but to apply the knowledge gained by learning ML has to be applied somewhere. and that application is neural network. and thats why neural network were invented to apply machine learning concepts in real life to solve real world problems.

How does a neuron "think"?
---> There are multiple neurons in a neural network just like there are multiple cells in a muscle. a neuron thinks and calculates the result accordingly to the weight it has. the weight could be negative or positive. and after using the sigmoid function we can conclude the result.  now a day we no more use the sigmoid function. but something else im unable to remember the name of it as of now.

What are weights?
---> weights are assigned to every neuron which could be positive or negative. for example if we are scanning a picture if a blurred 7 in a neural network the pixels where the traces of the body of the number 7 are visible will be weighted positively and wherever the image has empty or black default pixels it will be counted as negetive or zero weight depending on the case. and by calculating the positive weighted pixels the neural network assumes that its a 7. 

What is bias?
---> sigmoid function provides results on the scale of 0 to 1 but if and only if i want that result in another format of range then i can add my own mathematical equation or operation in the sigmoid function and based on that my result will change or that operation will bias my result so thats what is known as bias.

What is an activation function?
---> An activation function activates the neuron to pass the information to the further stage after calculating the weight distribution on a neutron it actively takes part in the operation of neural network and thats where the neuron(function) activates in the network so its also called activation function.


1️⃣ Why wasn't Machine Learning enough?
Your Answer: 7.5/10

You correctly understood that neural networks build on machine learning.

However, one important point is missing.

Machine Learning wasn't "not enough."

It had limitations.

For example:

Classical ML struggles with:

Speech recognition
Image recognition
Language generation
Complex pattern recognition
Huge datasets

Imagine showing 1 million cat pictures.

A Decision Tree won't magically learn cats.

A Neural Network can.

Better intuition

Machine Learning required humans to tell the model:

"Look at ears."

"Look at eyes."

"Look at whiskers."

Neural Networks learn these features by themselves.

That changed AI forever.

2️⃣ Why were Neural Networks invented?
Your Answer: 6.5/10

This is where I'll challenge your thinking.

You wrote:

Neural Networks apply Machine Learning.

Not exactly.

Neural Networks are one family of Machine Learning algorithms.

Think of it like this:

Artificial Intelligence

      \|/

Machine Learning

       \|/

 ├── Linear Regression

 ├── Decision Trees

 ├── SVM

 ├── Random Forest

 └── Neural Networks

Neural Networks don't sit above Machine Learning.

They are inside it.

That's an important distinction.

3️⃣ How does a neuron think?
Your Answer: 9/10

This was surprisingly good.

Especially this line:

according to the weight it has.

Excellent.

That is exactly what happens.

A neuron asks:

Which inputs matter more?

Weights answer that question.

The only thing missing:

A neuron doesn't "know."

It computes.

It has no intelligence.

It simply performs:

Input

↓

Multiply

↓

Add

↓

Activation

↓

Output

Millions of these tiny computations together create what looks like intelligence.

4️⃣ What are weights?
Your Answer: 10/10

This was my favorite answer.

The "blurred 7" example is excellent.

That tells me you're beginning to visualize how neural networks see images.

Exactly what I wanted.

Well done.

5️⃣ What is bias?
Your Answer: 4/10

This is the biggest misconception today.

Don't worry.

Almost everyone gets this wrong.

You wrote:

Bias changes the sigmoid output.

Not quite.

Bias is added before the activation function.

Think of it like this.

Suppose

Age = 20

Weight = 2

Result

20 × 2 = 40

Now add bias

40 + 5 = 45

NOW

45 goes into the activation function.

Bias simply shifts the neuron's decision threshold.

A good analogy:

Imagine opening a door.

Without bias

The door opens if someone pushes with 50 N.

With bias

Maybe it now opens with 40 N.

Or 60 N.

Bias changes how easily the neuron activates.

6️⃣ What is an activation function?
Your Answer: 8.5/10

Good intuition.

One improvement.

Activation doesn't merely "activate" the neuron.

It decides

Should this information continue?

Without activation functions...

Every neural network becomes nothing more than one giant linear equation.

No matter how many layers you add.

This single idea changed AI history.

Overall Score
Topic	Score
Why ML wasn't enough	7.5/10
Why NN invented	6.5/10
Neuron	9/10
Weights	⭐ 10/10
Bias	4/10
Activation	8.5/10
