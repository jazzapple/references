#####################################
# DALEX - Model - Human interface
https://github.com/pbiecek/DALEX
#####################################

# Model explainers are useful for: 
	# explaining why a model generated a prediction
	# identifying why a model did not make a correct prediction, and refine the model (Lime Huski example)
	
#modelDown package for generating HTML website summaries for predictive models

#####################################
# Deep learning
https://user2018-tutorial.netlify.com/#1
https://github.com/kevinykuo/user2018-deeplearning
http://cs231n.stanford.edu/slides/2018/cs231n_2018_lecture05.pdf
#####################################

# Inputs > linear transformations + weights (layers) > Activation (non-linear transformation) > Prediction > Loss > Optimise

# Tensors - multi dimensional arrays. E.g. video - 5D (samples, frames, height, width, channels), Timeseries 3D (samples, timesteps, features). Samples is always the first dimension

# Tensorflow: general purpose numerical computing library (with deep learning capabilities, of course!)
# Keras: high level APIs for deep learning, supports TensorFlow (and also CNTK, MXNet, ...)

# Paperspace cloud instance for deep learning

# Convolutional NNs: a sequence of Convolution Layers, interspersed with activation functions. Convolutions are filters which are combined as a representation of the data
	# Choosing layer dimensions: in general, common to see CONV layers with stride 1, filters of size FxF, and zero-padding with (F-1)/2. (will preserve size spatially)


# Recurrent Neural Networks
	# Feed in inputs sequentially rather than all at once
	# Applies and learns temporal structure of data
	# Appropriate for sequential data - NLP and time series forecasting problems
	# Many to One: Set up response variable as one time step, and our predictors are the 120 values preceding the response.
		# OR: Output a vector of 120 steps instead of 1. This still corresponds to the "many to one" picture.
	# Many to Many
		# time series distributed dense layer: outputs a prediction for each of the steps in the input sequence. Corresponds to the right-most "many to many" diagram.
		# Seq2seq/Encoder-decoder architecture:  We have an *encoder* network that summarizes the historical data into some numbers, and we also have a *decoder* network that translates these summary numbers into a forecast sequence. Each step in the prediction depends on the output and hidden state of the previous time stemp. During training, we provide the actual lagged values, and during prediction, we feed back the prediction for the previous timestep into the network. Corresponds to the middle "many to many" picture
	# Standard layer structure for recurrent data: LSTM, GRU
	# Note that predictions will be random with each run

# Fitting NNs - first goal is to minimise training loss over epochs on training data. 
	# Then on validation when over-fitting occurs (loss increases over epochs), implement regularisation	
	
	
#####################################
# Extreme Gradient Boosting (XG Boost)
https://github.com/hetong007/user2018tutorial
https://www.youtube.com/watch?v=Vly8xGnNiWs
github: https://github.com/dmlc/xgboost
forum: https://discuss.xgboost.ai
doc: https://xgboost.readthedocs.io/en/latest
#####################################

# Tree based
# Additive model. Add weak learners to each other, reducing loss/residuals each time. How? Random forest or sequentially
# Theoretically, boosting can be done with different algorithms at each stage, rather than tree based models. 
# Why choose XGBoost
	# Regularisation (mitigates over) 
	# Using both first and second order gradient - converges faster, so more efficient to train
	# Grow to a full binary tree before pruning, rather than pruning at each node
# Parameter tuning - where to look first?
	# Objective - e.g. RMSE not for classification!
	# Metric
	# eta/nrounds
# Overfitting - mitigation strategies
	# shallower trees: `max_depth`, `min_child_weight`
	# stronger randomness: `subsample`, `colsample_bytree`
	# stronger penalty: `gamma`, `lambda`
	# domain knowledge: `monotone_constraints`
# Underfitting - mitigation strategies
	# deeper trees: `max_depth`, `min_child_weight`
	# weaker randomness:  `subsample`, `colsample_bytree`
	# weaker penalty: `gamma`, `lambda`
	# parallel trees: `num_parallel_tree` - offeres a strong base model (random forest)
# Class imbalance - mitigation strategies
	# stratification in cross validation
# Increase model training speed
	# introduce histogram binning in params
	# depth-wise
	# loss-wise

#####################################
# mxnet - Amazon's deep learning framework
https://github.com/hetong007/user2018tutorial
https://github.com/apache/incubator-mxnet/tree/master/example
https://discuss.mxnet.io/
#####################################
# Context - CPU / GPU. This is why mx data types are introduced - to allow GPU compaitble computation (ctx=mx.cpu() / gpu())
# GPU compute power has great potential for training CNNs 
# MLP: A multilayer perceptron is a class of feedforward artificial neural network. An MLP consists of at least three layers of nodes. Except for the input nodes, each node is a neuron that uses a nonlinear activation function.
# Softmax layer normalises predictions. Prediction produced in the softmax layer is compared to the observed value in order to calculate loss
# Number of neurons in output layer corresponds to number of prediction classes. In mnist n = 10 as there are 10 digits
# Neural network layers: Basic building blocks:
	# Fully Connected: every node in one layer is connected to every node in the next layer
	# Convolutional: summarises info in matrix via filter. Filter subsamples the larger matrix to create feature maps (dot product) 
	# Pooling: summarises info in matrix via filter
	# Activation: introduces non-linearity between layers - translates values
# When defining layers, ensure each layer's output is fed as the next layer's input
# Shuffling images mitigates overfitting and will often result in training accuracy being on par with validation accuracy
# Pre-trained models available 
	# Image normalisation important before use, according to RGB channels - standard available publically
# Loading a pre-trained model	
	mx.model.load('model/resnet-18', 0)

#####################################
# Machine Learning resources
#####################################

# Decision tree concepts http://www.r2d3.us/visual-intro-to-machine-learning-part-1/
# Loss functions	
	# MAE more appropriate than RMSE for regression when predicted values are large
# Neural network concepts: https://playground.tensorflow.org/