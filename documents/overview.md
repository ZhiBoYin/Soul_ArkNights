## brief description:

​    soul-knights liked game with arknights characters and story.

## systems:

description of all aspect of the game

**1.object:**

*logical:*

- *object ID:*

  ​	a unique integer for each object

**1.1 visual object(object):**

*visual:*

- must have body:

​		require a picture or a set of pictures

logical:

- must have global position:
  - require x-y-z coords
- must have facing direction

##### 1.1.1 touchable object(object):

*logical:*

- collision box:

​		require x-y-z coords

​		require width and length(height are assumed to be infinite.[across all z-axis])

**1.1.1.1character(visual object,touchable object):**

*visual:*

- Optional[display of name]

- Optional[display of health point]

- animation when move

- animation when use skill

- animation when attack

- animation when be attacked


*logical:*

- name

- health point
- able to move in plane:

​		require x-y coords 

​		require speed

​		require facing-direction

- interactions (a list)

##### 1.1.1.1.1 enemy(characters)

visual:

- animation when attack
- animation when be attacked

logical:

- able to attack
- able to be attacked

##### 1.1.1.1.1.1 elite enemy(enemy)

visual:

- animation of use skill

logical:

- able to use skill

##### 1.1.1.2 interactable characters (characters)

logical:

- have a list of interactions(class)

1.1.1.2.1 player(interactable characters)

##### 1.1.1.2attack(touchable object):

visual:

- appearance of attack

logical:

- position:
  - require x-y coords

- range of attack

- amount of damage
- from which character
- condition that once it was achieved the attack object will be deleted

##### 1.1.1.2.1special attack(attack):

logical:

- special effect(class)
