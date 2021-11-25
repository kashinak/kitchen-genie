$(document).ready(function() {
    /* Add new ingredient in add recipe form */
    $("#btn-add-ingredient").on("click", function() {
        $('<input type="text" id="ingredient" class="form-control ingredients" name="ingredients" placeholder="1/4 cup olive oil" required />').insertBefore("#btn-add-ingredient");
    });

    /* Remove ingredient in add recipe form */
    $('#btn-remove-ingredient').on('click', function () {
        $("#ingredient-list input:last").remove();
    });

    /* Add new cooking preparation step in add recipe form */
    $("#btn-add-preparation").on("click", function() {
        $('<input type="text" class="form-control preparation" name="preparation" placeholder="Sauté onions, garlic, and peppers 5-7 minutes" required />').insertBefore("#btn-add-preparation");
    });

    /* Remove cooking recipe step in add recipe form */
    $('#btn-remove-preparation').on('click', function () {
        $("#preparation-list input:last").remove();
      });
    /* Cloudinary SDK installation */
    $.cloudinary.config({ cloud_name: 'dcll7ella', secure: true});
     
});