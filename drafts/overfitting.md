This is blowing my mind. https://arxiv.org/abs/1812.11118. Our typical textbook explanation explains over-fitting by looking at high-degree polynomial features. Perhaps that case is misleading. In NNs, there are higher-capacity models which don't over-fit. 1/

I am still trying to come up with a good interpretation. First let's think of polynomial features and a single independent variable. As we know, if we use degree 1 or 2 we may fit the data quite poorly, but robustly. If we allow very large degree, we can fit *any* training data perfectly, but we expect test performance to be bad. Usually the argument stops there with the conclusion that we should not allow large capacity. However, I think the new argument is that  the over-fitting becomes so bad because with very large degree, we have *just enough* capacity to fit with huge effort. If we further increase capacity with a more flexible model, then many other good fits become possible. The highly over-fitted model then looks like a local optimum compared to other more "relaxed" models (even though both are achieving zero training loss, so this is a bit vague from me).

In a way, I think the polynomial features are a very misleading example which may have influenced our thinking too much. Not all higher-capacity models involve the highly chaotic behaviour of high-degree polynomials.



data sets as large as ImageNet [33], which has ∼106 examples and ∼103 classes, may require networks with ∼109 parameters to achieve interpolation; this is larger than many neural network models for ImageNet [11]. In such cases, the classical regime of the U-shaped risk curve is more appropriate to understand generalization. For smaller data sets, these large neural networks would be firmly in the over-parametrized regime, and simply training to obtain zero training risk often results in good test performance [42].

But that sounds like we could take ImageNet, throw away a lot of data, and improve performance! Doesn't it?



That double-u curve  is a literal depiction of the two cultures!
