---
skip_header: true
---

<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="https://www.gstatic.com/firebasejs/8.2.1/firebase-app.js"></script>

<!-- TODO: Add SDKs for Firebase products that you want to use
     https://firebase.google.com/docs/web/setup#available-libraries -->
<script src="https://www.gstatic.com/firebasejs/8.2.1/firebase-analytics.js"></script>

<script>
  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  var firebaseConfig = {
    apiKey: "AIzaSyCpxGW-WWjQ81puR3BFuj4-ELQXZk2hnac",
    authDomain: "rnr-character-saver.firebaseapp.com",
    projectId: "rnr-character-saver",
    storageBucket: "rnr-character-saver.appspot.com",
    messagingSenderId: "967788923020",
    appId: "1:967788923020:web:5f4a10d8d79904225493a9",
    measurementId: "G-Z89NC4VGDX"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();
</script>

<script src="https://www.gstatic.com/firebasejs/8.2.1/firebase-auth.js"></script>
<script src="https://www.gstatic.com/firebasejs/ui/4.6.1/firebase-ui-auth.js"></script>
<link type="text/css" rel="stylesheet" href="https://www.gstatic.com/firebasejs/ui/4.6.1/firebase-ui-auth.css" />


<script>
  var ui = new firebaseui.auth.AuthUI(firebase.auth());
  var uiConfig = {
  callbacks: {
      signInSuccessWithAuthResult: function(authResult, redirectUrl) {
        // User successfully signed in.
        // Return type determines whether we continue the redirect automatically
        // or whether we leave that to developer to handle.
        return true;
      },
      uiShown: function() {
        // The widget is rendered.
        // Hide the loader.
        document.getElementById('loader').style.display = 'none';
      }
    },
    // Will use popup for IDP Providers sign-in flow instead of the default, redirect.
    signInFlow: 'popup',
    signInSuccessUrl: 'zombo.com',
    signInOptions: [
      firebase.auth.EmailAuthProvider.PROVIDER_ID
    ],
    // Terms of service url.
    tosUrl: 'google.com',
    // Privacy policy url.
    privacyPolicyUrl: 'kotaku.com'
  };
  ui.start('#firebaseui-auth-container', uiConfig);


</script>

<!-- The surrounding HTML is left untouched by FirebaseUI.
     Your app may use that space for branding, controls and other customizations.-->
<h1>Welcome to My Awesome App</h1>
<div id="firebaseui-auth-container"></div>
<div id="loader">Loading...</div>