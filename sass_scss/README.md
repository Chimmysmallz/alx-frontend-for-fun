﻿![](Top.png)

# Requirements

> - Allowed editors: vi, vim, emacs
> - All your files will be executed on Ubuntu 18.04 LTS using Sass 3.7.4 (or higher)
> - All your files should end with a new line
> - All your Scss files should have a comment at the beginning (i.e. syntax above)
> - All your files should start by a comment describing the task
> - A README.md file, at the root of the folder of the project, is mandatory
> - The length of your files will be tested using wc


# More Info

## Comments for your Scss file:

### All your Scss file must start with a comment block

```sh
$ cat my_styles.scss
/* My style */
body {
    .container {
        color: #3D3D3D;
    }
}
$
```

## Install Sass/Scss on Ubuntu 18.04 LTS

```sh
$ apt-get install -y ruby2.5 ruby2.5-dev
$ gem install sass -v 3.7.4
$ sass --version
Ruby Sass 3.7.4
```


# Tasks

**0. Always debugging! **

File: [0-debug_log.scss](0-debug_log.scss/)

Write a Sass file that prints Hello world in the debug output.

```sh
guillaume@ubuntu:~/$ sass 0-debug_log.scss | head -n 0
0-debug_log.scss:2 DEBUG: Hello world
guillaume@ubuntu:~/$ 
```


**1. Color variable**

File: [1-color_variable.scss](1-color_variable.scss)

Write a Sass file that assigns the text color #3D3D3D to the HTML tags body and p.

- You must use a Sass variable

```sh
guillaume@ubuntu:~/$ sass 1-color_variable.scss | tail -n +2
body {
  color: #3D3D3D; }

p {
  color: #3D3D3D; }
guillaume@ubuntu:~/$ 
```

**2. Colors**

File: [2-color_variables.scss](2-color_variables.scss)

Write a Sass file that assigns:

- The text color #3D3D3D to the HTML tags body and p
- The background color #6D6D6D to the HTML tags body and h2
- You must use 2 Sass variables

```sh
guillaume@ubuntu:~/$ sass 2-color_variables.scss | tail -n +2
body {
  color: #3D3D3D;
  background-color: #6D6D6D; }

p {
  color: #3D3D3D; }

h2 {
  background-color: #6D6D6D; }
guillaume@ubuntu:~/$ 
```

**3. Nested tag**

File: [3-nested_tag.scss](3-nested_tag.scss)

Write a Sass file that assigns:

- No margin or padding in body tags
- Margin 10px to all of the p tags inside body tags
- You must use nested declarations

```sh
guillaume@ubuntu:~/$ sass 3-nested_tag.scss | tail -n +2
body {
  margin: 0px;
  padding: 0px; }
  body p {
    margin: 10px; }
guillaume@ubuntu:~/$ 
```

**4. Nested class**

File: [4-nested_class.scss](4-nested_class.scss)

Write a Sass file that assigns:

- Text color #3D3D3D to elements inside body tags
- Text color #FF0000 to any elements of class .red inside body tags
- You must use nested declarations

```sh
guillaume@ubuntu:~/$ sass 4-nested_class.scss | tail -n +2
body {
  color: #3D3D3D; }
  body .red {
    color: #FF0000; }
guillaume@ubuntu:~/$ 
```

**5. Nested child**

File: [5-nested_child.scss](5-nested_child.scss)

Write a Sass file that assigns:

- Text color #3D3D3D to elements inside body tags
- Text color #FF0000 to any elements of class .red that are the first children of the body
- You must use nested declarations

```sh
guillaume@ubuntu:~/$ sass 5-nested_child.scss | tail -n +2
body {
  color: #3D3D3D; }
  body > .red {
    color: #FF0000; }
guillaume@ubuntu:~/$ 
```

**6. Nested hover**

File: [6-nested_hover.scss](6-nested_hover.scss)

Write a Sass file that assigns:

- Text color #FF0000 to button tags
- When the user hovers over button tags, text color should change to #00FF00
- You must use nested declarations

```sh
guillaume@ubuntu:~/$ sass 6-nested_hover.scss | tail -n +2
button {
  color: #FF0000; }
  button:hover {
    color: #00FF00; }
guillaume@ubuntu:~/$ 
```

**7. Nested and nested again**

File: [7-nested_deeper.scss](7-nested_deeper.scss)

Write a Sass file that assigns:

- Font size 14px to all body tags
- Font size 16px to all h1 tags inside body tags
- Font size 12px to h1 tags of class .smaller inside body tags
- You must use nested declarations

```sh
guillaume@ubuntu:~/$ sass 7-nested_deeper.scss | tail -n +2
body {
  font-size: 14px; }
  body h1 {
    font-size: 16px; }
    body h1.smaller {
      font-size: 12px; }
guillaume@ubuntu:~/$ 
```

**8. Margin mixin**

File: [8-mixin_margins.scss](8-mixin_margins.scss)

Write a Sass file that assigns:

- Margin left and right at 10px to body tags
- Margin left and right at 15px to div tags
- You must use a mixin

```sh
guillaume@ubuntu:~/$ sass 8-mixin_margins.scss | tail -n +2
body {
  margin-left: 10px;
  margin-right: 10px; }

div {
  margin-left: 15px;
  margin-right: 15px; }
guillaume@ubuntu:~/$ 
```

**9. Extended**

File: [9-extend_list.scss](9-extend_list.scss)

Write a Sass file that assigns:

- Font size 12px to all tags of class .info
- Text color #00FF00 to all tags of class .success and extend style of the class .info
- Text color #FF0000 to all tags of class .warning and extend style of the class .info

```sh
guillaume@ubuntu:~/$ sass 9-extend_list.scss | tail -n +2
.info, .success, .warning {
  font-size: 12px; }

.success {
  color: #00FF00; }

.warning {
  color: #FF0000; }
guillaume@ubuntu:~/$ 
```

**10. Import colors**

File: [10-import_colors.scss](10-import_colors.scss)

Write a Sass file that assigns:

- Text color $red from 10-colors.scss to the class .red
- Text color $green from 10-colors.scss to the class .green
- Text color $blue from 10-colors.scss to the class .blue
- You must use @import

```sh
guillaume@ubuntu:~/$ cat 10-colors.scss
/* All my colors */
$red: #FF0000;
$green: #00FF00;
$blue: #0000FF;
guillaume@ubuntu:~/$ sass 10-import_colors.scss | tail -n +3
.red {
  color: #FF0000; }

.green {
  color: #00FF00; }

.blue {
  color: #0000FF; }
guillaume@ubuntu:~/$ 

```


**11. For each**

File: [11-loop_photos.scss](11-loop_photos.scss)

Write a Sass file that creates a class for each name in the list $list-names and assigns the background image based on the name (example below):

- You must use @import
- You must use @each statement

```sh
guillaume@ubuntu:~/$ cat 11-photos.scss 
/* All names */
$list-names: julien john sam damian;
guillaume@ubuntu:~/$ sass 11-loop_photos.scss | tail -n +3
.photo-julien {
  background: image-url("photos/julien.jpg") no-repeat; }

.photo-john {
  background: image-url("photos/john.jpg") no-repeat; }

.photo-sam {
  background: image-url("photos/sam.jpg") no-repeat; }

.photo-damian {
  background: image-url("photos/damian.jpg") no-repeat; }
guillaume@ubuntu:~/$ 
```


**12. Loop Headers**

File: [12-loop_header.scss](12-loop_header.scss)

Write a Sass file that creates H* tags, where ‘*’ is the size of the font used.

- h1 must have font size equal to 1px, h2 must have font size equal to 2px, etc.
- You must create H* tags from 1 to 5
- You must use @for statement

```sh
guillaume@ubuntu:~/$ sass 12-loop_header.scss | tail -n +2
h1 {
  font-size: 1px; }

h2 {
  font-size: 2px; }

h3 {
  font-size: 3px; }

h4 {
  font-size: 4px; }

h5 {
  font-size: 5px; }
guillaume@ubuntu:~/$
```


**13. Columns and operators**

File: [100-loop_col.scss](100-loop_col.scss)

Write a Sass file that creates classes with different width:

- col-1 with width equals to 100%
- col-2 with width equals to 50%
- col-3 with width equals to 33.3333333333%
- col-4 with width equals to 25%
- You must create .col-* class from 1 to 4
- You must use a @for statement

```sh
guillaume@ubuntu:~/$ sass 100-loop_col.scss | tail -n +2
.col-1 {
  width: 100%; }

.col-2 {
  width: 50%; }

.col-3 {
  width: 33.3333333333%; }

.col-4 {
  width: 25%; }
guillaume@ubuntu:~/$ 
```

**14. Media query #0**

File: [101-media_query.scss](101-media_query.scss)

Write a Sass file that assigns:

- Font size 20px to h1 tags
- Font size 14px to h1 tags, when your screen width is smaller than 320px

```sh
guillaume@ubuntu:~/$ sass 101-media_query.scss | tail -n +2
h1 {
  font-size: 20px; }
  @media screen and (max-width: 320px) {
    h1 {
      font-size: 14px; } }
guillaume@ubuntu:~/$ 
```


**15. Media query #1**

File: [102-media_query.scss](102-media_query.scss)

Write a Sass file that assigns:

- Font size 20px to h1 tags
- Font size 18px to h1 tags, when your screen width is smaller than 960px
- Font size 16px to h1 tags, when your screen width is smaller than 640px
- Font size 14px to h1 tags, when your screen width is smaller than 320px
- Text color #1D1D1D to h1.small tags, when your screen width is smaller than 320px

```sh
guillaume@ubuntu:~/$ sass 102-media_query.scss | tail -n +2
h1 {
  font-size: 20px; }
  @media screen and (max-width: 960px) {
    h1 {
      font-size: 18px; } }
  @media screen and (max-width: 640px) {
    h1 {
      font-size: 16px; } }
  @media screen and (max-width: 320px) {
    h1 {
      font-size: 14px; }
      h1.small {
        color: #1D1D1D; } }
guillaume@ubuntu:~/$ 
```

**16. Sort!**

File: [103-sort_strings.scss](103-sort_strings.scss)

Write a Sass file that sorts the variable $list_to_sort and prints the sorted list in the debug output.

```sh
guillaume@ubuntu:~/$ cat 103-sort_list.scss 
$list_to_sort: john anna zoe kim felicia carrie;
guillaume@ubuntu:~/$ sass 103-sort_strings.scss | tail -n +2
103-sort_strings.scss:64 DEBUG: anna carrie felicia john kim zoe
guillaume@ubuntu:~/$
```