Convert specific ppt slides to images in linux, Ubuntu & Windows

Hi there!

My name is Shrinivaasan, 19. Heads up to you, this is my first library.

For a project I needed to convert ppt slides to jpg images in a linux instance,
but I was surprised to know that there was
no package to convert slides into images in Linux & Ubuntu.

Hence decided to create a package myself
that will work on linux, ubuntu, windows using just 2 external libraries which are also comaptible with linux & ubuntu

## Usage
- pip install ppt2img
- make sure you install python-pptx and download libreoffice


## Following have to be installed

    Library         Command to install
    -------         -----------------
    python-pptx      (pip install python-pptx)
    libreoffice      (sudo apt install libreoffice or 
                      download it from libreoffice.org)


In version 0.0.1 there is only one function,

ppt2img(inputppt,slideno,outputpath,imgformat,sofficepath)


## Expalanation of the function ppt2img()
1. inputppt : Path of source pptx. Should be in quotes like 'C:\Users\Dell\test.pptx'


2. slideno : Is a number(natural numbers only i.e 1,2,3,4,5,6,7 that it numbers from 1 increasing by 1)


3. outputpath : Path image output folder .Should be in quotes like 'C:\Users\Dell\imgoutput'


4. imgformat : Format of image. Should be in quotes and in lowercase like 'png' or 'jpg' 'jpeg'


5. sofficepath :

              a) In Windows/Linux computer :Path of LibreOffice installation. Generally stored at C:\ProgramFiles folder
                 Very Imp: Should be in double quotes like "C:\Program Files\LibreOffice\program\soffice.exe"
                 Example: to get the 2nd slide as image;

                         ppt2img('./ppt/test.pptx',2,'./imgoutput','jpg',"C:\Program Files\LibreOffice\program\soffice.exe")


              b) In Online Editor like Colab or Datalore: just type 'soffice' in the function in single quotes .
                 Example:to get the 2nd slide as image;

                        ppt2img('./ppt/test.pptx',2,'./imgoutput','jpg','soffice')

Contact me at : shravanshravan10@gmail.com