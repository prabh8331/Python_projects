# Introduction to CSS

CSS - Cascading Style Sheets

SS (style sheet) is a type of language just like ml(markup language) in html

Deprecated means the not in use anymore in programming lingo

## How to add CSS

1. Inline is useful when you want to apply to just in 1 element
2. Internal is useful when want to apply to 1 webpage website
3. External - is usefull 

Syntax:

Inline: it useful for adding css style just to one element
```html
<html style="background: blue">
</html>

```

Internal : it can apply anywhere in the document inside we can target any element, and it is useful for only one page website
```html

<html>
    <head>
        <style>
            html { /* "html" text here is called selector  */  
                background: red;
            }
        </style>
    </head>
</html>

```

External: it sits in other file
this is most used in programming
```html

<html>
    <head>
        <link    
            rel="stylesheet"
            href="./styles.css"
        />
    </head>
</html>

```

```css
html{
    background: green;
}
```


### CSS selector 
css selector help us choose where to apply css

css_selector {
property: value
}

1. Element selector : it select a perticular element tag like in below all h2 tag is selected 

```html
<h2>Red</h2>
<h2>Green</h2>
<h2>Blue</h2>
```

```css
h2{
    color: blue;
}
```

2. Class selector 
Class we can add an attribute to any html element and this class means grouping into one
.class_name {
    color: red
}

```html
<h2 class="red-text">Red</h2>
<h2>Green</h2>
<h2>Blue</h2>
```

```css
.red-text {
    color: red;
}
```

3. ID selector
Id work same as class but difference is class can be applied on multiple elements in html but ID is unique and can only be applied to one element
#ID_name {
    color: red
}

```html
<h2 id="main">Red</h2>
<h2>Green</h2>
<h2>Blue</h2>
```

```css
#main {
    color: red;
}
```

4. Attribute Selector

<h1 id="" class="" draggable="" src="" href="" attribute6="" attribure7="">sometext</h1>

html_element[attribute]{
    color: red
}

```html
<p draggable="true">Drag me</p>
<p draggable="true">Drag me</p>
<p draggable="false">Don't Drag me</p>
<p draggable="false">Don't Drag me</p>
<p>Don't Drag me</p>
<p>Don't Drag me</p>

```

```css
p[draggable] {
    color:red;
}

p[draggable="false"] {
    color:red;
}

```


5. Universal Selector 
this mean select all and apply css

*{
    color: red
}