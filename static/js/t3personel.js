document.addEventListener('DOMContentLoaded', function() {
    // Buton ve tablo elementlerini seç
    const filtreleButton = document.getElementById('filtrele_0_btn');
    const tableBody = document.querySelector('#t3personel_table tbody');
    let isFiltering = false;

    if (filtreleButton && tableBody) {
        filtreleButton.addEventListener('click', function() {
            isFiltering = !isFiltering;
            
            // Butonun görünümünü güncelle
            if (isFiltering) {
                filtreleButton.classList.remove('btn-outline-primary');
                filtreleButton.classList.add('btn-primary');
                filtreleButton.innerHTML = '<i class="fas fa-eye me-1"></i>Tüm Verileri Göster';
            } else {
                filtreleButton.classList.remove('btn-primary');
                filtreleButton.classList.add('btn-outline-primary');
                filtreleButton.innerHTML = '<i class="fas fa-eye-slash me-1"></i>0 Verilerini Gizle';
            }

            // Tüm satırları kontrol et
            const rows = tableBody.getElementsByTagName('tr');
            Array.from(rows).forEach(row => {
                // Eğer normal veri satırı ise (colspan olmayan)
                if (!row.querySelector('td[colspan]')) {
                    const ogle = parseInt(row.getAttribute('data-ogle')) || 0;
                    const aksam = parseInt(row.getAttribute('data-aksam')) || 0;
                    const lunchbox = parseInt(row.getAttribute('data-lunchbox')) || 0;
                    const coffee = parseInt(row.getAttribute('data-coffee')) || 0;

                    // Tüm değerler 0 ise ve filtreleme aktifse satırı gizle
                    if (isFiltering && ogle === 0 && aksam === 0 && lunchbox === 0 && coffee === 0) {
                        row.style.display = 'none';
                    } else {
                        row.style.display = '';
                    }
                }
            });

            // Konsola debug bilgisi yaz
            console.log('Filtreleme durumu:', isFiltering);
            console.log('İşlenen satır sayısı:', rows.length);
        });

        // Başlangıçta butonun durumunu ayarla
        filtreleButton.innerHTML = '<i class="fas fa-eye-slash me-1"></i>0 Verilerini Gizle';
        filtreleButton.classList.add('btn-outline-primary');
    } else {
        console.error('Buton veya tablo bulunamadı!');
    }
}); 