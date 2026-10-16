// auth.js
import { auth, db } from "./firebase.js";

import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  sendPasswordResetEmail,
  signOut
} from "https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js";

import {
  doc,
  setDoc
} from "https://www.gstatic.com/firebasejs/12.8.0/firebase-firestore.js";

/* ================= PASSWORD RULE ================= */
const passwordRegex =
  /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$/;

/* ================= REGISTER ================= */
window.registerUser = async () => {
  const username = document.getElementById("username").value.trim();
  const email = document.getElementById("email").value.trim();
  const pass = document.getElementById("password").value;
  const cpass = document.getElementById("confirm_password").value;
  const msg = document.getElementById("error"); // reuse this for success/error

  msg.textContent = "";
  msg.style.color = "red";

  if (!passwordRegex.test(pass)) {
    msg.textContent =
      "Password must be at least 8 characters with uppercase, lowercase, number & symbol";
    return;
  }

  if (pass !== cpass) {
    msg.textContent = "Passwords do not match";
    return;
  }

  try {
    const cred = await createUserWithEmailAndPassword(auth, email, pass);

    await setDoc(doc(db, "users", cred.user.uid), {
      username,
      email,
      createdAt: new Date()
    });

    // ✅ SUCCESS MESSAGE (PRINTED)
    msg.style.color = "green";
    msg.textContent =
      "✅ Account created successfully! Redirecting to login...";

    // ⏳ Give user time to see message
    setTimeout(() => {
      window.location.href = "index.html";
    }, 2000);

  } catch (err) {
    msg.style.color = "red";

    if (err.code === "auth/email-already-in-use") {
      msg.textContent = "Account already exists. Please login.";
    } else if (err.code === "auth/invalid-email") {
      msg.textContent = "Invalid email format.";
    } else {
      msg.textContent = err.message;
    }
  }
};

/* ================= LOGIN ================= */
window.loginUser = async () => {
  const email = document.getElementById("login_user").value.trim();
  const pass = document.getElementById("login_pass").value;

  try {
    await signInWithEmailAndPassword(auth, email, pass);
    window.location.href = "index.html";

  } catch (err) {
    switch (err.code) {
      case "auth/user-not-found":
        alert("No account found with this email. Please register first.");
        break;
      case "auth/wrong-password":
        alert("Incorrect password.");
        break;
      case "auth/invalid-email":
        alert("Invalid email address.");
        break;
      case "auth/too-many-requests":
        alert("Too many attempts. Try again later or reset password.");
        break;
      default:
        alert("Login failed. Try again.");
    }
  }
};

/* ================= FORGOT PASSWORD ================= */
window.forgotPassword = async () => {
  const email = document.getElementById("login_user").value.trim();

  if (!email) {
    alert("Please enter your email first");
    return;
  }

  try {
    await sendPasswordResetEmail(auth, email);
    alert("Password reset email sent. Check inbox or spam.");

  } catch (err) {
    if (err.code === "auth/user-not-found") {
      alert("No account found with this email.");
    } else if (err.code === "auth/invalid-email") {
      alert("Invalid email address.");
    } else {
      alert(err.message);
    }
  }
};

/* ================= LOGOUT ================= */
window.logout = async () => {
  try {
    await signOut(auth);
    window.location.href = "login.html";
  } catch (err) {
    alert("Error logging out. Try again.");
  }
};
