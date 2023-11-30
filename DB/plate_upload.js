const admin = require("firebase-admin");
const serviceAccount = require("./key_service_account.json");

const data = require("./plate_data_2.json");
const collectionKey = "Product";

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});

const firestore = admin.firestore();
const settings = { timestampsInSnapshots: true };
firestore.settings(settings);

if (data && typeof data === "object") {
  Object.keys(data).forEach((docKey) => {
    const plateData = data[docKey];

    firestore
      .collection(collectionKey)
      .doc(docKey)
      .set(plateData)
      .then((res) => {
        console.log("Document " + docKey + " successfully written!");
      })
      .catch((error) => {
        console.error("Error writing document: ", error);
      });
  });
}
