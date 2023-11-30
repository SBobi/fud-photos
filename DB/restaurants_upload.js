const admin = require("firebase-admin");
const serviceAccount = require("./key_service_account.json");

const data = require("./restaurant_data.json");
const collectionKey = "Restaurant";

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});

const firestore = admin.firestore();
const settings = { timestampsInSnapshots: true };
firestore.settings(settings);

if (data && typeof data === "object") {
  Object.keys(data).forEach((docKey) => {
    const restaurantData = data[docKey];

    // Convert "lat" and "lon" to GeoPoint
    const geoPoint = new admin.firestore.GeoPoint(
      restaurantData.lat,
      restaurantData.lon
    );

    // Replace "lat" and "lon" with the GeoPoint
    restaurantData.location = geoPoint;
    delete restaurantData.lat;
    delete restaurantData.lon;

    firestore
      .collection(collectionKey)
      .doc(docKey)
      .set(restaurantData)
      .then((res) => {
        console.log("Document " + docKey + " successfully written!");
      })
      .catch((error) => {
        console.error("Error writing document: ", error);
      });
  });
}
