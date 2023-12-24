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
            html { /* this is called selector  */  
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
