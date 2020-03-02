<h3 align="center">
  <img src="assets/atari_icon_web.png" width="300">
</h3>

# Atari
This is an Space Invaders playing Machine Learning program.  Based off of a framework from wonderful programmer [Greg Surma](https://gsurma.github.io).
Research Playground built on top of [OpenAI's Atari Gym](https://gym.openai.com/envs/#atari), prepared for implementing various Reinforcement Learning algorithms.
## Purpose
This project is aimed to see how making small tweaks to the program can increase performance in Space Invaders.  This highlights the No Free Lunch Theorum that no one program can do every task.

## Large Changes
I made a couple of large changes to this project.  These include removing the Genetic Evolution sections, changing references of 'acc' to 'accuracy', and adding the option to block out the shields from the machine's view.  I cut the Genetic Evolution parts to reduce unused sections.  I changed the references of 'acc' because it would not work otherwise.  I added the ability to block out shields so that I could compare how the machine did with a different view.
A side note, I had to go into tensorflow and change a line that was calling a deprecated global variable function.  It was a pretty easy fix, but it was hard to find.

## Usage

1. Clone the repository.
2. Go to the project's root folder.
3. Install required packages`pip install -r requirements.txt`.
4. Launch atari. I recommend starting with help command to see all available modes `python atari.py --help`.

## Human Comparison
To see what this game is like to play for the machine I downloaded an atari emulator called [Stella](https://stella-emu.github.io/).

## DDQN
### Hyperparameters
	* GAMMA = 0.99
	* MEMORY_SIZE = 900000
	* BATCH_SIZE = 32
	* TRAINING_FREQUENCY = 4
	* TARGET_NETWORK_UPDATE_FREQUENCY = 40000
	* MODEL_PERSISTENCE_UPDATE_FREQUENCY = 10000
	* REPLAY_START_SIZE = 50000
	* EXPLORATION_MAX = 1.0
	* EXPLORATION_MIN = 0.1
	* EXPLORATION_TEST = 0.02
	* EXPLORATION_STEPS = 850000

### Model Architecture
Deep Convolutional Neural Network by [DeepMind](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)

<img src="assets/network_architecture.png" width="500">


	* Conv2D (None, 32, 20, 20)
	* Conv2D (None, 64, 9, 9)
	* Conv2D (None, 64, 7, 7)
	* Flatten (None, 3136)
	* Dense (None, 512)
	* Dense (None, 4)
	
	Trainable params: 1,686,180



### Performance

---

###Sources
Make sure to check out these sources which can explain these better than I can.
https://towardsdatascience.com/atari-reinforcement-learning-in-depth-part-1-ddqn-ceaa762a546f
