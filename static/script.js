function previewImage() {
    const fileInput = document.getElementById("mriImage");
    const imagePreview = document.getElementById("imagePreview");
    const image = document.getElementById("image");

    const file = fileInput.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            image.src = e.target.result;
            imagePreview.style.display = "block";
        };

        reader.readAsDataURL(file);
    } else {
        imagePreview.style.display = "none";
    }
}
