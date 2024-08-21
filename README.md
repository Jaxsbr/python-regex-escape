# python-regex-escape

While learning python I was tasked with replacing text with markdown urls. Due to my lack of knowledge and subsequent learnings, I want to share the solutions to illustrate how code can be simplified with iteration

## Solutions

There are three functions, each improving on the former in simplicity and readability.

### Noob

The worst version. This contains place holder logic to avoid inner `[]` from interfering during Url replacement.
[noob_replace() = 50 lines](https://github.com/Jaxsbr/python-regex-escape/blob/main/pythonregexescape/main.py#L32-L81)

### Regex

This is much cleaner/shorter than [Noob](#noob), and uses complex regex patterns to escape the names during Url replacement.
[regex_replace() = 11 lines](https://github.com/Jaxsbr/python-regex-escape/blob/main/pythonregexescape/main.py#L84-L95)

### Simple

This is even more compact and readable and improves further on [Regex](#regex). The complexity of regex is foregone, and a simple dictionary key iteration and direct replace is used instead.
[simple_replace() = 7 lines](https://github.com/Jaxsbr/python-regex-escape/blob/main/pythonregexescape/main.py#L98-L103)

## Problem

Given a generated text, replace the known `names` with markdown Url's.
Additionally, don't replace the search term ("John") with a Url,
also be carful of special characters in names ("John Citizen [XR]")

### Given Text

```
"Here are the options that match your contact search criteria for the name "John":"
" - Johnathan"
" - John Farmer"
" - John Johnson"
" - John Citizen [XR]"
"Please pick a specific option from the given list."
```

### Expected Response

```
Here are the options that match your contact search criteria for the name "John":
 - [Johnathan](https://mycompany//user/id=1)
 - [John Farmer](https://mycompany//user/id=2)
 - [John Johnson](https://mycompany//user/id=3)
 - [John Citizen [XR]](https://mycompany//user/id=4)
Please pick a specific option from the given list.
```
