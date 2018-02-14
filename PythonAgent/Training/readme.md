# Training Module

This Module is used for all sorts of training.
Results of any training and source of any training must be stored here.
Do not store training data else where.

### Module Screen Capture

To import this module use either of the following
```sh
> from Training import screencapture
```
or
```sh
> import Training.screencapture
```

##### Module Usage
This Module Consist of only one class called ScreenShot
Initilizing ScreenShot Class
```sh
    shot = screencapture.ScreenShot(Param)
```
This Class has a `__init__()` which accepts 5 argument which is mandatory.
```sh
    __init__(self,point1x,point1y,point2x,point2y,saveOption)
```
1. self : this parameter passed by python (so dont worry about it Hell Yea..)
2. `point1x` : Top Left point of the screen's x axis.(int)
3. `point1y` : Top Left Point of the screen;s y axis.(int)
4. `point2x` : Bottom Right of the screeen's x axis.(int)
5. `point2y` : Bottom Right of the screen's y axis.(int)
6. `saveOption` : Enables to (save/not save) of images (boolean[True/False])

usage:
```sh
    sshot1 = screencapture.ScreenShot(0,0,400,400,True) //True will Enabe to save Image.
    sshot2 = screencaptere.ScreenShot(0,0,400,400,False) // False will Disable saving Of Image.
```
![axis](Tumbnails/Demo1.png)

The follwoing function can be applied on the ScreenShot object.
* `setSaveLocation(Param)`
* `showFrameCaptureTime(Param)`
* `resizeImage(Param)`
* `Init()`

##### 1. setSaveLocation(Param) accepts 2 parameter
This Function will override the Default save location and Name of the Image.
Any location you pass will be relative to the current working directory.
Default Save location is `\Training\Images` and Image Name is `Image`
```sh
    (ScreenShot_object).setSaveLocation(fName,Loc)    
```
1. `FName` : Name of the Image.(string) (Default `Image`)
2. `Loc` : Location where Images should be saved.(string) (Default `\Trainting\Images`)

Usage:
```sh
    sshot = screencapture.ScreenShot(0,0,400,400,True)
    sshot.setSaveLocation("capture","\\Training\\Images\\Wow\\")
```
Note: When ever you are passing location make sure the path is defined between `\\path\\`

##### 2. showFrameCaptureTime(param) accepts 1 parameter
This Function will print the seconds it took to capture the image.
```sh
    (ScreenShot_object).showFrameCaptureTime(Enable)
```
1. `Enable` : this will Trigger the Print Event.(boolean[True/False])

Usage:
```sh
    sshot = screencapture.ScreenShot(0,0,400,400,True)
    sshot.showFramCaptureTime(True) // will enable printing of the Time(seconds)
```

##### 3. resizeImage(Param) accepts 3 parameter
This Function will Resize the image according to your prefrence.
```sh
    (ScreenShot_object).resizeImage(x,y,Enable)
```
1. `x` : size of the Width
2. `y` : size of the height
3. `Enable` : Trigger for Enabling and Disabling Resize. (Default False)

Usage:
```sh
    sshot = screencapture.ScreenShot(0,0,400,400,True)
    sshot.resizeImage(20,20,True) // will Enable the Resizing of image.
```

##### 4. Init() accepts 0 parameter.
This is the Function which will Execute the Screenshot Object using the above configuration function.
The above three function are like configuring the object and this `Init()` function will execute the object by capturing saving and resizing the image continously.

Usage:
```sh
    sshot = screencapture.ScreenShot(0,0,400,400,True) // creating object.
    sshot.Init()                                       // Running/Executing the Object.
```
the above two line of code will perform capturing screen using Default Configuration.
The default Configuration can be overrided by the following code.

```sh
    sshot = screencapture.ScreenShot(0,0,400,400,True) // creating object.
    sshot.setSaveLocation("capture","\\Training\\Img\\") // overriding the default save location
    sshot.showFrameCaptureTime(True) // Enabling Printing of Time.
    sshot.resizeImage(40,40,True) // resizing the image from 400x400 to 40x40
    sshot.Init() // will use the above three function config and Execute the Object.
```

