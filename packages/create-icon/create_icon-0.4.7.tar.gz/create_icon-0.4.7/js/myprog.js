 
// Prints the div only 

 function printDiv(divName) {
     var printContents = document.getElementById(divName).innerHTML;
     var originalContents = document.body.innerHTML;

     document.body.innerHTML = printContents;

     window.print();

     document.body.innerHTML = originalContents;
 }

// Makes the image 3 times as large as the original

 function enlargeImg(x) {
     x.style.height = "464px";
     x.style.width = "464px";
 }
// Reverts back to the original size

 function normalImg(x) {
     x.style.height = "132px";
     x.style.width = "132px";
 }
