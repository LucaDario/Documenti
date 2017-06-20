/**
 * Created by Utente.
 * Date: 16/06/2017.
 */

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





// Create the ImageWidget
let imageWidget = new Monolith.Widget.ImageWidget;

// Hide the widget
imageWidget.setVisibility(false); // Default is true, which will show is

// Set the image associated with the widget
imageWidget.setImage("path/to/image.png");

// Set the image dimensions
imageWidget.setWidth(200);
imageWidget.setHeight(50);




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



