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