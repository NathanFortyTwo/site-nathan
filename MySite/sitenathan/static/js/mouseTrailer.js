const trailer =document.getElementById("trailer")
window.onmousemove = e => {


    const x = e.clientX - trailer.offsetWidth/2,
          y= e.clientY - trailer.offsetHeight/2;
    const keyframe = {
        transform:`translate(${x}px, ${y}px)`
    }
trailer.animate(keyframe,{
    duration : 10000
});
}
