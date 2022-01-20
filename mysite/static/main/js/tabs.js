function openTab(evt, tabName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
  
  // Get the element with id="defaultOpen" and click on it
  $(document).ready(document.getElementById(defaultOpen).click());
}

function download(file, text) {

    //creating an invisible element
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8, '
                         + encodeURIComponent(text));
    element.setAttribute('download', file);

    //the above code is equivalent to
    // <a href="path of file" download="file name">

    document.body.appendChild(element);

    //onClick property
    element.click();

    document.body.removeChild(element);
}

// Start file download.
document.getElementById("btn").addEventListener("click", function() {
    // Generate download of hello.txt file with some content
    var text = document.getElementById("text").value;
    var filename = "result.txt";

    download(filename, text);
}, false);