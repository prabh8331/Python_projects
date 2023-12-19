# How does internet works 

Internet is long piece of wire and wire connects different computers to each other

Client ---- ISP ---- DNS ------- server (google)

server - computers which are 24/7 ON

ISP - internet service provider (who we pay to get internet)

DNS server-- (Domain Name System server)-- DNS server will look up in its database to find the exact public IP address of that website

get the public ip address of DNS records from website 
[nslookup](https://www.nslookup.io/)
search the google.com
copy the ip and paste serch it will land to google website


Client is the computer who is making request to server

[see under sea internet wires](https://www.submarinecablemap.com/)


# How websites works 

HTML - give the structre 
CSS - styling the website
JS - do the logic and do something and have functionality 

GO to some website and do Inspect with open chrome developer tool

now if we change some element we can actully change on the local copy of that website which gets download, and when we hit refresh it fetches the new copy

Extensions to install for this --> Live Preview, Prettier, vscode-icons

Use the Chrome for development (preferred)

## What is HTML
It define the content and structure

HTML--> HyperText Markup Language

HyperText (or Hyper link with takes us to another page)
Markup Language--> the formating of text (done through the HTML tags)
some important one e.g. <header>, <botton>, <body>

### The Heading element

```text
Tags --> everything inside a angel bracket<> called a tag , 
<> - opening tag 
</> - closing tag
<h1>Hello</h1> - this all is Element
```

```html
<h1>Hello World</h1>
```

[mdn docs heading](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements)

```html
level of heading  - on 6 levels in heading
<h1>Hello World</h1>
<h2>Hello World</h2>
<h3>Hello World</h3>
<h4>Hello World</h4>
<h5>Hello World</h5>
<h6>Hello World</h6>
```

Don't --> 
1. don't have more than one h1
2. don't skip the level of heading

Do's --> 
1. use different heading levels

## The Paragraph element
```html
<p>this is paragraph1</p>
<p>this is paragraph2</p>

```

In web development instead of just writing this is paragraph or this is content we can use Lorem Ipsum this just some text (by -> Cicero)
<www.lipsum.com>

## void element (self closing tags)

Horizontal Rule Element  
```html
<p>this is paragraph1</p>
<hr />
<p>this is paragraph2</p>

```

Break Element
```html
<p>
To see a World in a Grain of Sand<br />
And a Heaven in a Wild Flower,<br />
Hold Infinity in the palm of your hand<br />
And Eternity in an hour.<br />
</p>
```

Don'ts
1. some time people use break<br /> instead of creating new paragraph, it is recomended to create a paragraph for each paragraph
use break only when needed to break within paragraph

<br> and <br /> both are vaild but it is recomend to use <br /> because it is more readable and tells it is a void element