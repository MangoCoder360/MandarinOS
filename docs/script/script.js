function hideLoader() {
  var loader = document.getElementById("loader");
  loader.style.display = "none";
}

function submitLogin() {
  var username = document.getElementById("usrname").value;
  var password = document.getElementById("psword").value;
  document.getElementById("loginPlaceholder").innerHTML = "Please wait while we sign you in...";
  var loader = document.getElementById("loader");
  loader.style.display = "block";
}
