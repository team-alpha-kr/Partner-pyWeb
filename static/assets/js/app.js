function getParam(key){var _parammap={};document.location.search.replace(/\??(?:([^=]+)=([^&]*)&?)/g,function(){function decode(s){return decodeURIComponent(s.split("+").join(" "));}
_parammap[decode(arguments[1])]=decode(arguments[2]);});return _parammap[key];}

function includeHTML(){var z,i,elmnt,file,xhttp;z=document.getElementsByTagName("*");for(i=0;i<z.length;i++){elmnt=z[i];file=elmnt.getAttribute("include-html");if(file){xhttp=new XMLHttpRequest();xhttp.onreadystatechange=function(){if(this.readyState==4){if(this.status==200){elmnt.innerHTML=this.responseText;}
if(this.status==404){elmnt.innerHTML="Page not found.";}
elmnt.removeAttribute("include-html");}}
xhttp.open("GET",file,true);xhttp.send();return;}}}