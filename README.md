# KissSensor
Start a FaceTime session when you blow a kiss!

Put images into [data/normal]() and [data/kiss]().

## Usage
First, capture the training data. Use `normal` or `kiss` to denote the label. I captured ~1,000 photos (500 for kiss and normal each) 
and achieved 90% prediction correctness. So you may also need that more.

```
$ python camera_reader.py <label>
```


Second, train the model. 

```
$ python model_train.py
```

Finally, detect your kiss

```
$ python camera_reader.py
```

## Install
Install OpenCV, Anaconda.

Build an AppleScript with following code and put it somewhere appropriate (like your desktop)
```
set phone_num to "THE_PHONE_NUMBER_TO_CALL"
set faceTime to "FaceTime"
if application faceTime is running then
	return
end if
do shell script "open facetime://" & quoted form of phone_num
tell application "System Events"
	repeat while not (button "Call" of window 1 of application process faceTime exists)
		delay 1
	end repeat
	click button "Call" of window 1 of application process "FaceTime"
end tell
```

## Licence

[MIT](https://github.com/Hironsan/BossSensor/blob/master/LICENSE)

## Author

[Hironsan](https://github.com/Hironsan)