# ForzaTune
Python tool to help tune your car in [Forza Horizon 3](https://forzamotorsport.net/en-us/games/fh3)

If you upgrade your car, you're able to tune the specific components.

As HokiHoshi explains in [this video](https://www.youtube.com/watch?v=qKhrvG8v6TY&t=522s)

It could be a good idea to tune your car based on the following formula

(Max – Min) * W%) – Min = Setting

to get the middle values your settings. But in general, I like my cars to set up a bit softer than the middle value.

Depends on what surface do I want to use my car, I like to change the setting by the same ratio on every component.

I pre-defined three modes: Asphalt, Mixed and Off Road. Depends on which mode I choose the tool will give me the modified “Recommended” value as well.

This script requires python3, and docopt and colorama libraries. There is a plan to create an external library independent version.

Example:

$ python3 ForzaTune.py
Plesase Choose a Mode:

1. Asphalt

2. Mixed

3. Off Road

To Exit press 'e'

Selected: 2
Mixed Selected
Weight Distribution of your car: 54
Min Springs: 65.7
Max Springs: 289.6

-------------------------------------------------------------------

Anti-Roll Bars Front Middle Value:  35.56

Anti-Roll Bars Front Recommended Value:  31.29

Anti-Roll Bars Rear Middle Value:  30.44

Anti-Roll Bars Rear Recommended Value:  29.83

-------------------------------------------------------------------

Springs Front Middle Value:  186.61

Springs Front Recommended Value:  164.21

Springs Rear Middle Value:  168.69

Springs Rear Recommended Value:  165.32

-------------------------------------------------------------------

Rebound Stiffness Front Middle Value:  5.86

Rebound Stiffness Front Recommended Value:  5.16

Rebound Stiffness Rear Middle Value:  5.14

Rebound Stiffness Rear Recommended Value:  5.04

Bump Stiffness Front Middle Value:  2.64

Bump Stiffness Front Recommended Value:  2.32

Bump Stiffness Rear Middle Value:  2.06

Bump Stiffness Rear Recomended Value:  2.01


It also takes command line argument.

Example:

$ python3 ForzaTune.py -r -w 54 -m 65.7 -x 289.6

Will have the same output. Please 'run $ python3 ForzaTune.py -h' for help. 
