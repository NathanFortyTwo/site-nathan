let arrayParent = []
let arrayChild = []

for (let i = 0; i <= 2; i++) {
    arrayParent.push(document.getElementById("card_"+i));
    arrayChild.push(document.getElementById("card_in_"+i));
    arrayParent[i].addEventListener("click", function() {
    console.log(arrayChild)
    arrayChild[i].classList.toggle("clicked");
    console.log(i)
    });
}

