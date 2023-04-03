let arrayParent = []
let arrayChild = []
let NbCards = 3;
/* there has to be a cleaner way to do this... */

for (let i = 0; i < NbCards; i++) {
    arrayParent.push(document.getElementById("card_"+i));
    arrayChild.push(document.getElementById("card_in_"+i));
    arrayParent[i].addEventListener("click", function() {
    arrayChild[i].classList.toggle("clicked");
    console.log(i)
    });
}
