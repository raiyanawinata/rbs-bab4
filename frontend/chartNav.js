// Buat chart menggunakan Chart.js
function createChart(data) {
    // Mengelompokkan judul buku berdasarkan kategori
    const categories = {};
    data.forEach(book => {
        if (!categories[book.kategori]) {
            categories[book.kategori] = 0;
        }
        categories[book.kategori]++;
    });

    // Mengambil nama-nama kategori dan total judul buku untuk setiap kategori
    let categoryNames = Object.keys(categories);
    let bookCounts = Object.values(categories);

    // Urutkan kategori berdasarkan jumlah buku (dari yang terbesar)
    const sortedIndices = bookCounts.map((_, i) => i).sort((a, b) => bookCounts[b] - bookCounts[a]);
    categoryNames = sortedIndices.map(index => categoryNames[index]).slice(0, 10);
    bookCounts = sortedIndices.map(index => bookCounts[index]).slice(0, 10);

    // Buat chart menggunakan Chart.js
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar', // Ubah tipe chart menjadi bar
        data: {
            labels: categoryNames,
            datasets: [{
                label: 'Persentase Popularitas Kategori',
                data: bookCounts, // Menggunakan jumlah buku langsung sebagai data
                backgroundColor: 'rgba(54, 162, 235, 0.5)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Lakukan permintaan GET ke endpoint Flask
fetch('http://127.0.0.1:5000/populer')
    .then(response => response.json())
    .then(data => {
        // Membuat diagram dari data kategori
        createChart(data);
    })
    .catch(error => console.error('Error:', error));
