# The HTML Boilerplate

```html
<!-- this is to add comments in html-->
<!DOCTYPE html>  <!-- DOCTYPE declaration, this tells the version of the HTML in which this code is written latest version is 5-->
<html lang="en">  <!-- this is the root of the document, this is the html tag in which our html code will come, lang attribute specify the language of the code, it is not for the actually user who can see the screen but the screen readers technologies so that it pronounce it correctly -->

    <head> <!-- between this head tag we set few values this is not shown in actual website-->
        <meta charset="UTF-8"> <!-- this is the meta tag to set the charset, UTF-8 will include emoji and all, if your code include any emogy and it is set to ascii then that will not work -->
        <title>My Website</title> <!--this is the title which gets displayed in tab bar-->
    </head>

    <body> <!--between this body tag every thing which will be shown in website will come will be shown -->

        <h1>Hello World!</h1>

    </body>

</html>

```

show all the bolierplat --> ! then enter


[mdn docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/)

```
## list elements in HTML
1. Unordered List 
ul - unordered list
li - list items
syntax--> 

<ul>
    <li>Milk</li>
    <li>Flour</li>
    <li>Water</li>
</ul>


2. Ordered list
ol -- ordered list
syntax -->
<ol>
    <li>Milk</li>
    <li>Flour</li>
    <li>Water</li>
</ol>


```

## Nesting and Indentation 
it is best practice to Indent the code to make it look better

can also use vscode indent line to qc the code

## Anchor Element
Attributes of html elements goes in opening tag,
attributes adds a additional information 

```html
<!-- html attributes -->
<tag attr1=value attr2=value>content</tag>

<!-- Anchor Element , href is reserved for anchor element only-->
<a href="https://google.com">This is a link</a>

<!-- Globle atteibute which can be applied to any element -->
<a draggable=true>this is a link</a>
```

### Image element
similar to Lorem Ipsum <www.lipsum.com> we have <https://picsum.photos>

```html
<!-- syntax of image element, it is a void element so it does not have close tage -->
<img src="url" />

```

