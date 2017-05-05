The following section will provide common-case code snapshots to help you perform the most common operations that can be 
done using Monolith.

<div style="page-break-before: always !important;"/>
## Widgets
### TextWidget
```javascript
// Create a TextWidget
let textWidget = new Monolith.Widget.TextWidget;

// Hide the widget
textWidget.setVisibility(false); // Default is true, which will show is

// Set the text. Markdown notation is also supported
textWidget.setText("Foo");
textWidget.setText("Markdown __is supported__ **too**");

// Set the text color using HEX notation (http://www.color-hex.com/)
textWidget.setTextColor("#C61A10");

// Set the text size in pixel
textWidget.setTextSize(15);

// Set the URL highlighting color
textWidget.setUrlHighligthColor("#EE42F4");

// Enable or disable the text formatting, this includes also URL highlighting
textWidget.setFormatText(true);
textWidget.setFormatText(false);
```

### ImageWidget
```javascript
// Create the ImageWidget
let imageWidget = new Monolith.Widget.ImageWidget;

// Hide the widget
imageWidget.setVisibility(false); // Default is true, which will show is

// Set the image associated with the widget
imageWidget.setImage("path/to/image.png");

// Set the image dimensions
imageWidget.setWidth(200);
imageWidget.setHeight(50);
```

### ButtonWidget
```javascript
// Create a ButtonWidget
let buttonWidget = new Monolith.Widget.ButtonWidget;

// Set the dimensions of the button
buttonWidget.setWidth(100);
buttonWidget.setHeight(50);

// Set the color of the button
buttonWidget.setBackgroundColor("#41F492");

// Set the action associated with the button
buttonWidget.setOnClickAction(function(){
    alert("The button has been clicked");
});

// Set the action associated with the button when the user long-clicks it
buttonWidget.setOnLongClickAction(function(){
    alert("The button has been long clicked");
});

// Set the milliseconds that need to pass before a click is considered a long click
buttonWidget.setOnLongClickActionTimer(500);
```

### ListWidget
```javascript
// Create the ListWidget
let listWidget = new Monolith.Widget.ListWidget;

// Add items to the list
listWidget.addItem("First");
listWidget.addItem("Second");
listWidget.addItem("Third");

// Set the indicator of the list
listWidget.setCharacterNumber(); // Numbered list
listWidget.setCharacterCircle(); // Unnumbered list

// Set the indicator color
listWidget. setColor("#292929");
```

### CheckListItemWidget
```javascript
// Create a new CheckListItemWidget
let checkListItemWidget = new Monolith.Widget.CheckListItemWidget;

// Set the text associated with the item
checkListItemWidget.setText("Click me!");

// Customize the check appereance
checkListItemWidget.setUseSelectionMark(true); // Color the check box instead of using a check tick
checkListItemWidget.setSelectionColor("#AAAAAA"); // Set the color that will be used to color the check box
checkListItemWidget.setUseSelectionMark(false); // Use a check tick
checkListItemWidget.setSelectionCharacter("X"); // Set the character used as check tick

// Check or un-check the option
checkListItemWidget.setChecked(true); // Checked
checkListItemWidget.setChecked(false); // Un-checked

// Know it the option is checked or not
let isChecked = checkListItemWidget.isChecked();
if (isChecked){
    // The option is checked
} else {
    // The option is not checked
}


// Set the action to perform on click
checkListItemWidget.setOnClick(function(item){
    // The item parameter represents the view of the item that has been clicked
    item.setText("New text after click");
});

// Set the action to perform after a long click (1000 ms)
checkListItemWidget.setOnLongClick(function(){
    // The item parameter represents the view of the item that has been clicked
   item.setText("New text after long click");
});


// Delete the item
checkListItemWidget.removeOption();
```

### Create a custom widget
In order to create a new custom widget and add it to Monolith so than you can use it like the default ones, you have todo 
as follows.

**1**. Create a new class which extends from `BaseWidget`
```javascript
export class MyWidget extends Monolith.Widget.BaseWidget {

    constructor(){
        super(); // You need to call this to create the above hierarchy
        
        // Initialize your widget here
    }
    
    renderView(){
        // Renders the view of the widget and returns a DOMElement object
    }

    performOperation(){
        // Perform some operation
    }

}
```

**2**. Use your widget wherever you want
```javascript
// Import the widget
import {MyWidget} from '/path/to/MyWidget.js';

// Istantiate the widget
let myWidget = new MyWidget();

// Perform operations with the widget
myWidget.performOperation();

// Render the widget's view
myWidget.renderView();
```
  
**Note**  
The default widget's behaviour does **not** let the user use a single widget without a bubble container that holds it.
If you plan to render the widget's view inside a Rocket.chat room, please create a bubble and add your widget to the 
bubble, so that the bubble will render it and show it to the user.

<div style="page-break-before: always !important;"/>
## Layouts
### VerticalLayout
```javascript
// Create a new VerticalLayout
let verticalLayout = new Monolith.Layout.VerticalLayout;

// Add a widget to the bottom of the layout
verticalLayout.addComponent(myWidget);

// Add another layout inside the layout
verticalLayout.addComponent(myLayout);

// Render the layout view with all of its contents
let domElement = verticalLayout.renderView();
// Perform operations with the returned DOMElement
```

### HorizontalLayout
```javascript
// Create a new HorizontalLayout
let horizontalLayout = new Monolith.Layout.HorizontalLayout;

// Add a widget to the right of the layout
horizontalLayout.addComponent(myWidget);

// Add another layout inside the layout
horizontalLayout.addComponent(myLayout);

// Render the layout view with all of its contents
let domElement = horizontalLayout.renderView();
// Perform operations with the returned DOMElement
```

### Create a custom layout
In order to create a custom layout, all you have to do is the following.  

**1**. Create a new class that represents your layout.
```javascript
export class MyLayout extends Monolith.Layout.BaseLayout {
    
    // This represents the array of items that are 
    // being added to the layout
    _items;
    
    constructor(){
        super(); // You need to call this
        
        // Perform the layout setup
    }
    
    addItem(component){
        // Add the given component to the array of items
    }
    
    renderView(){
        // Handles the rendering of the view and returns a DOMElement object
        // It should call the renderView() method of each item in the list
    }
}
```

**2**. Instantiate your class and use it
```javascript
// Import the class
import {MyLayout} from 'path/to/MyLayout.js';


// Create the layout instance
let myLayout = new MyLayout();

// Perform operations with the layout
```

<div style="page-break-before: always !important;"/>
## Bubbles
### MarkdownBubble
```javascript
// Create the bubble
let markdownBubble = new Monolith.Bubble.MarkdownBubble("Optional text here");

// Change the bubble text
markdownBubble.setText("Text with **markdown** __inside__");

// Render the bubble
markdownBubble.renderView();
```

### AlertBubble
```javascript
// Create the bubble
let alertBubble = new Monolith.Bubble.AlertBubble;

// Set the alert title
alertBubble.setTitle("Warning");

// Set the alert message
alertBubble.setMessage("Please check your data");

// Build the view
alertBubble.renderView();
```

<div style="page-break-before: always !important;"/>
### ToDoListBubble
```javascript
// Create the ToDoListBubble
let toDoListBubble = new Monolith.Bubble.ToDoListBubble;

// --- GENERIC OPERATIONS ---

// Get the id of the bubble
let id = toDoListBubble.getId();

// Set the text associated with the bubble
toDoListBubble.setText("This bubble contains a lot of items that can be checked");

// Set the color of the text
toDoListBubble.setTextColor("#1A5418");

// Tell the bubble to format the text and so support the markdown notation
toDoListBubble.setFormatText(true);

// Disable text formatting
toDoListBubble.setFormatText(false);

// Set the highlight color for URLs
toDoListBubble.setUrlHighlightColor("#891C15");

// Set the bubble's text size in pixel
toDoListBubble.setTextSize(15);

// Set the message to show upon completion 
toDoListBubble.setCompletionMessage("The list has all been checked.")


// --- ITEMS OPERATIONS ---

// Add an item to the list
toDoListBubble.addItem("First item");

// You can specify a second parameter which tells if the item that is being added
// should be initially checked or not
toDoListBubble.addItem("Second item", true); 

// Set the text of an item
toDoListBubble.setItemText("New text", 0); // Changes the text of the first item

// Check an item
toDoListBubble.setChecked(true, 0); // Checks the first item

// Remove an item specifying the index of that item
toDoListBubble.removeItem(1); // Removes the "Second item" item, as indexes start from 0


// Tell the bubble to use selection marks when ticking the options
toDoListBubble.setUseSelectionMark(true);

// Set the character to use when ticking an option
toDoListBubble.setSelectionCharacter("X");

// Tell the bubble to color the check box when ticking the options
toDoListBubble.setUseSelectionMark(false);

// Set the color used to color the check box
toDoListBubble.setSelectionColor("#1D2565");

// Set the function to call when clicking an item
// This function will be called after the click of any of the items.
// The parameter indicates the view of the item that has been clicked
toDoListBubble.setOnItemClick(function(item){
    item.setText("New text after click");
});

// Set the function to call when long-clicking an item
// This function will be called after the long click of any of the items.
// The parameter indicates the view of the item that has been long clicked
toDoListBubble.setOnItemClick(function(item){
    item.setText("New text after long click");
});

```

<div style="page-break-before: always !important;"/>
### Create a custom bubble
In order to create a new bubble type you have to do as follows.

**1**. Create a new class which extends from `Monolith.Bubble.BaseBubble`.
```javascript
export class CustomBubble extends Monolith.Bubble.BaseBubble {
    
    constructor(params){
        super(); // Always remember to call super!
        
        // Do something with the params
        // Setup the bubble
    }
    
    customOperation(){
        // Perform a custom operation
    }
    
    renderView(){
        super.renderView(); // Again, necessary call
        
        // Return a DOMElement object
    }
    
}
```

**2**. Put the following code wherever you want. Thi can be done even inside the same file that contains the class
definition, outside the definition itself.
```javascript
Monolith.Bubble.addBubble("key", function(message){
    // Create the bubble
    let customBubble = new CustomBubble(params);
    
    // Perform the operations you want
    customBubble.customOperation();
    
    // Return the setup bubble
    return customBubble;
});
```
Please note that this function takes two parameters:
1. A `string` which defines the unique key that identifies your custom bubble.  
   A good naming conventions for this key would be using the [reverse domain name notation](https://en.wikipedia.org/wiki/Reverse_domain_name_notation)
   (e.g. `com.mycompany.bubble.custom`) which allows you to identify your custom bubble type among all the other bubbles 
   types.
2. A `function` which takes as parameter a `message` object that identifies a 
   [Rocket.chat message](https://rocket.chat/docs/developer-guides/realtime-api/the-message-object/).  
   This function is the one that creates the bubble, taking data from the parameter object, performs operation on
   it if there's the need, and then return it.
   
##### Note
All of the written above should be made **only** inside the `client` directory of your Meteor project, otherwise it will
make your application crash.