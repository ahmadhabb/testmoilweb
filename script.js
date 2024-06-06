document.getElementById('image-input').addEventListener('change', function(event) {
    var file = event.target.files[0];
    var reader = new FileReader();
    
    reader.onload = function(e) {
        var img = document.createElement("img");
        img.src = e.target.result;
        img.classList.add('max-h-full', 'max-w-full','overflow-auto'); // Menambahkan kelas Tailwind untuk memastikan gambar tidak melebihi lebar kontainer
        document.getElementById('image-container').innerHTML = ''; // Bersihkan kontainer sebelum menambahkan gambar baru
        document.getElementById('image-container').appendChild(img);
    };
    
    reader.readAsDataURL(file);
});

document.getElementById('rotate-left').addEventListener('click', function() {
    rotateImage(-1);
});

document.getElementById('rotate-right').addEventListener('click', function() {
    rotateImage(1);
});

document.getElementById('delete-image').addEventListener('click', function() {
    document.getElementById('image-container').innerHTML = ''; // Menghapus gambar dari container
    document.getElementById('rotation-value').value = ''; // Menghapus nilai rotasi dari input
});

document.getElementById('rotation-value').addEventListener('change', function() {
    var newRotation = parseInt(this.value) || 0; // Ambil nilai rotasi dari input teks
    rotateImage(newRotation); // Panggil fungsi rotateImage dengan nilai rotasi baru
});


document.getElementById('rotation-value').addEventListener('change', function() {
    var rotationValue = parseInt(this.value) || 0;
    rotateImage(rotationValue);
});

function rotateImage(rotation) {
    var img = document.querySelector('#image-container img');
    var currentRotation = parseInt(img.getAttribute('data-rotation') || 0);
    var newRotation = currentRotation + rotation;

    // Pastikan nilai rotasi berada dalam rentang 0 hingga 360 derajat
    newRotation = (newRotation + 360) % 360;

    img.style.transform = 'rotate(' + newRotation + 'deg)';
    img.setAttribute('data-rotation', newRotation);
    document.getElementById('rotation-value').value = newRotation + '°'; // Menampilkan nilai rotasi saat ini pada input
}
