## Purpose
The following document will explain how to use **Monolith - An interactive bubble provider**, the stand-alone 
[Atmosphere.js](https://atmospherejs.com/)-hosted package developed by [NPE Developers](https://github.com/NPE-Developers).

The purpose of Monolith is to provide an SDK which will let the developer that uses it create one of the default bubble 
types that are present inside it, or extends them to create new kinds of bubble, that will be shown inside a 
[Rocket.chat](https://rocket.chat/) room as interactive messages.

## Recipients
This documents has been written thinking about all the developers that will use Monolith inside their Meteor's project. 
Because of that, the language used is highly specific and detailed. 

## Contents
This guide contains all the information about how to create, use or extend each kind of widget, layout or bubble that is 
already present inside Monolith.  
Before all of that, it will also explain how to install Monolith and getting started for using it.

## Getting started
### Installing Monolith
To install Monolith you will need the following things:
* an internet connection;
* the knowledge on how to setup a [Meteor](https://www.meteor.com/) project.

Once you got both of the two, the only things that are needed in order to start using Monolith inside your Meteor project, is to go inside the root folder of your project, and type the following shell commands:
```
> meteor install monolith
> meteor reset
> meteor npm install
> meteor run
```
**Note**. This procedure will erase all the temporary files that might have been created during previous project
runs (such as databases, logs, etc.), but it will ensure that Monolith is properly installed.

### General knowledge on classes' structure
The basic classes that are present inside Monolith are the following.

**`Monolith`**  
God object which contains all the data relative to the components that can be instanciated inside the project which is 
using the SDK itself.

**`BaseComponent`**  
Represents a base component, which can either be a layout or a widget, that can be placed inside a bubble.

**`BaseLayout`**`extends BaseComponent`  
Represents a base layout, which holds a serie of other `BaseComponent` inside it, displaying them in a certain way.  
This class than extends into two classes:
* `HorizzontalLayout` which holds all the components inside it one next to the other, starting from the left and going to the right;
* `VerticalLayout` which holds all the components inside it one below the other, starting from the top and going to the bottom.

**`BaseWidget`**`extends BaseComponent`  
Represents a base widget, which is the most basic part that a bubble is composed of.  
This class extends into the following widget classes:
* `TextWidget`: represent a text that can be formatted using the Markdown notation;
* `ButtonWidget`: represents a customizable button;
* `ImageWidget`: represents a view which displays the associated image;
* `ListWidget`: represents an unnumbered list;
* `CheckListItemWidget`: a check-list item, which is made of a checkbox and a text.

**`BaseBubble`**  
Represents a basic bubble, which has a layout that holds all the components inside it.  
This class is used as parent for the following bubbles:
* `MarkDownBubble` which represents a bubble that shows a Markdown-formatted text;
* `AlertBubble` which is used to display alerts to the user;
* `ToDoListBubble` which holds a text and a to-do list.