import { initializeApp } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyDhMcu6b49knv0-v9oF8jR7wu61yylY9e0",
  authDomain: "modern-pandavas.firebaseapp.com",
  projectId: "modern-pandavas",
  storageBucket: "modern-pandavas.firebasestorage.app",
  messagingSenderId: "18867784003",
  appId: "1:18867784003:web:9d967d516f70efea2987f6"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const db = getFirestore(app);
