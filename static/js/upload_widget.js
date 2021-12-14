// Code modeled after Sean Young's Cloudinary post on Slack
// Displays recipe image that was uploaded in add recipe form now showing in edit recipe form
$( "#recipe_image_url" ).on('change', function(event) {
  $( '#recipe_image' ).prop("src", $( this ).val());
});

// Cloudinary callback. Sets input value with recipe image url
function imageUploaded(error, result) {
  $( '#recipe_image' ).prop("src", result[0].secure_url);
  $( '#recipe_image_url' ).val(result[0].secure_url);
}