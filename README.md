# OOD-AE2

## Introduction

This project sought to create a web page that converts three user input values representing RGB values into a six-character hexadecimal code. Given that this was a project about colour, aesthetics considerations do come into play. Consequently, it was important not just to ensure that the calculator was mathematically functioning, but also that the colours red, green and blue as well as the colour that comes from the RGB inputs were incorporated into the user experience of the site. This project followed a very linear development pattern, but did use unit testing rather than integration testing, since unit testing was necessary to detect where any potential faults may be in the factory design pattern used for the creation of classes/objects in this project's code.

## Requirements

Since the project is visually oriented, this ineviitably required the creation of a low-fi prototype, which was created in figma as a response to the first ticket. The project would need to be completed as a Django project which could be created locally by cloning the git repository and then linked to the remote repository in GitHub in the form of git branches for each of the major three components of the development process. These three components would be: 1) the coding of the classes and object-oriented design patterns by which the RGB-to-hexadecimal conversions take place; 2) the creation of html templates for both the home page and hexadecimal result page of the website, encoding the colour scheme into the templates, as well as the creation of httprequests in a views.py page linking the two pages/urls together; 3) the creation of tests for the classes and methods created in the first step. These three steps follow in a consequential manner. Although the intermediate of the three steps could conceivably have been divided into still further fewer steps, the interdependence of both the http requests linking the two pages together and the html templates meant that it made sense to execute both tasks within a single git branch.

## Implementation

After the first ticket for the creation of a lo-fi prototype, three tickets were created in the repository for this project, one for each of the aforementioned three phases of the development process. The three local branches were named 'models-code' (in reference to the models.py file and the programming therein), 'webpages' (denoting the creation of the http requests and html templates) and 'tests'. 

### Models

A factory desgin pattern was used for the interaction of classes. All classes inherited in some way, directly, or indirectly, from the base class 'HexBase', which contains just a constructor that uses the input arguments (which stand for the red, green and blue values of an RGB triplet). The constructor ensures that the input values are converted to integers or set to 0 should no input values by entered by the user. 'HexRegular' inherits from 'HexBase' but contains methods for the conversion of decimal numbers to hexadecimal numbers. The method 'convert_digits' converts numbers ranging from 10 to 15 into their hexadecimal equivalents (A to F) whilst the subsequent method 'hexify' uses 'convert_digits' to convert any given integer in the range of 0 to 255 into a two-character-long string (such as 'FF' for 255). The final method, 'result', takes the red, green and blue inputs stored in the constructor and then uses 'hexify' to return a six-character-long string concatenated from the 'hexify' results for each input value. The third, class, 'HexLimiter', largely inherits from 'HexRegular' with the caveat that it uses the method 'limiter' to redefine any input values above 255 as 255 and any below 0 as 0. The final factory class, 'HexFactory', iterates through the input red, green and blue values to detect for any out-of-range numbers, and then chooses which of the 'HexRegular' or 'HexLimiter' classes to return the result.

### Webpages

Two templates, 'home.html' and 'hexresult.html', were created user input and hexadecimal code output pages respectively. In the views.py file, the functions 'home' and 'hexresult' were created to create and httprequest pathway between the two html pages, whilst the fiile urls.py was used to ensure url pathway between the two pages. The html pages needed to be created first so that they could then be referred to and used in the views.py file. However, the variable 'result', defined as the output of 'HexFactory' given user niputs, needed to be defined in the views.py file so that this result could then be used as a hexadecimal code for the colours that would be used in the 'hexresult.html' file. In both html files, content was placed in the direct center of the screen. The colour scheme for 'home.html' was largely monochrome, with the exception being that the user input text in each of the red, green and blue input boxes was colour coded. The background colour for the 'hexresult.html' file comes from the hexadecimal value in the 'result' variable, whilst the 'back' button and the six-character code itself are both white characters contained within small black boxes.

## Testing

Since the design pattern of the objects/classes is a factory design pattern, involving multiple instances of inheritance, it was logical to use unit testing. The code is highly interdependent, and integrated testing would not be able to detect where in the causal chain any code may be malfunctioning. An initial smoke test was performed, followed by tests for each of the four classes on their relative capabilities ('HexRegular' was only tested for inputs in the range of 0 to 255, whereas 'HexLimited' was also trained on numbers outside of this range, since its purpose is to take and alter out-of-range input numbers). Testing for the ability of the code to deal with non-integers was not necessary, since the 'home.html' template already forces users to input integers only, thanks to the 'type="number"' tag option in html.

## Deployment

<img width="1275" alt="Screenshot 2023-03-31 at 01 01 04" src="https://user-images.githubusercontent.com/122615093/228992906-b848e233-364d-4730-969b-ca60745de512.png">
Since the possibility of the code taking empty strings ('') as inputs was eliminated by the 'HexBase' constructor, the home page can return hexadecimal RGB value even when the user offers not inputs at all.


<img width="1275" alt="Screenshot 2023-03-31 at 01 02 08" src="https://user-images.githubusercontent.com/122615093/228992978-8879008e-b296-4598-bad2-89ae07f4ba9c.png">
However, when users *do* type in values, the colour-coding of the digtis they are typing will help remind them which of the red, green or blue values they are specifying at that moment.


<img width="1270" alt="Screenshot 2023-03-31 at 01 02 56" src="https://user-images.githubusercontent.com/122615093/228993002-e964fa2a-a345-432c-825d-bef99e5babdc.png">
Not only that, but the website also accommodates the fact that many individuals cannot be expected to know that RGB values have to be between 0 and 255. Conssequently, it will still be able to function even when given out-of-range input numbers.


<img width="1275" alt="Screenshot 2023-03-31 at 01 03 58" src="https://user-images.githubusercontent.com/122615093/228993032-18db2303-ba34-4820-9990-c54970cc4b0d.png">
