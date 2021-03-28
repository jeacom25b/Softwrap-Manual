There are some tricks when using Softwrap that are useful to know.

## split viewport

you can work with two viewports and have the souce mesh on one side and the target on the other side.
This trick uses local view to hide the objects in each viewport so you can have a clear view of each object independently with synced view angles.  

to do it just split the viewport in two, enable lock camera to view in both and in one of them select the camera and the source mesh and switch to local view,
in the other select the camera and the target mesh and also switch to local view. now just switch to camera view in both viewports to have a synced view of
both objects while not having one obstruct the view of the other.

<a href="../img/split_viewport.mp4" target="_blank" rel="noopener noreferrer">
    <video autoplay loop muted playsinline src="../img/split_viewport.mp4" style='max-width:100%'></video>
</a>

<br>
<br>
<br>

## Add pins while paused

You can pause the simulation and still add pins, this is useful if you want a workflow where you first mark feature points and then start the wrapping.
You can also pause it even before clicking start.

<video autoplay loop muted playsinline src="../img/pause.mp4" style='max-width:100%'></video>

<br>
<br>
<br>

## Scale the pins.

Pins have an area of influence, you can scale them to change it.
![](img/a.mp4)
<video autoplay loop muted playsinline src="../img/pin_scale.mp4" style='max-width:100%'></video>
