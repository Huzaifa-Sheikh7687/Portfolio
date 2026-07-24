import { useEffect } from "react";

export default function TawkChat() {
  useEffect(() => {
    var Tawk_API = window.Tawk_API || {};
    var Tawk_LoadStart = new Date();

    (function () {
      var s1 = document.createElement("script"),
        s0 = document.getElementsByTagName("script")[0];
      s1.async = true;
      s1.src = "https://embed.tawk.to/6a633c5eab56b61d47724bbc/1ju9q7k9m";
      s1.charset = "UTF-8";
      s1.setAttribute("crossorigin", "*");
      s0.parentNode.insertBefore(s1, s0);
    })();

    window.Tawk_API = Tawk_API;
    window.Tawk_LoadStart = Tawk_LoadStart;
  }, []);

  return null; // ye component kuch render nahi karta, sirf script inject karta hai
}
