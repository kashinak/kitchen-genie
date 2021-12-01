const cloudName = "dcll7ella"; // replace with your own cloud name
const uploadPreset = "u1eizdsc"; // replace with your own upload preset

// Remove the comments from the code below to add
// additional functionality.
// Note that these are only a few examples, to see
// the full list of possible parameters that you
// can add see:
//   https://cloudinary.com/documentation/upload_widget_reference

const myWidget = cloudinary.createUploadWidget(
  {
    cloudName: cloudName,
    uploadPreset: uploadPreset,
    cropping: true, //add a cropping step
    // showAdvancedOptions: true,  //add advanced options (public_id and tag)
    sources: [ "local", "url"], // restrict the upload sources to URL and local files
    multiple: false,  //restrict upload to a single file
    folder: "kitchen_genie", //upload files to the specified folder
    tags: ["users", "profile"], //add the given tags to the uploaded files
    // context: {alt: "user_uploaded"}, //add the given context data to the uploaded files
    clientAllowedFormats: ["images"], //restrict uploading to image files only
    maxImageFileSize: 2000000,  //restrict file size to less than 2MB
    maxImageWidth: 500, //Scales the image down to a width of 2000 pixels before uploading
    // theme: "purple", //change to a purple theme
  },
  (error, result) => {
    if (!error && result && result.event === "success") {
      console.log("Done! Here is the image info: ", result.info);
      document
        .getElementById("uploadedimage")
        .setAttribute("src", result.info.secure_url);
    }
  }
);

document.getElementById("upload_widget").addEventListener(
  "click",
  function () {
    myWidget.open();
  },
  false
);

// cloudinary callback. Sets upload image url input
function imageUploaded(error, result) {
  $( '#recipe_image' ).prop("src", result[0].secure_url);
  $( '#recipe_image_url' ).val(result[0].secure_url);
}

// Shows the cloudinary image upload widget
$( "#upload_widget" ).click(function(event) {
  event.preventDefault();

  cloudinary.openUploadWidget(
    {
      cloud_name: 'dcll7ella',
      upload_preset: 'u1eizdsc'
    },
    imageUploaded);
});